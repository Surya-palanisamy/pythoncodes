'''
l = ["apple", "orange", "kiwi", "grape"]
print(l)
print(l[0])
print(len(l))
print(type(l))
l[0] = "Banana"
print(l)
print(l[0])


a = eval(input("Enter the 1st number : "))
b = eval(input("Enter the 2nd number : "))
c = eval(input("Enter the 3rd number : "))
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("Sum of a,b,c = ", a+b+c)


a = eval(input("Enter any number : "))
if (a > 0):
    print(a, "is a positive number")
elif (a == 0):
    print("The give number is Zero")
else:
    print(a, "is a negative number")


i = 1
while(i < 11):
    print(i, end = ' ')
    i += 1


a = eval(input("Enter any number : "))
if (a % 2 ==  0):
    print(a, "is an even number")
else:
    print(a, "is an odd number")


a = input("Enter an input : ")
if (a.isalpha()):
    print(a, "is an alphabet")
elif (a.isdigit()):
    print(a, "is a number")
elif (a.isspace()):
    print("The given input is a White space")
else:
    print(a, "is a special character")


l = [1,3,5,7]
if 5 in l:
    print("The element 5 is present in the list")
else:
    print("The element 5 is not present in the list")


l = [10,15,20,25,30]
for i in l:
    if i % 2 == 0:
        print(i, end = " ")


import sys
print(sys.version)


l = [3,1,7,5]
a = sorted(l)
l.sort()
print(a)

import calendar
year = int(input("Enter the year : "))
print(calendar.calendar(year))


year = int(input("Enter the year : "))
if ((year % 4 == 0 and year % 100 != 0)or(year % 400 == 0)):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")



import math
r = eval(input("Enter the radius of the circle : "))
a = math.pi * (r ** 2)
print("The area of the circle is ", a)


a = input("Enter the character : ")
b = eval(input("Enter the number : "))
print("The equivalent ASCII value of the character is ",ord(a))
print("The equivalent ASCII value of the character is ",chr(b))


a = eval(input("Enter the Number : "))
print(bin(a))


d = int(input("Enter a number from 1 to 7: "))
if d == 1:
    print(d, "st day is Sunday")
elif d == 2:
    print(d, "nd day is Monday")
elif d == 3:
    print(d, "rd day is Tuesday")
elif d == 4:
    print(d, "th day is Wednesday")
elif d == 5:
    print(d, "th day is Thursday")
elif d == 6:
    print(d, "th day is Friday")
elif d == 7:
    print(d, "th day is Saturday")
'''
