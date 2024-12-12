str = "I am studing python from Linkdin"
print(str.endswith("din"))
print(str.endswith("Lin")) #return true if string ends with substr

#capitalize 1st char
str = "i am studying python from ApnaCollege"
print(str.capitalize()) # it will not modify the original str
str = str.capitalize()
print(str) # it will modify the original str

#Replace funtion all occurences of old

str = "We love to to to write the code in python"
print(str.replace("o","a"))

#Find functions return 1st index of 1st occurrer index start with 0
print(str.find("o"))
print(str.find("z"))

#str count -: count the occurence of substr
print(str.count("to"))
