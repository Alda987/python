n=int(input("Enter How many Numbers"))
p=int(input("Enter First Number"))
for i in range(1,n):
    x=int(input("Enter Next Number"))
    if x>p:
        p=x
print(p,"Is Largest")
