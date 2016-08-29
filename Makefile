# -*- Makefile -*-

venv:
	virtualenv venv
	./venv/bin/pip install cachetools frontera msgpack-python psycopg2 scrapy sqlalchemy kafka-python==0.9.5

clean:
	rm -f *~

distclean: clean
	rm -rf venv

mac:
	brew install postgresql

ubuntu:
	sudo apt-get install postgresql-server-dev-all
