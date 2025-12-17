#tuple are data type which is a collection of items of same or another data type
#tuple are created with () and seperated with ,
#tuple are immutable
#tuple returns the items in an ordered squence

name= ('hemu','vicky','chandra','lakshmi','hemu')
print(name[1])
print(name[2],name[3])

#printing each item at a time
for i in name:
    print(i)

#for fletching and printing each item at a time by using indexing
for  i in range(len(name)):
    print(name[i])

#cout() is used to find the count of a praticular item
print(name.count("hemu"))

#index() is used to find the index postion of a given item
print(name.index("hemu"))