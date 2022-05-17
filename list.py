sum=0
first_list = [10,20,30,40]
for add in range(0,len(first_list)):
     sum = sum +first_list[add]
print("the sum of number " , sum)



second_list = [10, 20, 4, 45, 99]
  
second_list.sort()
  
print("Largest element is:", second_list[-1])


third_list = [n for n in range (1200,2000,125)if n%2 !=0]
print(third_list)