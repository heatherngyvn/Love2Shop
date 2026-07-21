def calculate_discount(points):
    return points * 0.01

def apply_discount(total_cart_cost, discount):
    return max(0, total_cart_cost - discount)

def calculate_discounted_total(total, points):
    discount = calculate_discount(points)
    discounted_cart_total = total - discount
    if total > discount:
        return discounted_cart_total, 0
    else:
        return 0, points - int(total * 100)

def print_discount_cart_details(reward_points, discounted_cart_total, discount):
    # making sure discounted cart total isn't negative
    if discounted_cart_total > 0:
        print("Using "f"{reward_points}""pts for shopping cart for a discount of $"f"{discount:.2f}")
        print("Your new discounted total is $"f"{discounted_cart_total}")
    else:
        discounted_cart_total = 0
        reward_points = 0
        print("Your points cover the entire purchase! Your total is now $0.00")
    
def update_reward_points(reward_points, spending):
    # calculating/updating rewards points after purchase
    reward_points += int(spending)
    return reward_points

