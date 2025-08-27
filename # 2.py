# 1. Define the function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    else:
        return price

# 2. Inserted numeric values
original_price = 100.0
discount = 25.0

final_price = calculate_discount(original_price, discount)

print("Final price after discount: $", round(final_price, 2))

