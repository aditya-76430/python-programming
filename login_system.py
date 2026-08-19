user = input("Enter your userName/ID: ")
password = input("Enter your password: ")

if (user == "admin" and password == "pass"):
    print("Login Sucessfull!")
    
elif(user == "admin" and password != "pass"):
    print("wrong pass word !")
    
elif (user != "admin" and password == "pass"):
    print("Worng user ID")

else:
    print("Try again!, Both wrong")