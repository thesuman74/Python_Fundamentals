# # most common varible X and Y 
# x = 5 
# y = "Ram"
# print(x)

# # print(x,y)

# # # getting types 
# # print(type(y))

# # #Casting
# # x = str(5)
# # print(type(x))


# # #1.Variable Names 
# #        # Rules are basically same like other languages 
# #         #1.1 must start with a letter or the underscore character 
# # myvar = "John"
# # _my_var = "John"

# #         # 1.2 A variable name can only ontain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# #         # 1.3 Variable names are case-sensitive (age, Age and AGE are three different variables)
# #         # 1.4 A variable name cannot be any of the Python keywords.
# #         # 1.5 Canot start with numbers. 

# # #2. Assigning multiple values 
# # x,y = 5, "ram"
# x,y,z = 5, "ram"
#  # 2.1 One value to multiple variables
# x = y = z = "ram"
# print(x,y,z)

# # we cann't do this 
# x,y,z = 5, "ram" # enough varibles



# #2.2 unpacking a collection
# names = ["ram", "Hari", "shayam"]
# a , b, c = names

# # 3 Output variables 
# 3.1 strings 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #with space
print(x + y + z) #without space

# 3.2 Numbers 

x = 5
y = 10
print(x + y)

# numbers and string 
z = "ram "
# print(x + z) # error 
print(x, z)  

#4 Global variables - 

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# def myfunc():
#     global x
# x = "fantastic"
# # print(type(x))

# def anotherfunc():
#     y = "ram"
#     print(x ,y)
    
# anotherfunc()