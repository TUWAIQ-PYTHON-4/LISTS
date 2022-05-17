
#Q1: Write a Python program to sum all the items in the list.
from distutils.dep_util import newer_pairwise


new_list=[1,2,3]
sum=0
for n in new_list:
    sum=sum+n
print("answer Q1:",sum)
#Q2: Write a Python program to get the largest number from the list.
new_list1=[1,5,3,9,8]
large=0
for n in new_list1:
    if large<=n:
        large=n
print("answer Q2:",large)
#Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.
odd_list=[]
print("answer Q3:")
for range_number in range(1200 ,2000,125):
    mod=range_number%2
    if mod>0:
        print(range_number)

#Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
list_slicing=[1,2,3,4,5,6,7]
new_list_slicing=list_slicing[:5]
print("answer Q4:",new_list_slicing)
