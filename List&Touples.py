# A built-in data type that store set of values
# it can store elements of different types ( integer , float , string, etc.)
# marks = [87,64,33,95,76] #marks[0],marks[1]...
# student = ["Karan",85,"Delhi"] #student[0], student[1]...
# student[0] ="Arjun" #allowed in python
# len(student) # return length

marks = [90.3,87.2,55.3,79.0,89.4]
print(len(marks))
print(type(marks))
print(marks)
print(marks[0],marks[1],marks[2],marks[3],marks[4])

#Mutlple kind of data we can store in single list
student = ["Rajesh", 89 , "Delhi"]
print(type(student))
print(len(student))
print(student[0],student[1],student[2])
student[0] = "Kumar" #mutale
print(student)
# in python strings are immutale
# and lists are mutuale