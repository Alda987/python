list1=[2,4,9,19,75]
list2=[3,9,5,7,23]
combined_list=list1+list2
print(combined_list)
number=[]
even_list=[]
odd_list=[]
for num in combined_list:
    if num % 2==0:
      even_list.append(num)

    else:
        odd_list.append(num)

even_list.sort()
odd_list.sort()
combined_list=even_list+odd_list
print(combined_list)