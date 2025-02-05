# Используем базовый образ Python
FROM python:3.9-slim

# Установка системных библиотек (включая SQLite)
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем приложение
COPY . .

# Запускаем сервер
CMD ["python", "app.py"]
