dict = [{"name":"hemu" , "age":25},{"name":"venky","age":30},{"name":"maggie" , "age":25},{"name":"raj" , "age":21},
    {"name":"ram" , "age":18}]
f = filter(lambda x : x["age"] >=18, dict)   #first we are using  filter(is used to filter out from the  list), and lamda function
final_names = list(map(lambda x: x["name"], f))
print(final_names)

