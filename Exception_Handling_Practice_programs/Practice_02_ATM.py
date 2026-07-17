try:
    balance = 10000

    print("1. Check Balance")
    print("2. Deposit") 
    print("3. Withdraw") 

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance: ", balance)
    elif choice == 2:
        amount = float(input("Enter your deposit amount: "))
        balance = balance + amount 
        print("Updated Balance: ", balance) 
    elif choice == 3:
        amount = float(input("Enter your withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Updated Balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid Choice") 
except ValueError:
    print("Please enter a valid number")
finally:
    print("Thank you for using ATM.") 
