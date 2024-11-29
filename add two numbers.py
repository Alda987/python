def add(num1,num2):

    if num2==0:
        return num1
    else:
        return add(num1+1,num2-1)
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))

print('sum',add(num1,num2))