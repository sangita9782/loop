i=1
a=int(input("enetr"))
while i<=5:
    b=int(input("enetr"))
    i=i+1
    if b<a:
        print("no enter by smaller")
    elif b>a:
        print("no enter by greater")
    elif b==a:
        print("wow your guess right")
    break
else:
    print("wrong guess")