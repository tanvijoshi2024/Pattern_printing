n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:                      #for first column
            print('*', end=" ")
        elif i==n:                        #for last row
            print('*', end=" ")
        elif j==i:                      # to print * on the same line
            print('*', end=" ")
        else:                         #print blank spaces in the triangle
            print(" ",end=" ")
    print()
            