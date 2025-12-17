#list are data type which is a collection of items of same or another data type
#list are created with [] and seperated with ,
#list are mutable
#list returns the items in an ordered squence

# name = ['hemu','vicky','sussi']
# print(len(name))
#
# #fletching single items
# print(name[0])
# print(name[1])
# print(name[2])
#
# #print two items in single print
# print(name[0],name[2])
#
# #for fletching and printing each items at a time
# for i in name:
#     print(i)
#
# #for fletching and printing a item until condition
# name = ['hemu','vicky','sussi']
# length_of_list = len(name)
# for i in range(length_of_list):#for i in range(2)
#     if i >= 1 :
#          break          #break is used to finnish then loop
# print(name[i])                #print i


# print(name[:2])
    # name = [['hemu','vicky'],['sussi']]
    # print(name)
    # print(len(name))
    # val = name[0][1]
    # print(val)

# name = ['hemu','vicky','sussi']
# length_of_list = len(name)
# print(length_of_list)
# for i in range(length_of_list):   #for i in range(3)
#     if name[i] == 'vicky':
#         continue        #continue is used to skipk the iteration
# print(name[i])

name= ['hemu','chandra','vicky']
name.insert(0,'susss')
print(name)
name.extend(['maggie','mouni'])
print(name)
name.append('susss')
print(name)
name.pop()  #pop remove the vlaue the posotion we givwn, if not it will automatically del last
print(name)
# name.clear() #clear is used to clear the list
# print(name)
name.remove('susss')
print(name)