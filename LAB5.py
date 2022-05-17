# Q1: Write a Python program to sum all the items in the list.
my_list = [1,2,4,8,16,32]
print(sum(my_list))
    
# Q2: Write a Python program to get the largest number from the list.
my_list = [1,2,4,8,16,32]
print(max(my_list))

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
for n in range (1200,2000+1, 125):
    if(n%2 !=0):
        my_list = [n]
        print(my_list)
    else:
        continue    

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
my_list = [1,2,4,8,16,32]
new_list =my_list[0:5]
print(new_list)

