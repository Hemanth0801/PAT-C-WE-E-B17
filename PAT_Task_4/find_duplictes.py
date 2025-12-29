#finding the duplicates

list_1 = [2,4,6,3,5]
list_2 = [3,5,2,9,7]
list_3 = [8,9,4,3,2]
duplicate_value=[]
for i in list_1:
    if i in list_2 and i in list_3:
        duplicate_value.append(i)
print("Duplicates numbers: ",duplicate_value)