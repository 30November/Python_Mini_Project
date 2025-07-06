data = {}

def login(user,pwd):
    if user in data:
        if  data[user] == pwd:
            print("Welcome to our website")
            return True
        else:
            print("Please enter the coorect password")
    else:
        print("Not valid userID")
    
    return False

def create(user,pwd,confirm_pwd):
    if pwd != confirm_pwd:
        print("Password are not matching")
    elif len(pwd) < 8:
        print("Password's length to short (less than 8)")
    else:
        data[user] = pwd
        print("Registered")

while True:
    print("1.Login")
    print("2.Create")
    print("3.Delete")
    print("4.Exit")
    try:
        n = int(input("Enter the choice (1-4):"))
        if n == 1:
            user = input("Your UserId:")
            pwd = input("Password:")
            login(user,pwd)
        
        elif n == 2:
            user = input("Your UserId:")
            pwd = input("Password:")
            c_pwd = input("Confirm Password:")
            create(user,pwd,c_pwd)
        elif n == 3:
            user = input("Your UserId:")
            pwd = input("Password:")
            if login(user , pwd):
                print("Succesfully Delected")
                del data[user]
        elif n == 4:
            print("Thank you! Visit Again")
            break
        else:
            print("Enter the valid choice")
    except:
        print("Enter the valid choice")
