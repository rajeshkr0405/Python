'''
if - elif-else(Syntax)
if(condition):
stm1
elif(condition):
stm2
else :
    stmN
'''
# light = "pink"
# if(light ==  "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("Light is broken")
# print("end of code and runned")


# age = 24
# if(age>=18):
#     print("can vote")  #indentation for tab of space
# else:
#     print("cannot vote")

# mark = 90
# if(mark>=90):
#     print("Grade is A")
# elif(mark>=80):
#     print("Grade is B")
# elif(mark>=70):
#     print("Grade is C")
# elif(mark<=70):
#     print("Grade is D")

marks = int( input("enter student marks : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student ->", grade)