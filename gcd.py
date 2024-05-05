d1=int(input("Enter a number: "))
d2=int(input("Enter another number: "))
rem=d1%d2
while rem!=0 :
    d1=d2
    d2=rem
    rem=d1%d2
print ("The GCD of given numbers is: ",d2)
