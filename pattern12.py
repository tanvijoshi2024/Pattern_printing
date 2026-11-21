n=5
#top half of butterfly
for i in range(1,n+1):
    for j in range(i):                  # prints star to form the shape on left side 
        print("*",end=" ")
    for k in range(2*(n-i)):             #prints space to form the shape
        print(" ",end=" ")
    for l in range(i):                 #prints star to form the shape on right side
        print("*",end=" ")
    print()

#bottom half of butterfly
for i in range(n-1,0,-1):
    for j in range(i):                 # prints star to form the shape on left side
        print("*",end=" ")
    for k in range(2*(n-i)):              #prints space to form the shape
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")                #prints star to form the shape on right side
    print()
