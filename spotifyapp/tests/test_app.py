import pytest
import json
import os
import django
import tempfile
import logging

# Configura o Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'spotify.settings'
django.setup()

# Configura o logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Importa os modelos e funções do Django
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from stats.models import UploadedFile
from stats.views import process_json_file, format_duration

def test_signup_view(client, db):
    logger.info("Testando o signup view.")
    response = client.post("/signup/", {"username": "testuser", "password": "testpass", "password2": "testpass"})
    assert response.status_code == 302  # Redirect após sucesso
    assert User.objects.filter(username="testuser").exists()
    logger.info("Signup test passou com sucesso.")

def test_upload_file_view(client, db, django_user_model):
    logger.info("Testando upload de ficheiro.")
    user = django_user_model.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")

    fake_file = SimpleUploadedFile("test.zip", b"dummy content", content_type="application/zip")
    response = client.post("/upload/", {"file": fake_file})

    assert response.status_code == 302  # Redirect após upload
    assert UploadedFile.objects.filter(file="uploads/test.zip").exists()
    logger.info("Upload de ficheiro testado com sucesso.")

def test_process_json_file():
    logger.info("Testando processamento de JSON.")
    sample_data = [
        {
            "master_metadata_album_artist_name": "Lil Yachty",
            "master_metadata_track_name": "Flex Up",
            "master_metadata_album_album_name": "Lil Boat 3.5",
            "ms_played": 170858
        },
        {
            "master_metadata_album_artist_name": "21 Savage",
            "master_metadata_track_name": "ball w/o you",
            "master_metadata_album_album_name": "i am > i was",
            "ms_played": 195046
        }
    ]

    summary_data = {}

    # Criar um arquivo temporário para simular o JSON
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
        json.dump(sample_data, temp_file)
        temp_file_path = temp_file.name

    logger.debug(f"Arquivo temporário criado: {temp_file_path}")

    # Chamar a função com o caminho do arquivo temporário
    process_json_file(temp_file_path, summary_data)

    logger.debug(f"Resumo dos dados processados: {summary_data}")

    # Verificar se os dados foram processados corretamente
    assert "Lil Yachty" in summary_data
    assert "21 Savage" in summary_data
    assert summary_data["Lil Yachty"]["total_play_time"] == 170858
    assert summary_data["21 Savage"]["total_play_time"] == 195046

    logger.info("Processamento de JSON testado com sucesso.")
