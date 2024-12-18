# myDict.keys() #return all keys
# mydict.values() #return all values
# myDict.items() # return all
# myDict.get(Key) #return the key according to value
# myDict.update(newDict) #insert the specified items to the dictionary
Student = {
    "name" : "Shradha",
    "score" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 95,
    }
    
} 
print(list(Student.values()))
print(len(Student.keys()))
print(Student.items())
print(Student["name"])
print(Student.get("name"))
Student.update({"city" : "Delhi"})
print(Student)