i=int(input("enter to check for armstrong number")) 
sum=0
a=i
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if a==sum:
   print(sum,"armstrong")
else:
   print(sum,"not amstrong")