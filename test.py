def calculate_bread_cost():

    price_per_loaf = 3.49
    discount_rate = 0.60

    try:
        num_day_old_loaves = int(input("Enter the number of day-old loaves being purchased: "))
        if num_day_old_loaves < 0:
            raise ValueError("Number of loaves cannot be negative.")
    except ValueError as e: 
        print(f"Invalid input: {e}")
        return

    regular_price = price_per_loaf * num_day_old_loaves
    discount = regular_price * discount_rate
    total_price = regular_price - discount

    print(f"Regular price: £{regular_price:.2f}")
    print(f"Discount:       £{discount:.2f}")
    print(f"Total price:    £{total_price:.2f}")

if __name__ == "__main__":
    calculate_bread_cost()