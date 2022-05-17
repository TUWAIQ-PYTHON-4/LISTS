
list_num = [2, 4, 8, 10, 15]

#sum all the items in the list
print(sum(list_num))

#the largest number from the list.
print(max(list_num))

# an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
odd_nums= []
def odd_num(num1,num2):
    if num1 % 2 == 0:
        num1 = num1 + 1
    for i in range(num1, num2, 125):
        global odd_nums
        odd_nums.append(i)
    return odd_nums
print(odd_num(1200,2000))

# slicing to get the list from frist to 5 element
new_list = odd_nums[0:5]
print(new_list)



