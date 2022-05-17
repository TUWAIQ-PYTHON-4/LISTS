#Create a new list containing several different integers . from operator import ne
new_list = [1,2,3,4,5,6,7,8]

#Q1: Write a Python program to sum all the items in the list.
sum_list= sum(new_list)
print(sum_list)

#Q2: Write a Python program to get the largest number from the list.
largest_number = max(new_list)
print(largest_number)

#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_number = []
for elements in range(1200,2000,125):
    if (elements % 2 ) != 0:
         odd_number.append(elements)
    else:
        continue
print(odd_number)

#Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
another_list = new_list[:6]
print(another_list)
