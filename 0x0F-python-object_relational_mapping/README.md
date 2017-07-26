## 0x0F. Python - Object-relational mapping

### Read

- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/en/latest/index.html) (please don't pay attention to _mysql)
- [MySQLdb tutorial](http://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy tutorial](http://docs.sqlalchemy.org/en/latest/orm/tutorial.html)

##### As references:

- [SQLAlchemy](http://docs.sqlalchemy.org/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient-python)

### What you should learn from this project

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

##### Install MySQLdb module
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```
##### Install SQLAlchemy module
```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.1.6'
```

### Requirements for Python scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- You are not allowed to use execute with sqlalchemy
