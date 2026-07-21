from Items import (
    item_prices, add_item_to_cart, remove_item_from_cart,
    print_shopping_cart, get_item_price, clear_shopping_cart,
    checkout_shopping_cart
)
from AccountSystem import (
    get_all_users,
    load_user_account, 
    create_user_account,
    save_user_account
)

def main():
    # empty list to store shopping list items
    shopping_cart = []
    # initialize shopping cart to 0
    total_cart_cost = 0
    # initialize reward points to 0
    reward_points = 0

    # app introduction
    print("╭──────────────────────────╮")
    print("│      LOVE2SHOP APP       │")
    print("╰──────────────────────────╯")
    print("Welcome to Love2Shop!")
    
    # account management
    users = get_all_users()
    member_response = input("Hello! Are you a new member or returning member? Please write new or returning: ").strip().lower()
    if member_response == "new" or member_response == "new member":
       username = create_user_account(users)
    else:
        username = load_user_account(users)
    if username is None:
        return
    reward_points = users[username]["reward_points"]
        
    # user introduction
    print("Welcome to Love2Shop, " f"{username}!")
    budget = float(input("Please set your budget for this shopping trip: "))
    print("Your budget is $"f"{budget:.2f}.")
    print("Your total reward points: " f"{reward_points}")
    print("-------------------------------------------------------------------------------------------")
    print("⋆˚౨ৎ ⋆.˚Every dollar spent gives you 1 reward point for discounts on your purchases⋆˚౨ৎ ⋆.˚")
    print("⊹₊⟡⋆1 reward point has a discount value of 1 cent⊹₊⟡⋆")

    # shopping menu
    while True:
        print("\n ★ Shopping Menu ★")
        print("[1] Add an item")
        print("[2] Remove an item")
        print("[3] View your shopping cart")
        print("[4] Checking item price")
        print("[5] Clear your entire shopping cart")
        print("[6] Check out!")
        print("[7] View store")
        print("[8] View closet")
        print("[9] Quit\n")

    # handling user input
        user_choice = input("What would you like to do? Only enter the number (1-9): ").strip()

        if user_choice == "1":
            item = input("Please enter the shopping item from the store you would like to add: ").strip()
            total_cart_cost = add_item_to_cart(item, shopping_cart, total_cart_cost, budget)
            
            
        elif user_choice == "2":
            item = input("Please enter the shopping item from the store you would like to remove: ").strip()
            total_cart_cost = remove_item_from_cart(item, shopping_cart, total_cart_cost, budget)

        elif user_choice == "3":
            print_shopping_cart(shopping_cart, total_cart_cost, budget)
            
        elif user_choice == "4":
            check_item = input("Which item would you like to check the price of? ").strip()
            get_item_price(check_item)

        elif user_choice == "5":
            total_cart_cost = clear_shopping_cart(shopping_cart)

        elif user_choice == "6":
            purchased_items = shopping_cart.copy()
            total_cart_cost, reward_points = checkout_shopping_cart(shopping_cart, total_cart_cost, reward_points)
            users[username]["closet"].extend(purchased_items)
            users[username]["reward_points"] = reward_points
            save_user_account(users)
        
        elif user_choice == "7":
        # shopping list selection (items to choose from)
            print("\n｡𖦹°‧Store｡𖦹°‧")
            for category, items in item_prices.items():
                print(f"\n{category.capitalize()}")
                for item, price in items.items():
                    print(f"{item}: ${price}")
        
        elif user_choice == "8":
            print("\n˙⋆✮your saved closet˙⋆✮")
            closet_items = users[username]["closet"]

            if closet_items:
                from collections import Counter
                item_counts = Counter(closet_items)
                for item, quantity in item_counts.items():
                    print(f"- {item} x{quantity}")
            else:
                print("Your closet is empty!")

        elif user_choice == "9":
            print("✦Thank you for visiting Love2Shop! I hope you enjoyed your time here!✦")
            break

        else:
            print("Invalid choice. Please try again.")

# main method
if __name__ == "__main__":
    main()