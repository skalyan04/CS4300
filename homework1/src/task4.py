# task4.py
def calculate_discount(price, discount):
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)


if __name__ == "__main__":
    # usage with int
    int_price = 100
    int_discount = 20
    final_price_int = calculate_discount(int_price, int_discount)
    # Format with no decimal if it's pretty much an integer
    print(f"Final price (int): {final_price_int:.0f}")

    # usage with float
    float_price = 99.99
    float_discount = 15.5
    final_price_float = calculate_discount(float_price, float_discount)
    # Format with 2 decimal places
    print(f"Final price (float): {final_price_float:.2f}")
