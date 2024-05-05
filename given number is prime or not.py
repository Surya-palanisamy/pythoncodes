i=int(input("enter the 1 number: "))

for j in range(2,i):
        if i%j==0:
            
            print("not prime")
            break
else:
    print("prime number")
