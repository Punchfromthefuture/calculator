#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "=== Установка проекта ==="

if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv
else
    echo "Виртуальное окружение уже существует."
fi

echo "Установка зависимостей..."
./venv/bin/python -m pip install -r requirements.txt

echo "Инициализация базы данных..."
./venv/bin/python -c "import db_manager; db_manager.init_db()"

echo "✅ Установка завершена."
