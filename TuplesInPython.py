# # A built-in data type that lets us create immutable sequence of values.
# # tup = (87,64,33,95,76) #tup[0],tup[1]...
# # top[0] = 43 #Not allowed in Python

# # tup1 = ()
# # tup2= (1,)
# # tup3= (1,2,3)
# what is list : list mutable data type that value can be change
# what is tuplese : tuple is immutable data type that value can't be changes
'''
tup1 = (1,2,3,4)
print(type(tup1))
print(tup1[1])
tup2= (2,)
print(tup2)
print(type(tup2))
'''
#Tuple methods
'''
tup = (2,1,3,1)
tup.index(el) # returns index of first occurrence tup.index(1) is 1
tup.count(el) #counts total occurrences tup.count(1) is 2
'''
'''
tup =(1,2,3,4,2)
print(tup.index(2))
print(tup.count(2))
'''
'''
#Wwrite a programm to ask the user to enter names of their 3 favorite movies & store then in a list
FirstMovie = input("Enter first favorite movie name :")
secondMovie = input("Enter Second favorite movie name :")
thirdMovie = input("Enter third favorite movie name :")
movies = []
movies.append(FirstMovie)
movies.append(secondMovie)
movies.append(thirdMovie)
print(movies)
'''
'''
#Write a Program to check if a list contains a palindrome of elements .(hint : use copy() method)
list = [1,2,1]
copy_list1=list.copy()
copy_list1.reverse()
if(copy_list1 == list):
    print("Palindrome")
else:
    print("Not Palindrome")
    '''
'''
#Write to count the number of students with the "A" grade in the following tuple
#["c","d","a","b","b","a"]
grade = ("C" , "D" , "A" , "B" , "B" , "A")
print(grade.count("A"))
'''
#Store the above values in a list & sort them from "A" to "D"
grade = ["C" , "D" , "A" , "B" , "B" , "A"]
grade.sort()
print(grade)
