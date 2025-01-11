#Break & Continue 
#Break : Used to terminate the loop when encountered.
#Continue : terminate execution in the current iteration & continue execution of the loop whith the iteratio
i =1
while i<= 10 :
    if(i%2 != 0):
        i +=1
        continue
    print(i)
    i +=1