n= 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1:                      #check in first row
            print('*', end=" ")
        elif i==n:                     #check in last row
            print('*', end=" ")
        elif j==1:                      #check in first column
            print('*', end=" ")
        elif j==n:                     #check in last column
            print('*', end=" ")
        else:                            #print space
            print(" ", end=" ")
    print()
