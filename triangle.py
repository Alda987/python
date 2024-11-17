'''Author: ALDA TREESA JOSY 
Date:17/01/2024
Description:If/Else Condition Task: Use nested if/else statements to determine the type of triangle based on side lengths. Problem Description:You are given three integers representing the lengths of the sides of a triangle. You need to determine the type of triangle:'''
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a + b > c and b + c > a and c + a > b:
    
    if a == b == c:
        print("The triangle is Equilateral.")
    else:
        
        if a == b or b == c or c == a:
            print("The triangle is Isosceles.")
        else:
            
            print("The triangle is Scalene.")
else:
    print("The given sides do not form a triangle.")