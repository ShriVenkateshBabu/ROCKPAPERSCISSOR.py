# str datatype
name2  = "hello"
# print(type(name2))
# print(type(name2)== str)
# print(isinstance(name2,str))

# using constructor function 
# name2 = str("hello world")
# print(isinstance(name2,str))

# concatentaion
# result = name2+ " " + "hello 2"
# print(result)

# casting number to str
# decade = str(1980)
# print(type(decade))

# statement = "i love flims" + decade
# print(statement)

# multi line ''' ''' 
# give the output exatly as type wwe give

# multi_line = '''i am venky
# i am venky1'''
# print(multi_line)


# \ \t \n .... \t - tab give some space and where as \n - new line ...\ to have char as str


# name ='i\'am venky \t wellcome \n to overcome'
# print(name)


# str methods

# name = "i am venky \t sub \n to Course"

# # print(name.lower()) # all to lower
# # print(name.upper())  # all to upper
# # print(name.title())  # all to first letter to upper
# # print(name.replace("venky","shri venkatesh babu")) # first paramaeter 
# # # repplaced with the second paramaetr
# # print(len(name)) # give the lenght on the str


# name+= "   "
# name = "    " + name
# print(len(name))
# print(len(name.strip()))
# print(len(name.lstrip())) # remove the space r - right l - left
# print(len(name.rstrip()))

# print(name.count("e")) # says how many time the character has been appered in my str
# print(name.islower()) # returns true if my str is full of lowercase
# print(name.isupper()) # reutrn true if my str is full of uppercase
# print(name.find("e")) # reutrn at which place the e is frist encountred
# print(name.rindex("e")) # reutrn at which place the e is last encountred
  
# stu_name = "VENKY"
# print(stu_name.center(20,'*'))
# print(stu_name.ljust(16,"$") + "23".rjust(4))

# print(stu_name[-1])
# print(stu_name[-1:3])
# print(stu_name[-1:])
# print(stu_name[:-1])

# print(stu_name.startswith("V"))
# print(stu_name.startswith("v"))

# print(stu_name.endswith("Y"))
# print(stu_name.endswith("y"))


# boolen operator

# y = True
# print(type(y))
# print(isinstance(y,bool))

# int 
# y = 12
# print(type(y))
# print(isinstance(y,int))

#float 
# y = 12.5
# print(type(y))
# x = float(12)
# print(isinstance(y,float))
# print(x)

# complex

# y = 2+5j
# x = complex(3)
# print(x)
# print(y.imag)
# print(y.real)

#bulit in methods for number
y = -12.811
x = 32.5
# print(abs(x))
# print(abs(x * -1))
# print(abs(y))

# round
# print(round(y,2)) second arguement is for the decimal points

import math
# print(math.pi)
# print(math.sqrt(int(12)))
# print(math.ceil(y))
# print(math.floor(y))


# z = str(12)
# print(z)
# print(type(z))

# zipcode  ="600"
# zp = int(zipcode)
# print(int(zipcode))
# print(type(zp))

# z = "new"
# zi = int(z)
# print(z)


# a = int(input("enter a number\n"))
# print(a +12)