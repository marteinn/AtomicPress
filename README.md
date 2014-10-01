# AtomicPress

AtomicPress is a static blog generator modeled after WordPress data models.
It is built in Flask and takes advantage of it's awesome eco-system such as
Flask-Freeze, Flask-Admin, Flask-Migrations, Flask-SQLAlchemy, to mention a few.


## Features

- Ports, Pages, Categories, Tags and Authors, almost like WordPress.
- Markdown rendering
- Theme support
- Import from Wordpress
- Gist integration
- Admin interface


## Getting started

To install AtomicPress you'll need python 2.7 and pip.


## Filters

### code

	[code][/code]
	
### gist

	[gist id="asdasd"]
	
### image

Embed image path.

	<img src="[image id="myimage.jpg"]" />
	>>> <img src="/uploads/myimage.jpg" />

## Commands

### Updating from a older version

    python manage.py upgrade -d=atomicpress/migrations/


### Importing

AtomicPress uses wpparser to import data from wordpress export files.

    python manage.py importer import_blog -f=./data/blog.wordpress.2014-09-25.xml


### Exporting

    python manage.py exporter export
    
    
### Sync through ftp

	python manage.py ftp sync


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

AtomicPress is released under the [MIT License](http://www.opensource.org/licenses/MIT).
