
lst=[3,5,7,9,4,6,8,4,8,9]
print(sum(lst))
print(max(lst))


def odd_numbers(num1:int,num2:int)->int:
    return [num for num in range(num1, num2, 125) if num % 2 !=0]

print(odd_numbers(1200,2000))


newlist = []
newlist.extend(lst)
print(newlist)