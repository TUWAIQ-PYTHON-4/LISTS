#Write a Python program to sum all the items in the list .
list = [1,2,3,4,5,6,7]
print(list)
SumItems = sum(list)
print(SumItems)
#Write a Python program to get the largest number from the list.
LargNumber = max(list)
print(LargNumber)
#Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
ListOdd = [item for item in range(1200 , 2000,125) if item%2 != 0 ]
print(ListOdd)
#use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
SliceList = slice(0 , 5)
print(ListOdd[SliceList])