user_name = "3mraan"
password = 193746852

counter=1
while True:
    UserName_enterd = input("Enter your User Name ")
    password_enterd =int(input("Enter a password "))
    if user_name == UserName_enterd and password == password_enterd:
        print("welcome", user_name)
        break
    if counter<3:
        print("""the UserName or password don't correct
please try again!""")
        counter+=1
    else:
        print("Please check your bank account!!!")
        break
