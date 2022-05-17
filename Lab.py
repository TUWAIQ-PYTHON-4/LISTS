import math
sum=0
listNumber=[1,2,9,5,80]
#sum all the items in the list.
for i in listNumber:
    sum+=i
print("summition all number in [1,2,9,5,80] :",sum)
# largest number from the list.
print("The largest number in [1,2,9,5,80] is : " ,max(listNumber))
# odd numbers list from the elements of a range from 1200 to 2000 with steps of 125
oddNumber=[*range(1200,2000,125)]
oddNumber=[i for i in oddNumber if i%2!=0]
print("odd Number from 1200 to 2000 with 125 step : " ,oddNumber)
# slicing to get a new list from the previous list starting from the start to the 5th
print("The List after slicing is :",oddNumber[:5])

