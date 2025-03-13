FROM python:3.12-alpine

WORKDIR /workspace

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

CMD poetry run python src/session_9/bot.py