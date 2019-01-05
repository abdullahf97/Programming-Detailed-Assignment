print('Practice Problem 3.17')
a = eval('2*3+1')
print(a)

#b = eval('hello')
#print(b)
#This will give an error because hello in not defined
print("b = eval('hello') will give an error.")
"""Traceback (most recent call last):
  File "C:/Programming Assignment/Practice Problem 3.17.py", line 5, in <module>
    b = eval('hello')
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined"""
c = eval("'hello' + ' ' + 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

#e = eval('x = 5')
#print(e)
#it will give error due to syntax error
print("e = eval('x = 5') will give an error.")
"""Traceback (most recent call last):
  File "C:/Programming Assignment/Practice Problem 3.17.py", line 20, in <module>
    e = eval('x = 5')
  File "<string>", line 1
    x = 5
      ^
SyntaxError: invalid syntax"""
