'''
AUTHOR: ALDA TREESA JOSY
DATE:25/10/2024
DESCRIPTION:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit
'''
temp=float(input("enter a temperature"))
unit=input("Is this in celsius or fahrenheit?")
if unit=="C":
 fahrenheit=(9/5)*temp + 32
 print(temp,"celsius to fahrenheit",fahrenheit)
else:
 celsius=5/9*(temp-32)
 print(temp,"fahrenheit to celsius",celsius)



