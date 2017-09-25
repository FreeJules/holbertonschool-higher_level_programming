## Python Hello World

### Zen
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Read

- Read the first three chapters of [The Python tutorial](https://docs.python.org/3.4/tutorial/index.html): [Whetting Your Appetite](https://docs.python.org/3.4/tutorial/appetite.html), [Using the Python Interpreter](https://docs.python.org/3.4/tutorial/interpreter.html) and [An Informal Introduction to Python](https://docs.python.org/3.4/tutorial/introduction.html). For this last chapter (An Informal Introduction to Python), read until 3.1.2. Strings included (you do not have to read '3.1.3 Lists').

- Watch: [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt).

- Python's got style! [PEP 8 -- Style Guide for Python Code](PEP 8 -- Style Guide for Python Code).

##### TL;DR;

* install it: ```sudo apt-get install python3-pep8``` (version 1.7)
  * alternative install using pip3 (Python3 version of pip): [Install](https://pep8.readthedocs.io/en/release-1.7.x/intro.html#installation)
If /usr/bin/pep8 doesn’t exist, pep8 is located here /usr/local/lib/python3.4/dist-packages/pep8.py or /usr/lib/python3.4/dist-packages/pep8.py (cp /usr/local/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8 or cp /usr/lib/python3.4/dist-packages/pep8.py /usr/bin/pep8 && chmod u+x /usr/bin/pep8)
use it: pep8 file.py
... and of course, last but not least: man python3

### What you should learn from this project

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Who created Python
- Who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Holberton Python coding style and how to check your code with PEP 8

### Requirements for Python scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc

### Requirements for Shell scripts

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 14.04 LTS
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable
