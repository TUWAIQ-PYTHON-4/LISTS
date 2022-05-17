# Create a new list containing several different integers .
my_list=[11,9,13,50,33,44,20,10]
# Q1: Write a Python program to sum all the items in the list.
def sum_of_list(user_list):
    sum=0
    for element in user_list:
        sum+= element
    print("the sum is: ", sum)

# calling the function
sum_of_list(my_list)


# Q2: Write a Python program to get the largest number from the list.
def largest_num(user_list):
    largest_number=max(user_list)
    print("the largest number is: ",largest_number)
# calling the function
largest_num(my_list)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
elements_range_list=range(1200,2000,125)
odd_number_list=[num for num in elements_range_list if not(num%2==0)]
print(odd_number_list)
# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list= my_list[:5]
print(new_list)
