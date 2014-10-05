ATOMICPRESS_SETTINGS:=settings

init:
	pip install -r requirements.txt
	mkdir uploads
	python manage.py create_db
	python manage.py prefill fill

run:
	python manage.py runserver -a

export:
	python manage.py exporter export
