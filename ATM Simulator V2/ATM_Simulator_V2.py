import json

try:
    with open("transactions.json", "r") as file:
        transaction = json.load(file)
except FileNotFoundError:
    transaction = {
        "saldo": 100000,
        "transactions": []
    }

saldo = transaction["saldo"]
transactions = transaction["transactions"]

def simpan_data(saldo, transactions):
    transaction = {
        "saldo": saldo,
        "transactions": transactions
    }
    with open("transactions.json", "w") as file:
        json.dump(transaction, file, indent=4)

def tampilkan_menu():
    print("==== ATM SIMULATOR ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("")

def check_balance(saldo):
    print("")
    print("==== BALANCE ====")
    format_saldo = f"{saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"Your balance : Rp.{format_saldo}")
    print("")

def deposit(saldo):
    print("")
    print("==== DEPOSIT ====")
    print("")
    try:
        deposit_value = int(input("Input your deposit: "))
    except ValueError:
        print("Input must be a number.")
        print("")
        return saldo   
    else:
        if deposit_value <= 49999:
            print("")
            print("Invalid deposit amount.")
            print("Minimum deposit : Rp.50.000,00")
            print("")
            return saldo
        else: 
            saldo += deposit_value
            print("Deposit successful.")
            print("")
            transactions.append(
                {"jenis": "Deposit", "nominal": deposit_value}
            )
            return saldo

def withdraw(saldo):
    print("")
    print("==== WITHDRAW ====")
    print("")
    try:
        withdraw_value = int(input("Input your withdraw: "))
    except ValueError:
        print("Input must be a number.")
        print("")
        return saldo
    else:
        if withdraw_value >= saldo or withdraw_value <= 0 or saldo - withdraw_value < 50000:
            print("")
            print("invalid withdraw amount.")
            print("Your balance cannot be 0.")
            print("Your minimum balance value after withdraw is Rp.50.000,00")
            print("")
            return saldo
        else:
            saldo -= withdraw_value 
            print("Withdraw successful")
            print("")
            transactions.append(
                {"jenis": "Withdraw", "nominal": withdraw_value}
            )
            return saldo

def transaction_history():
    print("\n==== TRANSACTION HISTORY ====")
    if not transactions:
        print("No transactions yet.")
    else:
        for nomor, item in enumerate(transactions, start= 1):
            print(f"{nomor}. {item['jenis']} - Rp{item['nominal']}")
        print("")

def exit_program():
    print("")
    print("==== EXIT ====")
    print("")
    print("Thank you for using our program.")
    print("")

def invalid_input():
    print("")
    print("Invalid input.")
    print("Please choose a number between 1 - 5 to use this program.")
    print("")

running = True

while running:
    tampilkan_menu()
    option = input("Choose option: ")

    if option == "1":
        check_balance(saldo)
    elif option == "2":
        saldo = deposit(saldo)
    elif option == "3":
        saldo = withdraw(saldo)
    elif option == "4":
        transaction_history()
    elif option == "5":
        simpan_data(saldo, transactions)
        exit_program()
        running = False
    else:
        invalid_input()