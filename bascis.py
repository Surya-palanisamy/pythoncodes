

a= ["apple","orange","mango",123]
print(a)
print(a[0])
print(len(a))
print(type(a))
a[0]="banana"
print(a)


a= int(input("enter the num : "))
b = int(input("enter the num : "))
c  = int(input("enter the num : "))
print("the sum ber is ",a+b+c)
"""
"""
a = int(input("enter tne num : "))
if a == 0:
   print("zero")
elif a>0:
  print("positve")
else:
  print("negative")
"""
"""
a= int(input("enter the num : "))
if a%2 ==0:
    print("even")
else :
    print("Odd")
"""
"""
i = 0:
    while i <11:
        print(i,end = "  ")
        i+=1
"""
"""
a = input("enter some thing : ")
if   a.isalpha():
        print( "alphabet")
elif a.isdigit():
        print("number")
elif a.isspace() :
        print("White space")
else :
    print("wrong input")
"""
"""
a = [1,2,3,4,5,6]
if 5 in a:
    print("the given numer is  in list")
else:
    print("not in list")
"""



"""

a = [10,15,20,25,30]
for i in a:
    if i%2==0:
        print(i,end = " " )


"""
"""
import sys
print(sys.version)
"""
"""
a = [1,3,24,34,80,1,2]
b = sorted(a)
print(b)
a.sort()
print(a)
"""
f=255
for i in range(f):
    print(chr(i))



































