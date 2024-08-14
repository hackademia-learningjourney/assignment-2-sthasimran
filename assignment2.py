import json

def signUP_IN():
    # Load existing user data from the JSON file
    try:
        with open("user_info.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    option = int(input("1. Sign Up\n2. Sign In\nEnter any one option: "))

    if option == 1:
        username = input("Enter your username: ")
        if username in users:
            print("Username already exists. Please try a different one.")
            return
        
        password = input("Enter your password: ")
        mobile_no = input("Enter your mobile number: ")

        # Adding new user information to the dictionary
        #key:value
        users[username] = {'password': password, 'mobile_no': mobile_no}

        # Saving the updated user information back to the JSON file
        with open("user_info.json", "w") as f:
            json.dump(users, f)

        print("Sign up successful!")

    elif option == 2:
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")

        # Check if the entered username exists and the password matches
        if entered_username in users and users[entered_username]['password'] == entered_password:
            print(f"Successful Login! Your mobile number is {users[entered_username]['mobile_no']}.")
        else:
            print("Incorrect username or password. Please enter valid information.")

    else:
        print("Invalid option. Please enter 1 or 2.")

signUP_IN()
