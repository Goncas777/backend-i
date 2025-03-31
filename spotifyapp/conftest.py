import subprocess
import pytest

import pytest
from django.conf import settings

@pytest.fixture(scope='session')
def change_db_settings():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'qwerty',
        'HOST': 'database',  # Nome do serviço de banco de dados no Docker
        'PORT': '5432',
    }
    # O Django usa essa configuração para o banco de dados durante os testes
    yield
    # Qualquer limpeza ou reversão das configurações pode ser feita aqui

