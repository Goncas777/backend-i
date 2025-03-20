FROM python:3.12-slim

WORKDIR /workspace

RUN pip install poetry

COPY . .

RUN poetry install -nq

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "uvicorn"]

CMD ["uvicorn", "session_13.main:app", "--host", "0.0.0.0", "--port", "8000"]