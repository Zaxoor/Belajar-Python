import json

try:
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
except FileNotFoundError:
    transactions = [
        {
            "jenis": "Income",
            "deskripsi": "Uang Saku",
            "nominal": 50000,
            "kategori": "Pocket Money"
        },
        {
            "jenis": "Expense",
            "deskripsi": "Makan Siang",
            "nominal": 20000,
            "kategori": "Food"
        },
        {
            "jenis": "Income",
            "deskripsi": "Uang Bensin",
            "nominal": 50000,
            "kategori": "Transport"
        },
        {
            "jenis": "Expense",
            "deskripsi": "Kalkulator",
            "nominal": 80000,
            "kategori": "Education"
        }
    ]

def simpan_data(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

def menu():
    print("\n===== PERSONAL FINANCE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Transactions")
    print("4. Show Transactions by Type")
    print("5. Show Transactions by Category")
    print("6. Show Summary")
    print("7. Show Summary by Category")
    print("8. Search Transactions")
    print("9. Exit")

def exit_program():
    print("\n===== EXIT =====")
    print("Thank you for using our program!")

def add_income():
    print("\n===== ADD INCOME =====")
    deskripsi = input("Description: ")
    try:
        nominal = int(input("Amount: "))
    except ValueError:
        print("Invalid input, please input a number.")
        return
    else:
        if nominal < 50000:
            print("Invalid input, please input the amount at least 50.000.")
            return
        else:
            kategori = input("Category: ")
            new_transactions = {
                "jenis": "Income",
                "deskripsi": deskripsi,
                "nominal": nominal,
                "kategori": kategori
            }
            transactions.append(new_transactions)
            print("\nIncome added successfully!")

def add_expense():
    print("\n===== ADD EXPENSE =====")
    deskripsi = input("Description: ")
    try:
        nominal = int(input("Amount: "))
    except ValueError:
        print("Invalid input, please input a number.")
        return
    else:
        if nominal <= 0:
            print("Expense must be higher than 0, please try again later.")
            return
        else:
            kategori = input("Category: ")
            new_transactions = {
                "jenis": "Expense",
                "deskripsi": deskripsi,
                "nominal": nominal,
                "kategori": kategori
            }
            transactions.append(new_transactions)
            print("\nExpense added successfully!")

def show_transactions():
    print("\n===== LIST TRANSACTIONS =====")
    for nomor, transaction in enumerate(transactions, start=1):
        print(f"{nomor}. {transaction['jenis']} | {transaction['deskripsi']} | Rp{transaction['nominal']} | {transaction['kategori']}")

def show_summary():
    print("\n===== FINANCIAL SUMMARY =====")
    if not transactions:
        print("There's no transactions to be summarized.")
    else:
        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction['jenis'] == "Income":
                total_income += transaction['nominal']
            elif transaction['jenis'] == "Expense":
                total_expense += transaction['nominal']
        balance = total_income - total_expense
        print(f"Total Income: Rp{total_income}")
        print(f"Total Expense: Rp{total_expense}")
        print(f"Balance: Rp{balance}")
        return

def search_transaction():
    print("\n===== SEARCH TRANSACTION =====")
    found = False
    keyword = input("Input description keyword: ")
    for transaction in transactions:
        if keyword.lower() in transaction['deskripsi'].lower():
            print("\nTransaction found!")
            print(f"Type: {transaction['jenis']}")
            print(f"Description: {transaction['deskripsi']}")
            print(f"Value: Rp{transaction['nominal']}")
            print(f"Category : {transaction['kategori']}")
            found = True
    if not found:
        print(f"{keyword} not available in transactions list.")
        return

def filter_transaction():
    print("\n===== TRANSACTION TYPE =====")
    print("1. Show income only")
    print("2. Show expense only")
    tipe = input("\nOption (1/2): ")
    if tipe == "1":
        jenis_dicari = "Income"
        print("\n===== INCOME TRANSACTIONS =====")
    elif tipe == "2":
        jenis_dicari = "Expense"
        print("\n===== EXPENSE TRANSACTIONS =====")
    else:
        print("Invalid input, please input a number between 1 and 2.")
        return
    found = False

    for nomor, transaction in enumerate(transactions, start=1):
        if transaction['jenis'] == jenis_dicari:
            print(f"{nomor}. {transaction['jenis']} | {transaction['deskripsi']} - Rp{transaction['nominal']} | {transaction['kategori']}")
            found = True
    if not found:
        print("No transactions found in this type.")
        return

def filter_category():
    print("\n===== TRANSACTION CATEGORY =====")
    print("1. Show pocket money only")
    print("2. Show food only")
    print("3. Show transport only")
    print("4. Show education only")
    kategori = input("\nOption (1-4): ")
    if kategori == "1":
        kategori_dicari = "Pocket Money"
    elif kategori == "2":
        kategori_dicari = "Food"
    elif kategori == "3":
        kategori_dicari = "Transport"
    elif kategori == "4":
        kategori_dicari = "Education"
    else:
        print("Invalid input, please input a number between 1 - 4.")
        return
    found = False

    for nomor, transaction in enumerate(transactions, start= 1):
        if transaction['kategori'] == kategori_dicari:
            print(f"{nomor}. {transaction['deskripsi']} - Rp{transaction['nominal']}")
            found = True
    if not found:
        print("No transactions found in this category.")
        return

def category_summary():
    print("\n===== CATEGORY SUMMARY =====")
    if not transactions:
        print("There's no transactions to summarized")
    else:
        total_pocket_money = 0
        total_food = 0
        total_transport = 0
        total_education = 0
        for transaction in transactions:
            if transaction['kategori'] == "Pocket Money":
                total_pocket_money += transaction['nominal']
            elif transaction['kategori'] == "Food":
                total_food += transaction['nominal']
            elif transaction['kategori'] == "Transport":
                total_transport += transaction['nominal']
            elif transaction['kategori'] == "Education":
                total_education += transaction['nominal']
        total_transaction = total_pocket_money + total_food + total_transport + total_education
        print(f"Pocket Money : Rp{total_pocket_money}")
        print(f"Food : Rp{total_food}")
        print(f"Transport : Rp{total_transport}")
        print(f"Education : Rp{total_education}")    
        print(f"\nTotal Transaction : Rp{total_transaction}")

running = True
    
while running:
    menu()
    option = input("\nOption: ")
    if option == "9":
        simpan_data(transactions)
        exit_program()
        running = False
    elif option == "1":
        add_income()
    elif option == "2":
        add_expense()
    elif option == "3":
        show_transactions()
    elif option == "4":
        filter_transaction()
    elif option == "5":
        filter_category()
    elif option == "6":
        show_summary()
    elif option == "7":
        category_summary()
    elif option == "8":
        search_transaction()