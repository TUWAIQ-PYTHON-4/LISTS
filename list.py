'''
## Create a new list containing several different integers . 
### Q1: Write a Python program to sum all the items in the list.
### Q2: Write a Python program to get the largest number from the list.
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''
lst=[3,5,7,9,4,6,8,4,8,9]
print(sum(lst))
print(max(lst))


def odd_numbers(num1:int,num2:int)->int:
    return [num for num in range(num1, num2, 125) if num % 2 !=0]

print(odd_numbers(1200,2000))

newlist=(lst[5:])
print(newlist)