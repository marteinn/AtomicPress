init:
    pip install -r requirements.txt

migrate:
    python manage.py db migrate -d=atomicpress/migrations/

upgrade:
    python manage.py db upgrade -d=atomicpress/migrations/