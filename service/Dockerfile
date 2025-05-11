FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    build-essential \
    && pip install poetry black isort flake8 \
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 8003

CMD ["sh", "./scripts/start.sh"]