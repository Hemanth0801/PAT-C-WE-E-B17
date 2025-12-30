#rated and sorted list(values are  in order ascending)
#rotated(where the values are arranged from one side to another)

Sorted_num=[1,2,3,4,5,6,7]  #this is  sorted list
numbers = [4,5,6,7,1,2,3]  #this rotated list
minimum = numbers[0]   #just for the condition we are assuming
for num in numbers:
    if num < minimum:
        minimum = num
print("Minimum element is:", minimum)
