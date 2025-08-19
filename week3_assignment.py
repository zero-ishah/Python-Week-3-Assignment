# Week 3 Assignment: Calculate Discount

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount if discount_percent >= 20%.
    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Output result
    if discount_percent >= 20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
