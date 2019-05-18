 print("Hello, World!)
  File "<stdin>", line 1
    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal


>>> print("Hello", World!)
  File "<stdin>", line 1
    print("Hello", World!)
                        ^
SyntaxError: invalid syntax


>>> print("Hello", World)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'World' is not defined


>>> print("Hello", World)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'World' is not defined


>>> x = {}
>>> x["news"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'news'



>>> x = {"news":"this is news"}
>>> x["news"]
'this is news'
>>> x["news2"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'news2'


>>> [1,2,3,4,5,6]
[1, 2, 3, 4, 5, 6]
>>> list1 = [1,2,3,4,5,6]
>>> list1[5] # VALID INDEX NO ERRORS
6
>>> list1[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range


>>> sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum expected at least 1 arguments, got 0


>>> sum("news")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'