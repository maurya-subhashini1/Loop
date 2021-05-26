num=int(input("enter the number:"))
a=0
i=1
while i<num:
    if(num%i)==0:
        a=a+i
    i=i+1
if a==num:
    print("is perfect number") 
else:
    print(num,"is not perfect number")     
        