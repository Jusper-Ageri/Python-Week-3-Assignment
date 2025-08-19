def calculate_discount(price, discount_percent):

#1. Calculates the final price after applying a discount.
#2. Only applies discount if discount_percent is >= 20.
  
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display result
if final_price != price:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${final_price:.2f}")