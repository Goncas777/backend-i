import subprocess
import pytest

@pytest.fixture(scope="session", autouse=True)
def run_migrations():
    # Executa o comando make compose.migrate antes dos testes
    subprocess.run(["make", "migrations"], check=True)
def run_migrate():
    # Executa o comando make compose.migrate antes dos testes
    subprocess.run(["make", "compose.migrate"], check=True)
