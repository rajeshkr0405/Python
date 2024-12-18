#Dictionaries are used to store data values in key:value pairs
#They are unordered, mutable(changeable)& don't allow dublicate keys

# dict={
#     "name" : "Rajesh",
#     "cgps" : 9.5,
#     "marks" : [98,97,95]     "key" : value
# }
# dict["name"],dict["cgps"],dict["marks"]
# dict["key"]="value" #to assign or add new 
dict={
    "name" : "Rajesh",
    "cgps" : 9.5,
    "marks" : [98,97,95]     
}
print(dict["name"])
dict["name"]="rakesh"
print(dict["name"])
dict["surename"]="kumar"
print(dict["surename"])
