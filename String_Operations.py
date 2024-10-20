'''
Author: ALDA TREESA JOSY 
Date:19/10/2024
Description: Python program that performs the following tasks:

Create two separate strings:

The first string should contain your first name.
The second string should contain your last name.
Concatenate the two strings with a space in between and store the result in a new variable.

Print the concatenated string.

From the concatenated string:

Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

conc = str1 + " " + str2
print(conc)
h = len(conc)
print("length",h)
last_part=conc[5:9]
print("last part of the string",last_part)