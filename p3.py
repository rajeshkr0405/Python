#Write a program to enter marks of 3 sujects from the user and store then iin a dictionary. 
#Start with an empty dictionary & add one by one . use subject name as key & marks as value
subject={}
x = int(input("Enter marks of physics :"))
subject.update({"physics" : x})

x = int(input("Enter marks of maths :"))
subject.update({"math" : x})
               
x = int(input("Enter marks of pyshics :"))
subject.update({"chem" : x})

print(subject)