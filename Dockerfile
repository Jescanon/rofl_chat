FROM python:3.11-slim
LABEL authors="jecanon"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend ./backend

COPY alembic.ini .