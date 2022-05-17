

### Q1: Write a Python program to sum all the items in the list.

numbers= [11,20,5,8,4]
sum=sum(numbers)
print(sum)


### Q2: Write a Python program to get the largest number from the list.

max_number=numbers[0]

for max in range(len(numbers)):
    if numbers[max] > max_number:
        max_number = numbers[max]

print(max_number)


 ### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_numbers= []
for number in range(1200,2000,125):
    if number %2 != 0:
        odd_numbers.append(number)
    
print(odd_numbers)



### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

print(numbers[:5])