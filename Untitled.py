Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> word = "Welcome"
>>> import re
>>> print "Valid" if re.match("^[a-zA-Z0-9_]*$", word) else "Invalid"
SyntaxError: invalid syntax
>>> print ("Valid") if re.match("^[a-zA-Z0-9_]*$", word) else "Invalid"
Valid
>>> word="213@#$"
>>> print ("Valid") if re.match("^[a-zA-Z0-9_]*$", word) else "Invalid"
'Invalid'
>>> word="asf@asf24"
>>> print ("Valid") if re.match("^[a-zA-Z0-9_]*$", word) else "Invalid"
'Invalid'
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@]*$", word) else "Invalid"
Valid
>>> print ("Valid") if re.match("^[a-zA-Z0-9_.]*$", word) else "Invalid"
'Invalid'
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@.]*$", word) else "Invalid"
Valid
>>> 
============== RESTART: /Users/mariacharles/Documents/email.py ==============
Enter the number of testcases2
Enter your email: 
charles@gmail.com
Traceback (most recent call last):
  File "/Users/mariacharles/Documents/email.py", line 5, in <module>
    if re.match("^[a-zA-Z0-9_@.]*$", s):
NameError: name 're' is not defined
>>> 
============== RESTART: /Users/mariacharles/Documents/email.py ==============
Enter the number of testcases2
Enter your email: 
afgas@.com
Your name is :
afgas
Enter your email: 
sdfus
Your name is :
sdfu
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@.]*$", word) else "Invalid"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print ("Valid") if re.match("^[a-zA-Z0-9_@.]*$", word) else "Invalid"
NameError: name 'word' is not defined
>>> word="charles"
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@.]*$", word) else "Invalid"
Valid
>>> print ("Valid") if re.match("^[a-zA-Z0-9_][@][.]*$", word) else "Invalid"
'Invalid'
>>> word="charles@."
>>> print ("Valid") if re.match("^[a-zA-Z0-9_][@][.]*$", word) else "Invalid"
'Invalid'
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@.]$", word) else "Invalid"
'Invalid'
>>> word
'charles@.'
>>> print ("Valid") if re.match("^[a-zA-Z0-9_]*$", word) else "Invalid"
'Invalid'
>>> print ("Valid") if re.match("^[a-zA-Z0-9_@.]*$", word) else "Invalid"
