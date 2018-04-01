DUCKTY.PY
============

Yet another duck-typing library for python.

It generates `isinstance` and `issubclass` compiant type object dinamicaly.

Example
--------

```py
from ducktypy import Duck

class Swan(object):
    def walk(self):
        return 'slap slap'
    
    def quack(self):
        return 'quaaaacck'

    def fly(self):
        return True

swan = Swan()
if isinstance(swan, Duck.has('walk', 'quack')):
    print('It must be a duck.')

class Python(object):
    def walk(self):
        return 'stupidly'

    def spam(self):
        return ' '.join(['spam'] * 100)
    
python = Python()
if not isinstance(python, Duck.has('walk', 'quack')):
    print('It must NOT be a duck.')

python.quack = 'quack!'

if isinstance(python, Duck.has('walk', 'quack')):
    print('Now, it must be a duck.')

```

What is returned from `Duck.has` is a class object.
This "Duck"-ed class deals other instances/classes as one of (instance of) subclass,
when the other one has all attributes which "Duck"-ed class `has` . 

TODO
-----

- make it mypy-compat
- write more tests
- make it `pip install`-able
    - but I am not so hurry for it...
    - this is toy project now, and changing for mypy-compat can introduce breaking interface changes.
- decide if support python 2.7
