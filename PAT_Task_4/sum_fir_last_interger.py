number=int(input("enter number:"))
num=str(number)   #number will change to string
first_digit=int(num[0])   #0 means position of string
last_digit=int(num[-1])   #-1 means from last character
sum_digits=first_digit+last_digit
print("first digit: ",first_digit)
print("last digit: ",last_digit)
print("sum of first and last digits: ", sum_digits)
