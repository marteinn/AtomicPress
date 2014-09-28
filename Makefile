init:
	pip install -r requirements.txt

migrate:
    . bin/activate; python manage.py db migrate -d=atomicpress/migrations/

upgrade:
    . bin/activate; python manage.py db upgrade -d=atomicpress/migrations/