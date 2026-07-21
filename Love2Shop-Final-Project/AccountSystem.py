import json

def load_user_account(users):
    returning_member_username = input("Welcome back! Please enter your username: ")
    returning_member_password = input("Please enter your password for this account: ")
    if returning_member_username not in users:
        print("Your username not found. Please try again.")
        return None

    if users[returning_member_username]["password"] != returning_member_password:
        print("Your password is incorrect. Please try again.")
        return None

    print(f"Welcome back, {returning_member_username}!")
    return returning_member_username

def create_user_account(users):
    print("Please create an account with us today!")
    new_member_username = input("Please enter your username for this account: ")
    if new_member_username in users:
        print("That username is already taken. Please try again.")
        return None
    new_member_password = input("Please enter your password for this account: ")
    users[new_member_username] = {"password": new_member_password, "reward_points": 0, "closet": []}
    save_user_account(users)
    print("Account creation is successful!")
    return new_member_username

def save_user_account(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def get_all_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
