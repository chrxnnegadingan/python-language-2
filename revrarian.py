
def bank_transaction():

    account_holder = "Maria Santos"
    balance = 10000.00
    deposit = 2500.00
    withdrawal = 1500.00

    # ERROR 1: The variable deposit_amount is not defined.
    balance = balance + deposit_amount

    # ERROR 2: The comparison uses = instead of ==.
    if balance = 11000:
        print("Balance verified.")

    # ERROR 3: The variable withdrawal_amount is undefined.
    balance = balance - withdrawal_amount

    # ERROR 4: This variable is misspelled.
    transaction_fee = 50
    final_balance = balnce - transaction_fee

    # ERROR 5: Missing closing quotation mark.
    print("Account Holder: Maria Santos)

    print("Initial Balance:", 10000.00)
    print("Deposit:", deposit)
    print("Withdrawal:", withdrawal)
    print("Final Balance:", final_balance)


bank_transaction()
