# task4.py

def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount percentage.
    Works with any numeric type (int, float) due to duck typing.
    """
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    final_price = price - (price * (discount / 100))
    return final_price


if __name__ == "__main__":
    print("Final price (int):", calculate_discount(100, 20)) 
    print("Final price (float):", calculate_discount(99.99, 15.5)) 
