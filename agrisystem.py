
def process_order():

    customer_name = "Maria Santos"
    product_name = "Wireless Headphones"
    product_price = 1500.00
    quantity = 2
    shipping_fee = 100.00
    discount_rate = 0.10

    # ERROR 1: The multiplication operator is missing.
    subtotal = product_price quantity

    # ERROR 2: The variable discount is not declared.
    discount = subtotal * discount_percentage

    # ERROR 3: The assignment operator is used instead of ==.
    if quantity = 0:
        print("Invalid quantity.")

    # ERROR 4: The variable total_amount is not declared
    # and the calculation uses an undefined shipping variable.
    total_amount = subtotal - discount + delivery_fee

    # ERROR 5: Missing colon at the end of the condition.
    if total_amount > 2000
        print("Eligible for free shipping.")

    # ERROR 6: Incorrect capitalization of the variable name.
    print("Customer:", Customer_name)

    # ERROR 7: Missing closing quotation mark.
    print("Product:", product_name)

    print("Price:", product_price)
    print("Quantity:", quantity)
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Shipping Fee:", shipping_fee)
    print("Total Amount:", total_amount)


process_order()
