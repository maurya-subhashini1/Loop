i=int(input("inter the the number"))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse number is:",rev//1*10)

    