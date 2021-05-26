i=int(input("enter the the number"))
a=0
x=i
while (i>0):
    a=(a*10)+i%10
    i=i//10
    if (x==0):
        print("pollindrom number")
    else:
        print("not pollidrom number")