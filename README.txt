
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


Interacting with the database    Create the database  for the crawler
=============================


Connect to the database
-----------------------
Connect to the database using the postgres client tool "psql" and create the database.

To create a database named "general", you would do this:

    [don@don-ThinkPad-T420s] 1% psql -h postgres.scrapy.quixey.com -U scrapy
    Password for user scrapy:
    psql (9.5.4)
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    scrapy=>

Create the database
-------------------

    scrapy=> create database general;

    CREATE DATABASE
    scrapy=>


List databases
--------------

    scrapy=> \l
                                       List of databases
        Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
    -------------+----------+----------+-------------+-------------+-----------------------
     appannie    | scrapy   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     bikeaholics | scrapy   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     general     | scrapy   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     scrapy      | scrapy   | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                 |          |          |             |             | postgres=CTc/postgres
     template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                 |          |          |             |             | postgres=CTc/postgres
    (7 rows)

    scrapy=>


Connect to a database
---------------------

    scrapy=> \c general
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    You are now connected to database "general" as user "scrapy".
    general=>


Show tables in the current database
-----------------------------------

    general=> \d
                 List of relations
     Schema |     Name     |   Type   | Owner
    --------+--------------+----------+--------
     public | metadata     | table    | scrapy
     public | queue        | table    | scrapy
     public | queue_id_seq | sequence | scrapy
     public | states       | table    | scrapy
    (4 rows)

    general=>


Show schema for a table
-----------------------

    general=> \d metadata
                    Table "public.metadata"
       Column    |            Type             | Modifiers
    -------------+-----------------------------+-----------
     fingerprint | character varying(40)       | not null
     url         | character varying(1024)     | not null
     depth       | integer                     | not null
     created_at  | timestamp without time zone | not null
     fetched_at  | timestamp without time zone |
     status_code | character varying(20)       |
     score       | double precision            |
     error       | character varying(128)      |
     meta        | bytea                       |
     headers     | bytea                       |
     cookies     | bytea                       |
     method      | character varying(6)        |
    Indexes:
        "metadata_pkey" PRIMARY KEY, btree (fingerprint)

    general=>
