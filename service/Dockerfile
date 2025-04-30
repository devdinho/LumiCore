FROM python:3.12.6-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev postgresql-dev \
    && pip install poetry black isort flake8\
    && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 8003

CMD ["sh", "./scripts/start.sh"]