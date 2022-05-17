
my_list = [1,2,3,50,7,8,9,5,10,6]

def sum_list():
    print("list sum = " , sum(my_list))

sum_list()

def largest_number():
    print("the largest number is :" , max(my_list))

largest_number()


def odd_number(num1:int , num2:int):
    new_list=[]
    for i in range(num1,num2+1,125):
        if (i%2!=0):
            new_list.append(i)
    print("the odd number list is :",new_list)
odd_number(1200,2000)     

def slicing_list():
    new_list = my_list[:5]
    print("the new slicing list is :" ,new_list)
slicing_list()

            
