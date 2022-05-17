my_list = [1, 2, 6, 4, 10, 0, 8, 20]


# Q1
def sumList(list):
    sum = 0
    for x in list:
        sum += x

    return sum


print(sumList(my_list))


# Q2
def getLarge(list):
    largest = list[0]
    for x in list:
        if largest <= x:
            largest = x

    return largest


print(getLarge(my_list))

# Q3
oddList = [x for x in range(1200, 2000, 125) if x % 2 != 0]

print(oddList)


# Q4

def sliceList(list):
    newList = list[5:]

    return newList


print(sliceList(oddList))
