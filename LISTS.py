
my_list = [1,2,3,50,7,8,9,5,10,6]

def sum_list():
    print("list sum = " , sum(my_list))

sum_list()

def largest_number():
    print("the largest number is :" , max(my_list))

largest_number()


def odd_number(num1:int , num2:int):
    list_odd =[]
    for i in range(num1,num2+1,125):
        if (i%2!=0):
           list_odd.append(i)
    print("the odd number list is :",list_odd)
    #Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list
    new_list = list_odd[:5]
    print("the new slicing list is :" ,new_list)


odd_number(1200,2000)     



            
