def mul(num1,num2):
    if num2==1:
        return num1
    else:
        return num1 + mul(num1,num2-1)
num1=int(input("enter a number:"))
num2=int(input("enter a number"))
print(mul(num1,num2))