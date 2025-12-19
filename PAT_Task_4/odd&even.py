num=[10,501,22,37,100,999,87,35]
odd_num=[]   #odd num wil store here
even_num=[]  #even num will store here
for i in num:     #using loop we are spliting into odd and even
    if i % 2 == 0:
        even_num.append(i)  #append will add the number at the end of the list
    else:
        odd_num.append(i)
print("even numbers:" ,even_num)
print("odd numbers:" ,odd_num)

