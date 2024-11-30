from time import sleep
user_name="3mraan"
password=193746852
Account_amount=5000

while True:
    UserName_enterd = input("Enter your User Name ")
    password_enterd =int(input("Enter a password "))
    sleep(7)
    if user_name == UserName_enterd and password == password_enterd:
        Withdrawal =int(input("Enter the withdrawal amount "))
        sleep(5)
        if Withdrawal <= Account_amount:
            print(f"{Withdrawal} has been deducted from your bank account")
            sleep(5)
            Account_amount-=Withdrawal
            print(f"Your account amount has become {Account_amount}")
            break
        else:
            print("Your balance is insufficient, try again")