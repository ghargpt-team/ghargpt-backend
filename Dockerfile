FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VERSION=1.8.3
ENV POETRY_VENV=/opt/poetry-venv

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    ca-certificates \
    openssl \
    libssl-dev \
    dnsutils \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app
COPY . .

WORKDIR /app/apps/api
RUN poetry config virtualenvs.create false \
    && poetry install --only=main --no-dev --no-interaction

WORKDIR /app
EXPOSE 8000

CMD cd /app/apps/api && poetry run uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}