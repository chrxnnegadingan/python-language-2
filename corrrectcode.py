
def process_order():

    customer_name = "Maria Santos"
    product_name = "Wireless Headphones"
    product_price = 1500.00
    quantity = 2
    shipping_fee = 100.00
    discount_rate = 0.10

    subtotal = product_price * quantity
    discount = subtotal * discount_rate

    if quantity <= 0:
        print("Invalid quantity.")
        return

    if subtotal >= 2000:
        shipping_fee = 0.00
        print("Eligible for free shipping.")

    total_amount = subtotal - discount + shipping_fee

    print("Customer:", customer_name)
    print("Product:", product_name)
    print("Price:", product_price)
    print("Quantity:", quantity)
    print("Subtotal:", round(subtotal, 2))
    print("Discount:", round(discount, 2))
    print("Shipping Fee:", round(shipping_fee, 2))
    print("Total Amount:", round(total_amount, 2))


if __name__ == "__main__":
    process_order()
