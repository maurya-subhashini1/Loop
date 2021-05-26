no_rows=int(input("enter the number of rows:"))
for row in range(1, no_rows+1):
    for colum in range(1, row+1):
        print("*",end=" ")
    print()
for row in range(no_rows-1,0,-1):
    for column in range(1,row+1) :
        print("*",end=" ") 
    print() 