# AtomicPress

AtomicPress is a static blog generator for python developers that don't want the Wordpress security hassle.
It is built in Flask and takes advantage of it's awesome eco-system such as Flask-Freeze, Flask-Admin, Flask-Migrations, Flask-SQLAlchemy, to mention a few. It utilizes SQLite for its database needs.


## Features

- Posts, Pages, Categories, Tags and Authors (like WordPress).
- Markdown rendering
- Theme support
- Import from Wordpress
- Gist integration
- A simple admin interface
- Build you own extensions
- Sync your generated blog with either FTP or to Amazon S3


## Why not Pelican/Jekyll/Octopress/Hyde? 

1. AtomicPress is built in Python.
2. It is built upon Flask, which is easy to extend.
3. It's built to make Wordpress import simple.


## Installation

AtomicPress can easily be installed through pip.

    pip install atomicpress


### Develop

    pip install git+git://github.com/marteinn/AtomicPress.git@develop


## Getting started

To install AtomicPress you'll need python 2.7, virtualenv and pip.

If you want a quickstart, just copy the example `base-example`, cd and type `make init` and you are ready to go.


## Settings

- `SQLALCHEMY_DATABASE_URI`: Path to your sqlite database.
- `DEBUG`: Show errors, should be deactivated for live environments.
- `SECRET_KEY`: Session key for signing.
- `STATIC_URL`: Path to the static content, default: `/static/`
- `UPLOADS_URL`: Path to the uploads folder, defult `/uploads/`
- `THEME`: The theme you want to run, default is `atomicpress.themes.minimal`.
- `GIST_BACKEND_RENDERING`: If you want to render a `<noscript></noscript>` that contains the gist content as pure text. Default is `False`
- `EXTENSIONS`: A array with the extensions you want to run.
- `MARKDOWN_EXTENSIONS`: A list with the active [markdown extensions](https://pythonhosted.org/Markdown/extensions/index.html).

### S3
- `AWS_ACCESS_KEY_ID`: Access key id to aws.
- `AWS_ACCESS_KEY`: Access key to aws.
- `AWS_REGION`: The region your bucket is places (optional).
- `AWS_S3_CALLING_FORMAT`: A boto setting (uses SubdomainCallingFormat by default) (optional).
- `S3_BUCKET`: The bucket you want to deploy to.
- `S3_DESTINATION`: The path within the bucket you want to deploy to.

### FTP

- `FTP_HOST`: Hostname to your ftp account.
- `FTP_USERNAME`: Ftp username.
- `FTP_PASSWORD`: Ftp password.
- `FTP_DESTINATION`: Ftp sup

## Admin

AtomicPress uses Flask-Admin to show a admin interface, you can access it by running `runserver` with the argument `-a` (admin). Per default is located at `http://localhost:5000/admin/`.


## Themes

AtomicPress ships with the theme minimal per default, if you would like to make your own, just specify the path in your settings file.

    THEME=mytheme

To make your own, just look at the theme [minimal](https://github.com/marteinn/AtomicPress/tree/develop/atomicpress/themes/minimal) that ships with AtomicPress.

## Filters

AtomicPress comes with a couple of filters you can use in the post content area.

### code

Render a basic code snippet.

    [code]var a = 1;[/code]
    >>> <pre class="code">var a = 1;</pre>

### gist

Embeds a more advanced code snippet through a github gist to content.

    [gist id="asdasd"]

### image

Embed image path with the `[image]` filter.

    <img src="[image id="myimage.jpg"]" />
    >>> <img src="/uploads/myimage.jpg" />

If you only want the uploads path, you can use the `[uploads]` filter.

    <img src="[uploads]myimage.jpg" />
    >>> <img src="/uploads/myimage.jpg" />

## Commands

### Database

#### Create database

Creates the database and stores it according to the SQLALCHEMY_DATABASE_UR path.

    python mange.py create_db

#### Remove database

Removes the sqlite database file.

    python mange.py drop_db

**Options**

    -r (remove) Remove the sqlite file when done.
    -f (force) Do now show the agreement promp.

#### Updating from a older version

Upgrading from a older version? Run this to make sure the schema is up to date.

    python manage.py upgrade -d=atomicpress/migrations/

### Prefill db with initial data

Adds initial data to the database, perfect when you want to try out AtomicPress.

    python manage.py prefill fill


### Server

#### Runserver

Creates a lightweight http server running the web application.

    python manage.py runserver

**Options**

    -a (admin) Activate the admin area (do not do this in a production anvironment)
    -t (toolbar) Show debug toolbar.
    -d (debug) Show debug messages.

Note: Although untested, it is possible to run AtomicPress as a standard wsgi application.


### Import

AtomicPress uses [wpparser](https://github.com/marteinn/wpparser/) to import data from wordpress export files. Just specify the path to your database export and you are ready to go.

    python manage.py importer import_blog -f=./data/blog.wordpress.2014-09-25.xml

**Options**

    -f (file) Path to wordpress export file.

### Export

Create a static package of you blog, that are ready to be deployed.

    python manage.py exporter export

### Sync

#### S3

Send the exported static files to a AWS S3 bucket.

    python manage.py s3 sync

#### FTP

Send the files to your ftp account.

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
