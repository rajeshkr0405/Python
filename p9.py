#Print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
'''list = [1,4,9,16,25,36,49,64,81,100]
for List in list:
    print(List)
else:
    print("Loop Ends")'''

#Searh for a number X in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
numbers = (1,4,9,16,25,36,49,64,81,100,40)
x = 49
idx = 0
for nbr in numbers:
    if(nbr == x):
        print("number found at", idx)
        idx += 1

