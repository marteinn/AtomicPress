# AtomicPress

AtomicPress is a static blog generator modeled after WordPress data models.
It is built in Flask and takes advantage of it's awesome eco-system such as
Flask-Freeze, Flask-Admin, Flask-Migrations, Flask-SQLAlchemy, to mention a few.


## Features

- Ports, Pages, Categories, Tags and Authors (like WordPress).
- Markdown rendering
- Theme support
- Import from Wordpress
- Gist integration
- Admin interface
- Sync your generated blog with either ftp or to Amazon S3


## Getting started

To install AtomicPress you'll need python 2.7 and pip.


## TODO:Settings


## Themes

AtomicPress ships with the minimal theme per default, if you would like to make your own, just specify the path in your settings file.

	THEME=mytheme

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

### Database

#### Create database

	python mange.py create_db
	
#### Remove database

	python mange.py drop_db
	
**Options**

	-r remove
	-f force
	
#### Updating from a older version

    python manage.py upgrade -d=atomicpress/migrations/
    
### Prefill db with initial data

	python manage.py prefill fill
	


### Server

#### Runserver

	python manage.py runserver 
	
**Options**

	-a admin
	-t toolbar
	-d debug

### Import

#### Importing

AtomicPress uses wpparser to import data from wordpress export files.

    python manage.py importer import_blog -f=./data/blog.wordpress.2014-09-25.xml

### Export

    python manage.py exporter export

### Sync
    
#### S3

	python manage.py s3 sync
    
#### FTP

	python manage.py ftp sync
	



## Extensions

### Toggle extensions

AtomicPress uses a pluggale extension system, similar to django's INSTALLED_APPS.
To disable a plugin, define a property in your settings file and just define the ones you need.

	EXTENSIONS = (
	    # "atomicpress.ext.importer",
	    "atomicpress.ext.exporter",
	    "atomicpress.ext.ftp",
	    "atomicpress.ext.s3",
	    "atomicpress.ext.prefill",
	)
	
Activating you own is also simple, like this extension called catpictures:

	EXTENSIONS = (
	    "atomicpress.ext.importer",
	    "atomicpress.ext.exporter",
	    "atomicpress.ext.ftp",
	    "atomicpress.ext.s3",
	    "atomicpress.ext.prefill",
	    "catpictures",
	)
	
### Create extension

To create a extension, create a module with a function called setup. Thats all you need.



## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

AtomicPress is released under the [MIT License](http://www.opensource.org/licenses/MIT).
