i=1
a=int(input("enter"))
while i<=5:
    b=int(input("enter"))
    i=i+1
    if b==a:
        print("you guess right")
        break
else:
    print("you loss 5 chnace")