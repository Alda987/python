def is_right_triangle():
    s1=[]

    a=int(input("enter a number"))
    s1.append(a)

    b=int(input("enter a number"))
    s1.append(b)

    c=int(input("enter a number"))
    s1.append(c)
    s1.sort()


    if s1[2]**2==s1[0]**2+s1[1]**2:
        print("the triangle is a valid")
    else :
        print("the triangle is not valid")
is_right_triangle()
