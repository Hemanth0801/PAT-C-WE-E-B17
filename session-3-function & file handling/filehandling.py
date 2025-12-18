#file handling is a way to handle a text file in python
#operation supported
  #read
  #write
  #append
  #read and write.

# write into a empty  file

# path = 'text.txt'  #gives a path
# f=open(file=path,mode='w') #open a file using open(file=file path,mode for file open)
# f.write('hello world') #write something in a file
# f.close() #close the file

#read content from the file
# path='text.txt'
# f=open(file=path,mode='r')
# print(f.read())
# f.close()

#append the new lines in a file
path = 'text.txt'  #gives a path
f=open(file=path,mode='a') #open a file using open(file=file path,mode for file open)
f.write('\n this is me') #append something in a written file
f.close() #close the file




