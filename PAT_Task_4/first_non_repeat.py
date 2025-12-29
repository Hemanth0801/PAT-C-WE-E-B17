#first non-repeating number

list=[1,2,3,4,5,6,4,3,2,1]

for i in list:
    if list.count(i) == 1:    #here they ask first dig to non-repeat so it wwill display 5
        print(i)
        break               #condition satisfied and it brek