#python basic exercises 
'''
print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t" \
"Up above the world so high,\n\t\tLike a diamond in the sky." \
"\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
'''

#import sys 
#print(sys.version)


#
# import datetime
#now = datetime.datetime.now()
#print(now.strftime("%d/%m/%Y %H:%M:%S"))
'''
from math import pi

r =float(input("Enter the radius:"))

area= pi*r**2

print("The area of the cirle is "+str(area))
'''
'''
first_name =input("Enter first name ")
last_name=input("Enter last name ")
print (last_name +" "+first_name)
'''
'''
values =input("Enter some numbers")
List= values.split(",")
print (List)
tuple =tuple(List)
print(tuple)
'''
'''
filename= input("Enter the filename:")
list=filename.split(".")
print(list[-1])

'''

#color_list=["Red","Green","White","Black"]
#print("%s %s" %(color_list[0],color_list[-1]))

#exam_st_date=(11,12,2014)
#print("The examination will start from %i %i %i" % exam_st_date)

'''
a=int(input(("Enter the integer ")))
n1 = int(("%s" %a))
n2=int(("%s%s" %(a,a)))
n3=int(("%s%s%s" %(a,a,a)))

print(n1+n2+n3)

'''

'''
import calendar

x=int(input("Enter the year:"))
y=int(input("Enter month:"))

calendar= calendar.month(x,y)

print(calendar)

'''

'''
from datetime import date

f_date= date(2014, 7, 2)
print(f_date)

l_date=date(2015,7,11)

print(l_date)

delta=l_date-f_date

print(delta.days)
'''
'''
from math import pi

r=6
volume =4/3 * pi *r**3

print('The volume of the sphere is:',volume)
'''
'''
def difference(n):
    if n<=17:
        return 17-n
    else:
        return (n-17)*2

print(difference(22))
print(difference(14))
'''

'''
def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

'''
'''
def sum_three(a, b, c):
    
        return(a + b + c)*3
    return (a + b + c)

print(sum_three (1,2,3))
print(sum_three(1,1,1))
print(sum_three(1,1,3))
'''

'''

def string_add(string):

   if (string[:2]=="Is"):
      return string
   return  "Is"+string 

print(string_add("hello"))
print(string_add("Isman"))
print(string_add("IsIsman"))
'''

'''
n = int(input("enter any number"))

def is_odd_or_even(n):
    if(n % 2 == 0):
        print("This is even number:",n)
    else :
        print("This is odd number:",n)
    

is_odd_or_even(n)
'''


'''
numbers = [1,2,3,4,5,4,4,5,3,4,4,4,4,4,4,4,4,4,4]
i=0
for count in numbers:
    if(count == 4):
      i+=1
print(i)    

'''

'''
def copies_string(n, string):
    if(len(string) < 2):
        return string *n
    return string[:2] *n
print(copies_string(2,"st"))
print(copies_string(3,"hello"))


''' 

'''
vowel = 'aeiou'

def check_vowel(l):
    return l in vowel


print(check_vowel('b'))
print(check_vowel('a'))

'''

'''
list = [1, 5, 8, 3]
def checker(n):
        return n in list

print(checker(3))
print(checker(-1))
'''

'''
def histogram(items):
    for x in items:
        output = ''
        times = x
        
        while times > 0:
            output += '*'
            times = times - 1 
        print(output)

histogram([1,2,3,4,5,6,7,8,9])

'''
'''
def list_add(element):
    result = ''

    for x in element:
        result += str(x)
        
    return result

print(list_add([1,2,3,4,5]))

'''


'''
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

print(numbers)

for x in numbers:
    if x == 237:

        print(x)
        break
    elif x % 2 == 0:
        print(x)



'''

'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

result = color_list_1.difference(color_list_2)

print(result)

'''
'''

base = int(input("Enter the base "))
height = int(input("Enter the height "))

Area = base * height /2

print("Area of the triangle is ", Area)

'''


'''
def divisor(x, y):
    gdc = 1
    if x % y == 0:
        return y
    for k in range (int (y/2), 0, -1):
         if x % k == 0 and y % k ==0:
             gdc = k
             break
    return gdc

print(divisor(4,6))

'''

'''
def lcm (x, y):
    if x > y:
        z = x
    else :
        z = y
    while True:
        if z % x == 0 and z % y ==0:
            lcm =z
            break
        z += 1
    return lcm

print(lcm(4,6))

'''

'''

def sum_all(a, b, c):
    if a == b  or b == c or a == c: 
        sum = 0
    else :
        sum = a + b + c

    return sum

print(sum_all(4, 4, 4))

'''
'''
def sum_two (a, b):
    sum = a + b
    if sum in range(15, 20):
        return 20
    
    return sum


print(sum_two(1, 7))

'''

'''
def checker(a, b):
    if a == b or a + b == 5 or abs(a -b) ==5:
        return True
    return False  

print(checker(5,3))

'''

'''
def checker(a, b):
    if(isinstance(a, int) and isinstance(b, int)):
        return a +b
    else :
        return " Objects are not integers"


print(checker(1, '4'))
print(checker(2,3))
print(checker(2,2.2))
'''
'''
name = "Mukhammadjon"
age =27
address = "Pirenejska 20 /11"

print(f"My name is {name}")
print(f"I am a {age} years old")
print(f"I live in {address}")

'''

'''
def personal_detail():
    name, age = "Mukhammadjon", 27
    address = "Pirenejska Bemowo Warzsawa"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_detail()
'''
'''
def express_solver(x, y):
    return  (x + y) **2

print(express_solver(4,3))
'''

'''
def future_value(amt, i, y):
    future_val = amt * (1 + i/100)**y
    return round(future_val,2)

print(future_value(10000, 3.5, 7))
'''

'''
import math

p1 = [4, 0]

p2 = [6, 6]

distance = math.sqrt(((p1[0] - p2[0]) ** 2)+((p2[0] - p2[1]) **2))

'''

'''
import os.path

print(os.path.isfile("example.txt"))

print(os.path.isfile("learning.py"))

'''


'''
import struct

print(struct.calcsize("P") * 8)
'''
'''
import site

print(site.getsitepackages())
'''

'''
import os

print("Current File Name: ", os.path.realpath(__file__))
'''

'''
import multiprocessing

cpp_count = multiprocessing.cpu_count()

print(cpp_count)
'''

'''
n = "246.2458"

print(int(n))
print(float(n))

print(int(float(n)))

'''



'''
for i in range (0, 10):
    print('*', end='')
print("\n")

'''


'''
import cProfile

def sum():
    print(1 + 2)
cProfile.run('sum()')
'''
'''

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs)

eprint("abs", "efg", "xyz", sep= "--*")

'''
'''
import getpass

print(getpass.getuser())

'''
'''

import socket
local_hostname = socket.gethostname()

print(local_hostname)
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

first_ip = filtered_ips[:1]

print(first_ip[0])

'''


'''
import time 

def sum_of_n_numbers(n):
    start_time =  time.time()

    s = 0

    for i in range(1, n + 1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time

n = 5 

print("\nTime to sum of 1 to ", n, "and required time to calculate is ", sum_of_n_numbers(n))
'''

'''
def sum_n_numbers(n):
    s = 0
    for i in range(0, n + 1):
        s = s + i
    print("sum of first n numbers",s)

sum_n_numbers(5)
'''

'''
def convert_height(h):
    height = int(input("enter the heigt:"))

    centimeter = height * 100 

    print()
'''


'''
import math 

def triangle():
    a = int(input("enter the value "))
    b = int(input("Enter the value"))
    c = int(math.sqrt((a**2) + (b **2)))
    print("Right angled triangle", c)

triangle()

'''

'''
def convertor(feet):
    feet_inch = feet * 12
    feet_yard = feet_inch / 3
    feet_mile = feet_inch / 5280

    print("feet to inch ", feet_inch)
    print("feet to yards",feet_yard)
    print("feet to mile", feet_yard)

convertor(10)
'''

'''
days = int(input("Input days: ")) * 3600 *24

hours = int(input("Input hours: ")) * 3600

minutes = int(input("Input minutes: ")) * 60 

seconds = int(input("Input seconds:"))

time = days + hours + minutes + seconds

print("The amount of seconds:", time)
'''


'''
import os 

def absolute_path(path_fname):

    return os.path.abspath(path_fname)

print("Absolute file path: ", absolute_path("example.txt"))

'''

'''
import os.path, time

print("Last modified: %s" %time.ctime(os.path.getmtime("example.txt")))

print("Created: %s" %time.ctime(os.path.getctime("example.txt")))

'''
'''


time = float(input("Enter the seconds"))


day = time // (3600 * 24)

time = time % (3600 * 24)

hour = time // 3600

time  %= 3600

minutes = time // 60

time %= 60

seconds = time 

print("d:h:m:s -> %d:%d:%d:%d" % (day,hour,minutes,seconds))

'''


'''
weight = int(input("Enter your kg: "))

height = int(input("Enter the your height in meter:"))


mass_index = weight/( height ** 2)

print("Body mass index ",mass_index)

'''


'''
digit = int(input("Enter the number"))

x1 = digit // 100


x2 = digit % 10

sum = x1 + x2

print("Sum of the numbers", sum)

'''

'''
n1 = int(input("Enter number"))

n2 = int(input("Enter number"))

n3 = int(input("Enter number"))

a1 = min(n1,n2,n3)

a3 = max(n1,n2,n3)

a2 = (n1+n2+n3) - a1 - a3

print("Numbers in sorted order:", a1,a2,a3)

'''
'''
import glob
import os

files  = glob.glob("*.txt")

files.sort(key=os.path.getmtime)

print("\n".join(files))
'''


'''
import math

math_ls = dir(math)

print(math_ls)

'''


'''
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

word = input("Input the word to be hashed: ")

word = word.upper()

coded = word[0]


for a in word[1 : len(word)]:
    i = 65 - ord(a)
    coded = coded +str(soundex[i])
print()

print("The coded word is: " +coded)

print()

'''
'''
import sys

print("\nPython Copyright Information")

print(sys.copyright)

print()
'''


'''
import sys

print("This is the name/path of the script:"), sys.argv[0]

print("Number of arguments:", len(sys.argv))

print("Argument List:", str(sys.argv))

'''


'''
import sys

if sys.byteorder == "little":
    print("Little-endian platform.")
else :
    print("Big-endian platform")
'''


'''
import sys

import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))

print(textwrap.fill(module_name, width=70))

'''

'''
import sys 
str1 = "one"
str2 = "f"
str3 = "three"
x = 0
y = 112
z = 122.56

print("Size of ", str1, " = ", str(sys.getsizeof(str1)) + "bytes")

print("Size of ", str2, " = ", str(sys.getsizeof(str2)) + "bytes")
'''

'''
import sys

print()
print("recercion limit", sys.getrecursionlimit())
'''
'''
listofcolors = ["Red", "White","Black"]
colors = '-'.join(listofcolors)
print("resulst", colors)
'''

 
















