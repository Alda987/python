def sum(l1):
    s=0
    for i in l1:
        s=s+i
    print(s)
l1=[]
n=int(input("enter the number of elements"))
for i in range(n):
    n1=int(input("enter the numbers"))
    l1.append(n1)
sum(l1)

