
while True:
    user= int(input("Enter a number:?"))
    if user> 1:
        for x in range(2,user):
            if (user % x)== 0:
                 print("This is not a prime number")
                 break
        else:
                print("This is a prime number")
    else:
                print("This is not a prime number")




