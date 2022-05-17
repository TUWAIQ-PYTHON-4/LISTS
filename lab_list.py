## Create a new list containing several different integers . 
### Q1: Write a Python program to sum all the items in the list.

numbers_list=[1,2,3,4,5,6,7,8]
sum:int = sum(numbers_list)
print('the sum of the number is the list = ', sum)

### Q2: Write a Python program to get the largest number from the list.

max_num: int = max(numbers_list)
print('the largest number = ', max_num)

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125,
# using list comprehension.

odd_list = [num for num in range(1200,2000 + 1, 125) if num % 2 == 1]
print(odd_list)



### Q4: use list slicing to get a new list from the previous list starting from the start to
#  the 5th element in the list.

new_list=numbers_list[:5]
print(new_list)




