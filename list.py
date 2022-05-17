new_list = [1, 2, 3, 10, 15, 20]
#Q1
sum_elemtn = sum(new_list)
print(sum_elemtn)

#Q2 
print (" Largest element is:   " , max(new_list))

#Q3
odd_list =[]
for i in range (1200 , 2000 , 125):
    
    if (i%2) != 0 :
        odd_list.append(i)
    
print ( odd_list )
    

#Q4
print (new_list[:5])