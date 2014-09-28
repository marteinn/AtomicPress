# AtomicPress

AtomicPress is a static blog generator modeled after WordPress data models.

## Features

- Markdown rendering
- Theme support
- Import from Wordpress


## Getting started

To install AtomicPress you'll need python 2.7 and pip.


## Commands

### Updating from a older version

    python manage.py upgrade -d=atomicpress/migrations/


### Importing

AtomicPress uses wpparser to import data from wordpress export files.

    python manage.py importer import_blog -f=./data/blog.wordpress.2014-09-25.xml


### Exporting

    python manage.py exporter export


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

AtomicPress is released under the [MIT License](http://www.opensource.org/licenses/MIT).
