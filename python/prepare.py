""" -------------------------------------------------
https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
""" -------------------------------------------------
x = 5 #input("Enter 'x' co-ordinates: ")
y = 6 #input("Enter 'y' co-ordinates: ")

match (x, y):
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
"""
""" -------------------------------------------------
pt = Point(3,4)
where_is(Point)
"""
""" -------------------------------------------------
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
"""
""" -------------------------------------------------
import platform
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
"""
""" -------------------------------------------------
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
"""
""" -------------------------------------------------
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
"""
""" -------------------------------------------------
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
"""
""" -------------------------------------------------
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
"""
""" -------------------------------------------------
Write a Python program to display the first and last colors from the following list.

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))
"""
""" -------------------------------------------------
Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
"""
""" -------------------------------------------------
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5

Python int(x, base=10):

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""
""" -------------------------------------------------
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

Sample function: abs()

Python Docstring:

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.

print(abs.__doc__)
"""
""" -------------------------------------------------
Write a Python program to print the calendar of a given month and year.

Note: Use 'calendar' module.

Python calendar.month(theyear, themonth, w=0, l=0):

The function returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

'l' specifies the number of lines that each week will use. 

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

"""
""" -------------------------------------------------

Python String Formatting Best Practices



#1 “Old Style” String Formatting (% Operator)

>>> errno = 50159747054
>>> name = 'Bob'
>>> 'Hello, %s' % name
"Hello, Bob"
>>> '%x' % errno
'badc0ffee'
>>> 'Hey %s, there is a 0x%x error!' % (name, errno)
'Hey Bob, there is a 0xbadc0ffee error!'
>>> 'Hey %(name)s, there is a 0x%(errno)x error!' % {
...     "name": name, "errno": errno }
'Hey Bob, there is a 0xbadc0ffee error!'



#2 “New Style” String Formatting (str.format)

>>> 'Hello, {}'.format(name)
'Hello, Bob'
>>> 'Hey {name}, there is a 0x{errno:x} error!'.format(
...     name=name, errno=errno)
'Hey Bob, there is a 0xbadc0ffee error!'



#3 String Interpolation / f-Strings (Python 3.6+)

>>> f'Hello, {name}!'
'Hello, Bob!'
>>> a = 5
>>> b = 10
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
'Five plus ten is 15 and not 30.'
>>> def greet(name, question):
...     return f"Hello, {name}! How's it {question}?"
...
>>> greet('Bob', 'going')
"Hello, Bob! How's it going?"
>>> f"Hey {name}, there's a {errno:#x} error!"
"Hey Bob, there's a 0xbadc0ffee error!"



#4 Template Strings (Standard Library)

>>> from string import Template
>>> t = Template('Hey, $name!')
>>> t.substitute(name=name)
'Hey, Bob!'

>>> templ_string = 'Hey $name, there is a $error error!'
>>> Template(templ_string).substitute(
...     name=name, error=hex(errno))
'Hey Bob, there is a 0xbadc0ffee error!'

That means, if a malicious user can supply a format string, they can potentially leak secret keys and other sensitive information! Here’s a simple proof of concept of how this attack might be used against your code:

>>> user_input = '${error.__init__.__globals__[SECRET]}'
>>> Template(user_input).substitute(error=err)
ValueError:
"Invalid placeholder in string: line 1, col 1"


Python String Formatting Rule of Thumb: If your format strings are user-supplied, use Template Strings (#4) to avoid security issues. Otherwise, use Literal String Interpolation/f-Strings (#3) if you’re on Python 3.6+, and “New Style” str.format (#2) if you’re not.

"""
""" -------------------------------------------------


Write a Python program to calculate number of days between two dates.

Python datetime.date(year, month, day) :

The function returns date object with same year, month and day. All arguments are required. Arguments may be integers, in the following ranges:

    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= number of days in the given month and year

If an argument outside those ranges is given, ValueError is raised.

    Note: The smallest year number allowed in a date or datetime object. MINYEAR is 1.
    The largest year number allowed in a date or datetime object. MAXYEAR is 9999.

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

"""
""" -------------------------------------------------
Write a Python program to create a histogram from a given list of integers.

def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])

"""
""" -------------------------------------------------
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b).

def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

"""
""" -------------------------------------------------
Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))
"""
""" -------------------------------------------------
Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

"""
""" -------------------------------------------------
Write a Python program to check whether a file exists.

import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))


import os.path
print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))

my_file = open('main.py')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")

"""
""" -------------------------------------------------
 Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)


"""
""" -------------------------------------------------
 Write a Python program to get OS name, platform and release information.

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())

"""
""" -------------------------------------------------
 Write a Python program to locate Python site-packages.

site.getsitepackages(): Return a list containing all global site-packages directories.

import site; 
print(site.getsitepackages())


>>> print(site.getsitepackages())
['/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages',
 '/Applications/Xcode.app/Contents/Developer/AppleInternal/Library/Python/3.8/site-packages',
 '/Library/Python/3.8/site-packages',
 '/AppleInternal/Library/Python/3.8/site-packages',
 '/AppleInternal/Tests/Python/3.8'
]
>>> 


"""
""" -------------------------------------------------
 Write a Python program to call an external command.

from subprocess import call
call(["ls", "-l"])

import os
print(os.system('ls -l'))

"""
""" -------------------------------------------------

 Write a Python program to find out the number of CPUs using.

import multiprocessing
print(multiprocessing.cpu_count())

import psutil
print(psutil.cpu_count())

"""
""" -------------------------------------------------

 Write a python program to get the path and name of the file that is currently executing.

import os
print("Current File Name : ",os.path.realpath(__file__))

"""
""" -------------------------------------------------

48. Write a Python program to parse a string to Float or Integer.


n = "246.2458"
print(float(n))
print(int(float(n)))

def test(s):
   try:
       return int(s)
   except ValueError:
       return float(s)
print(test('12'))
print(test('233.12'))

"""
""" -------------------------------------------------
https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
""" -------------------------------------------------

Membership test operations

x in y

any(x is e or x == e for e in y) 


"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
""" -------------------------------------------------

"""
