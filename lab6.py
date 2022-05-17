import math
arr=[1,2,3,4]
print (" to sum all the items in the list")
sum=0
for i in arr:
    sum+=i
print(sum)    
print(" to get the largest number from the list")
print(max(arr))
print(" odd numbers list")
My_list = [*range(1200,2000,125)]
list = [x for x in My_list if x%2!=0 ]
print(list)
print(" get a new list from the previous list starting from the start to the 5th element in the list")
newlist=list[:5]
print(newlist)