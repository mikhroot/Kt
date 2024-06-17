Шаг 1: Клонирование репозитория:

git clone https://github.com/mikhroot/Kt
cd practice

Шаг 2: Создайте виртуальное окружение и активируйте его:
python -m venv venv
source venv/bin/activate

Шаг 3: Установите зависимости:
pip install -r requirements.txt

Шаг 4: Cоздание и миграция базы данных:
flask db init
flask db migrate
flask db upgrade

Шаг 5: Произведите настройку переменных окружений в .env файле

Шаг 6: Запустите приложение:
python app.py

Доступ: http://127.0.0.1:5000/
