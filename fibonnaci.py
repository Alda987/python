def fibonacci(n):

    a=0
    b=1
    print(a)
    print(b)
    for i in range(n-2):

        x=a+b
        print(x)
        a=b
        b=x


fibonacci(20)