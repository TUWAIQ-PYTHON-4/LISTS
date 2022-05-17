numbers = [2 ,6,5 ,6 ,25, 9 ,99 , 64]
suming_list = sum(numbers)
print(suming_list)
largest_value = max(numbers)
print(largest_value)
odds_numbers = []

def listOfOddNumbers(a,b,c):
    if a % 2 == 0:
        a = a + 1
    for x in range(a, b, c):
        global odds_numbers
        odds_numbers.append(x)
    return odds_numbers
print(listOfOddNumbers(1200,2000,125))

new_list = odds_numbers[0:5]
print(new_list)