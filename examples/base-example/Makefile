export ATOMICPRESS_SETTINGS=settings.prod

init:
	pip install -r requirements/install.txt
	mkdir uploads
	python manage.py create_db
	python manage.py prefill fill

run_dev:
	python manage.py runserver -a -d

run:
	python manage.py runserver

sync:
	python manage.py s3 sync

export:
	python manage.py exporter export
