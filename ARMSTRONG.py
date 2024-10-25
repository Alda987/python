'''AUTHOR: ALDA TREESA JOSY
DATE:25/10/2024
DESCRIPTION:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit
'''
NUM1=int(input("ENTER A NUMBER"))
sum_of_digits = 0
while(NUM1>0):
    R=NUM1%10
    sum_of_digits=sum_of_digits+R**3
    NUM1=NUM1//10


print("sum of the given digits",sum_of_digits)
