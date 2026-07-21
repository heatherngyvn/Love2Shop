from RewardSystem import (
    calculate_discounted_total,
    update_reward_points,
    print_discount_cart_details
)
from collections import Counter
# dictionary to store items and their prices
item_prices = {
        ".✦ ݁˖CLOTHING.✦ ݁˖": {
            "shirt": 5,
            "dress shirt": 10,
            "sweater": 10,
            "skirt": 6,
            "dress": 13,
            "shorts": 4,
            "sweatpants": 8,
            "jeans": 18,
            "socks": 5,
            "shoes ": 9,
            "dress shoes ": 15,
            "heels": 13,
            "boots": 19,
            "gloves": 6,
            "flip flops": 4,
        },
        ".✦ ݁˖ACCESSORIES.✦ ݁˖": {
            "backpack": 20,
            "tote bag": 5,
            "scarf": 9,
            "baseball cap": 9,
            "sun hat": 11,
            "purse": 25,
            "rings": 8,
            "earrings": 7,
            "watch": 15,
            "sunglasses": 12,
            "necklace": 9,
            "briefcase": 13,
        }
    }

def add_item_to_cart(item, shopping_cart, total_cart_cost, budget):
    for category, items in item_prices.items():  # iterate over categories to find item
        if item in items:
            item_cost = items[item]
            if total_cart_cost + item_cost <= budget:
                shopping_cart.append(item)
                total_cart_cost += item_cost
                print("✓ " f"{item}" " added to cart!")
                print("Your new shopping cart total is : $"f"{total_cart_cost:.2f}.")
                print("Your remaining budget is : $"f"{budget - total_cart_cost:.2f}.")
            else:
                print("⚠ "f"{item}" " cannot be added to your cart, you're over budget!")
            return total_cart_cost
    print(f"{item}" " is not available at our store, sorry about that.")
    return total_cart_cost

def remove_item_from_cart(item, shopping_cart, total_cart_cost, budget):
    if item not in shopping_cart:
        print(f"{item} is not in your shopping cart! Please try again.")
        return total_cart_cost
    for items in item_prices.values():
        if item in items:
            shopping_cart.remove(item)
            item_cost = items[item]  # ensuring we're deducting the correct item
            total_cart_cost -= item_cost
            print(""f"{item}" " has been successfully removed from your shopping cart!")
            print("Your new shopping cart total is : $"f"{total_cart_cost:.2f}.")
            print("Your remaining budget is : $"f"{budget - total_cart_cost:.2f}.")
            return total_cart_cost
    
def print_shopping_cart(shopping_cart, total_cart_cost, budget):
    if shopping_cart:
        print("\n⋆˚✿˖°your shopping cart⋆˚✿˖°")
        item_counts = Counter(shopping_cart)
        for item, quantity in item_counts.items():
            print(f"- {item} x{quantity}")
        # shopping cart summary after printing all the items
        print("\nTotal items: "f"{len(shopping_cart)}")
        print("Shopping cart total: $"f"{total_cart_cost:.2f}")
        print("Remaining budget: $"f"{budget - total_cart_cost:.2f}")
    else:
        print("There are no items to show, your shopping cart is empty!")
    
def get_item_price(check_item):
    found = False  # initialize found as False to look for item
    for items in item_prices.values():
        if check_item in items:
            price = items[check_item]
            print("The item, " f"{check_item}," " is $"f"{price}.")
            found = True # item was found
            break
    if not found:
        print("This item is not in our store, please try again.")

def find_item_price(item):
    for items in item_prices.values():
        if item in items:
            return items[item]
    return 0

def clear_shopping_cart(shopping_cart):
    print("Erasing your shopping cart....")
    shopping_cart.clear()
    total_cart_cost = 0 # reset cart total
    print("Shopping cart has been successfully erased! Your cart cost is $0.")
    return total_cart_cost

def checkout_shopping_cart(shopping_cart, total_cart_cost, reward_points):
    if not shopping_cart:  # Check cart contents upfront
        print("Your shopping cart is currently empty! Please add items before checking out.")
        return total_cart_cost, reward_points
        
    applying_discount = input("Would you like to apply your points for a discount? (1 pt = 1 cent) ")
    discounted_cart_total = total_cart_cost
    
    if applying_discount == "yes" and reward_points > 0:
       points_used = reward_points
       discounted_cart_total, reward_points = calculate_discounted_total(total_cart_cost, reward_points)
       discount = total_cart_cost - discounted_cart_total
       print_discount_cart_details(points_used, discounted_cart_total, discount)
    else:
        print("No discount is applied.")
        discounted_cart_total = total_cart_cost
        discount = 0
        print("Your cart total is $"f"{total_cart_cost:.2f}")
    subtotal =  total_cart_cost
    total_paid = discounted_cart_total
    points_earned = int(total_paid)
    print_receipt(shopping_cart, subtotal, discount, total_paid, points_earned)
    completed_checkout(shopping_cart)
    reward_points = update_reward_points(reward_points, total_paid)
    return 0, reward_points
    
def completed_checkout(shopping_cart):
    print("\n˙⋆✮your new closet˙⋆✮")
    item_counts = Counter(shopping_cart)
    for item, quantity in item_counts.items():
        print(f"- {item} x{quantity}")

    # reset shopping cart for next shopping trip!
    shopping_cart.clear()

def print_receipt(shopping_cart, subtotal, discount, total_paid, points_earned):
    print("\n===================================")
    print("          ShopEasy Receipt           ")
    print("===================================")
    print("Items Purchased:")

    item_counts = Counter(shopping_cart)
    for item, quantity in item_counts.items():
        price = find_item_price(item)
        item_total = price * quantity
        item_name = f"{item} x{quantity}"
        print(f"{item_name:.<25} ${item_total:.2f}")
    print("-----------------------------------")
    print("\n"f"{'Subtotal:':<25} ${subtotal:.2f}")
    if discount > 0:
        print(f"{'Discount:':<25} -${discount:.2f}")
    else:
        print(f"{'Discount:':<25} ${discount:.2f}")
    print(f"{'Total Paid:':<25} ${total_paid:.2f}")
    print(f"{'Reward Points Earned:':<25} {points_earned}pts")
    print("------------------------------------")
    print("Thank you for shopping with ShopEasy!")
        