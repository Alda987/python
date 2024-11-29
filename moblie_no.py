def mobile():
    phone_number=int(input("enter the phone number:"))
    a=str(phone_number)
    if len(a)==10 and a[0] in '789':
        print("The given number is a valid phone number")
    else:
        print("The given number is not a valid phone number")
mobile()