for i in range(5):#for rows |
    for j in range(5):#for columns ---
        print(i, end =" ")
    print()
n=int(input("enter the number"))
for rows in range(n):#for rows |
    for col in range(n):
        print(rows,end ='')
    print()
n=int(input("Enter the number:"))
for row in range(n):
    for col in range(n):
        print((row +col)%2,end='')
    print()
n=int(input("Enter the size"))
for i in range(n):
    for j in range(i+1):
        print("*", end ='')
    print()
n=int(input("Enter size"))
for row in range(n):
    for col in range(n-row):
        print("*", end='')
    print()

n =int(input("enter the size"))
for row in range(n):
    for spc in range(n-row-1):
        print('',end =' ')
    for col in range(row+1):
        print("*", end=' ')
    print()
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*", end=' ')
        else:
            print('', end=' ')
    print()

        
    
    
                            
