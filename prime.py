a=int(input("enter"))
i=2
while i<=a//2:
    if a%2==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime")
