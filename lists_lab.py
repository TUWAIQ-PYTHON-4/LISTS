## Create a new list containing several different integers . 
list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_int)

### Q1: Write a Python program to sum all the items in the list.
list_int_sum = sum(list_int)
print(list_int_sum)

### Q2: Write a Python program to get the largest number from the list.
max = max(list_int)
print(max)

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
list_of_odds = [i for i in range(1200, 2000+1, 125 ) if i % 2 != 0]
print(list_of_odds) 

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list_of_odda = list_of_odds[:5]
print(new_list_of_odda)

