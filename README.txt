
Creating the python venv
========================


Install system libraries
------------------------

If you're on a mac, do:
  make mac

If you're on ubuntu, do:
  make ubuntu


Build the python virtualenv
---------------------------
To build the virtualenv, do:
  make venv


Create the database  for the crawler
====================================

Connect to the database using the psotgres client tool and create the database.

To create a database named "general", you would do this:

    [don@don-ThinkPad-T420s] 1% psql -h postgres.scrapy.quixey.com -U scrapy
    Password for user scrapy:
    psql (9.5.4)
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)

    scrapy=> create database general;
    CREATE DATABASE
    scrapy=>
