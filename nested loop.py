

print("INCREASING TRIANGLE")
for i in range(6):
    for j in range(i,i+1):
        print(j*'*')
print("DECREASING TRIANGLE")
for i in range(5,0,-1):
    for j in range(i,i+1):
        print(j*'*')
print("HILL")
row=5
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
print("reverse the hill pattern")
row=5
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()




        