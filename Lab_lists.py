# LISTS

## Create a new list containing several different integers . 
new_list = [1,2,3,4,5,6,6,7,8,9,10]
### Q1: Write a Python program to sum all the items in the list.
sum = sum(new_list)
### Q2: Write a Python program to get the largest number from the list.
max = max(new_list)
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_list = [x for x in range(1200,2000,125) if x %2 ]
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_odd_list = odd_list[:5]
