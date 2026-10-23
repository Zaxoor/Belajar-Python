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
    print("6. Show Summary by Type")
    print("7. Show Summary by Category")
    print("8. Search Transactions")
    print("9. Show Transaction Type Summary")
    print("10. Exit")

def exit_program():
    print("\n===== EXIT =====")
    print("Thank you for using our program!")

def input_teks_valid(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input cannot be empty!")
        else:
            return teks

def add_income():
    print("\n===== ADD INCOME =====")
    deskripsi = input_teks_valid("Description: ")
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
            kategori = input_teks_valid("Category: ")
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
    deskripsi = input_teks_valid("Description: ")
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
            kategori = input_teks_valid("Category: ")
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

def hitung_saldo(total_pemasukan, total_pengeluaran):
    return total_pemasukan - total_pengeluaran

def hitung_total_jenis(jenis_transaksi):
    total = 0
    for transaction in transactions:
        if transaction['jenis'] == jenis_transaksi:
            total += transaction['nominal']
    return total

def show_summary():
    print("\n===== FINANCIAL SUMMARY =====")
    if not transactions:
        print("There's no transactions to be summarized.")
    else:
        total_income = hitung_total_jenis("Income")
        total_expense = hitung_total_jenis("Expense")
        balance = hitung_saldo(total_income, total_expense)
        print(f"Total Income: Rp{total_income}")
        print(f"Total Expense: Rp{total_expense}")
        print(f"Balance: Rp{balance}")

def show_transaction_type_summary():
    print("\n===== TRANSACTION TYPE SUMMARY =====")
    if not transactions:
        print("No transactions available.")
        return
    total_income = hitung_total_jenis("Income")
    total_expense = hitung_total_jenis("Expense")
    print(f"Total Income: Rp{total_income}")
    print(f"Total Expense: Rp{total_expense}")

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
        print("No transactions available")
        return

    total_kategori = {}
    for transaction in transactions:
        kategori = transaction['kategori']
        nominal = transaction['nominal']
        if kategori in total_kategori:
            total_kategori[kategori] = nominal + total_kategori[kategori]
        else:
            total_kategori[kategori] = nominal
    for kategori, total in total_kategori.items():
        print(f"{kategori} - Rp{total}")    

running = True
    
while running:
    menu()
    option = input("\nOption: ")
    if option == "10":
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
    elif option == "9":
        show_transaction_type_summary()