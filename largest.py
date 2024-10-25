'''
AUTHOR: ALDA TREESA JOSY
DATE:25/10/2024
DESCRIPTION:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit
'''

number1=int(input("enter a number"))
number2=int(input("enter a number"))
number3=int(input("enter a number"))
if(number1>number2) & (number1>number3):
 print("The largest number is",number1)
elif(number2>number3) & (number2>number3):
 print("the largest is",number2)
else:
 print("the largest is",number3)
