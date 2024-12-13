a = int(input("Enter First Numer :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter third Number : "))
print("User entered numbers are :" ,a , b ,c)
if(a>b and a>c):
    print("a is greates number amongs of entered",a)
elif(b>c):
    print("b is greates", b)
else:
    print("c is greatest",c)