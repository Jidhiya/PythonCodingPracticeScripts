
balance = 0

while True:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient balance!")
    elif choice == "3":
        print("Exiting ATM. Goodbye!")
        break
    else:
        print("Invalid choice!")
