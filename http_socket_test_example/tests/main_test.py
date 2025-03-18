import pytest
import subprocess
import requests

@pytest.fixture
def server():
    process = subprocess.Popen(
        ["poetry", "run", "python", "../src/http_socket_test_example/main.py"]
    )
    process.wait(timeout=10)
    yield process
    process.terminate()
    process.kill()

def test_response(server):
    assert server
    response = requests.get("http://localhost:8080")
    assert response.status_code == 200
