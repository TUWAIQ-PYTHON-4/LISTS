# Q1: Write a Python program to sum all the items in the list.
my_listQ1 = [1,2,4,8,16,32]
print(sum(my_listQ1))
    
# Q2: Write a Python program to get the largest number from the list.
my_listQ2 = [1,2,4,8,16,32]
print(max(my_listQ2))

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
my_listQ3=[]
for n in range (1200,2000+1, 125):
    if(n%2 !=0):
        my_listQ3.append(n)
        
    else:
        continue    
print(my_listQ3)    


# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
my_listQ4 = [1,2,4,8,16,32]
new_list =my_listQ4[0:5]
print(new_list)

