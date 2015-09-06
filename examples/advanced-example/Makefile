runserver_dev:
	export ATOMICPRESS_SETTINGS=settings.prod && python manage.py runserver -a -d

runserver_prod:
	export ATOMICPRESS_SETTINGS=settings.prod && python manage.py runserver

sync:
	export ATOMICPRESS_SETTINGS=settings.prod && python manage.py s3 sync

export:
	export ATOMICPRESS_SETTINGS=settings.prod && python manage.py exporter export
