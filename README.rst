cloudinn
=========

Pre-interview technical assessment task!

.. image:: https://img.shields.io/badge/built%20with-Django%20-ff69b4.svg
     :target: https://www.djangoproject.com/
     :alt: Built with Django
.. image:: https://img.shields.io/badge/built%20with-CELERY-000000.svg
     :target: http://www.celeryproject.org/
     :alt: CELERY  


:License: MIT

Project Description
^^^^^^^^^^^^^^^^^^^^^

Using Python or Golang write a command line program which takes an Age of Empires || unit
name as a user input and search for information about this unit then render this unit’s data to
the user.
Use this API endpoint to retrieve the age of empires || units data
https://age-of-empires-2-api.herokuapp.com/docs/
All the data retrieved from the API endpoint should be stored locally in a database of your
choosing to minimize the amount of requests made to the API.
The code should be delivered on a public github repository. Undocumented code will be
disregarded. Along with the code you must include a guide on how to setup and use the
application.


Project Setup
^^^^^^^^^^^^^

To run the project on local machine you have to setup python3 and postgresql first::

    $ sudo -u postgres psql
    $ postgres=# create database mydb;;
    $ postgres=# create user myuser with encrypted password 'mypass';
    $ postgres=# grant all privileges on database mydb to myuser;
    $ postgres=# \q
    $ sudo apt-get install redis-server
    $ sudo systemctl enable redis-server.service
    $ git clone https://github.com/AbdelrahmanRabiee/cloudinn.git
    $ mkdir venv/
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ nano cloudinn/.env
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

    open new terminal window and activate venv then start **CELERY** 
        $ celery -A cloudinn worker -l info

.env structure
^^^^^^^^^^^^^

    DB_NAME='mydb'
    DB_USER='myuser'
    DB_PASSWORD='mypass'
    SECRET_KEY=herhherhehkerhuifreyy4y54y33gg33gy3y3
    DEBUG=True
    ALLOWED_HOSTS=0.0.0.0,127.0.0.1
    CELERY_BROKER_URL='redis://localhost:6379'
    CELERY_RESULT_BACKEND='redis://localhost:6379' 


Project Testing
^^^^^^^^^^^^^^^

     To run test cases do below commands::

          $ python manage.py test empires.tests.test_api.TestUnitAPI      