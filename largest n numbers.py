limit=int(input("enter the limit"))
num=int(input("enter the number"))
big=num
small=num
while limit>1:
    num=int(input("enter the number"))
    if num>big:
        big=num
    elif num<small:
        small=num

    limit=limit-1
print(f"enter the big",big)
print(f"enter the small",small)
