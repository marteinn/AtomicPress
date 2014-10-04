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

	[code]var a = 1;[/code]
	>>> <pre class="code">var a = 1;</pre>
	
### gist

Embeds a gist to content.

	[gist id="asdasd"]
	
### image

Embed image path.

	<img src="[image id="myimage.jpg"]" />
	>>> <img src="/uploads/myimage.jpg" />

## Commands


### Importing

AtomicPress uses wpparser to import data from wordpress export files.

    python manage.py importer import_blog -f=./data/blog.wordpress.2014-09-25.xml


### Create database

	python mange.py create_Db
	
### Remove database

	python mange.py drop_db
	
**Options**

	-r remove
	-f force
	
### Runserver

	python manage.py runserver 
	
**Options**

	-a admin
	-t toolbar
	-d debug

### Exporting

    python manage.py exporter export
    
### Sync through S3

	python manage.py s3 sync
    
### Sync through FTP

	python manage.py ftp sync
	
### Prefill db with initial data

	python manage.py prefill fill
	
### Updating from a older version

    python manage.py upgrade -d=atomicpress/migrations/



## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

AtomicPress is released under the [MIT License](http://www.opensource.org/licenses/MIT).
