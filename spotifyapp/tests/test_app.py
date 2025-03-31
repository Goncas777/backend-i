import pytest
import json
import os
import django
import subprocess

# Configura o Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'spotify.settings'
django.setup()

# Importa os modelos e funções do Django
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from stats.models import UploadedFile
from stats.views import process_zip_and_generate_summary


@pytest.fixture(scope="session", autouse=True)
def run_migrations():
    # Executa o comando make compose.migrate antes dos testes
    result = subprocess.run(
        ["make", "compose.migrate"], capture_output=True, text=True
    )
    
    if result.returncode != 0:
        pytest.fail(f"Erro ao executar migrações: {result.stderr}")
    else:
        print(result.stdout)  # Isso pode ajudar a verificar a saída das migrações.


def test_signup_view(client, db):
    response = client.post("/signup/", {"username": "testuser", "password": "testpass", "password2": "testpass"})
    assert response.status_code == 302  # Redirect após sucesso
    assert User.objects.filter(username="testuser").exists()


def test_upload_file_view(client, db, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")
    
    fake_file = SimpleUploadedFile("test.zip", b"dummy content", content_type="application/zip")
    response = client.post("/upload/", {"file": fake_file})
    
    assert response.status_code == 302  # Redirect após upload
    assert UploadedFile.objects.filter(file="uploads/test.zip").exists()


def test_process_zip_and_generate_summary(tmp_path, db):
    zip_path = tmp_path / "test.zip"
    with open(zip_path, "wb") as f:
        f.write(b"dummy data")
    
    output_file = tmp_path / "summary.json"
    
    try:
        process_zip_and_generate_summary(str(zip_path), str(output_file))
        assert os.path.exists(output_file)
    except Exception as e:
        pytest.fail(f"Erro ao processar ZIP: {e}")


def test_show_summary(client, db, tmp_path):
    summary_file = os.path.join(settings.MEDIA_ROOT, "extracted", "summary.json")
    os.makedirs(os.path.dirname(summary_file), exist_ok=True)
    
    with open(summary_file, "w") as f:
        json.dump({"test": "data"}, f)
    
    response = client.get("/summary/")
    assert response.status_code == 200
    assert "test" in response.content.decode()


def test_show_summary_not_found(client):
    response = client.get("/summary/")
    assert response.status_code == 404


def test_download_summary(client, db, tmp_path):
    summary_file_path = os.path.join(settings.MEDIA_ROOT, "extracted", "summary.json")
    os.makedirs(os.path.dirname(summary_file_path), exist_ok=True)
    
    with open(summary_file_path, "w") as f:
        json.dump({"data": "test"}, f)
    
    response = client.get("/download_summary/")
    assert response.status_code == 200
    assert response["Content-Disposition"] == 'attachment; filename="summary.json"'


def test_download_summary_not_found(client):
    response = client.get("/download_summary/")
    assert response.status_code == 404
