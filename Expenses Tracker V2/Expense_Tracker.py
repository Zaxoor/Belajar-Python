# Expense Tracker

import json

try:
    with open("expenses.json", "r") as file:
        expense = json.load(file)
except FileNotFoundError:
    expense = [
        {"deskripsi": "Makan", "harga": 25000, "kategori": "Food"},
        {"deskripsi": "Bensin", "harga": 50000, "kategori": "Transport"},
        {"deskripsi": "Kopi", "harga": 25000, "kategori": "Food"}
    ]
running = True

while running:
    print("==== EXPENSE TRACKER ====")
    print("1. Show expenses")
    print("2. Show expenses by category")
    print("3. Add expense")
    print("4. Remove expense")
    print("5. Edit expense")
    print("6. Category summary")
    print("7. Show total")
    print("8. Exit")

    choice = input("Choose: ")
    print("")

    if choice == "8":
        print("Thank you for using our program!")
        print("")
        with open("expenses.json", "w") as file:
            json.dump(expense, file, indent=4)
        running = False
    elif choice == "1":
        print("==== EXPENSES ====")
        if not expense:
            print("There's no available expense to show")
            print("")
        else:
            for expenses in expense:
                print(f"{expenses["deskripsi"]} - Rp{expenses["harga"]}")
                print(f"Category : {expenses['kategori']}")
                print("")
            print("")
    elif choice == "2":
        print("==== SHOW EXPENSES BY CATEGORY ====")
        category = input("Input category: ")
        print("")
        found = False
        for expenses in expense:
            if expenses["kategori"].lower() == category.lower():
                print(f"{expenses['deskripsi']} - Rp{expenses['harga']}")
                found = True
        if not found:
            print(f"There's no {category} in your expenses.")
        print("")
    elif choice == "3":    
        print("==== ADD EXPENSE ====")
        deskripsi = input("Input new description: ")
        while True:
            try: 
                harga = int(input("Input new price: "))
                if harga <= 0:
                    print("Please input the price > 0.")
                else:    
                    break
            except ValueError:
                print("Invalid input. Please input the price with integers.")
        kategori = (input("Input new category: "))
        new_expenses = {
            "deskripsi": deskripsi, "harga": harga, "kategori": kategori
        }
        expense.append(new_expenses)
        print("")
    elif choice == "4":
        print("==== REMOVE EXPENSE ====")
        if not expense:
            print("There's no expense to remove")
            print("")
        else:
            for nomor, expenses in enumerate(expense, start=1):
                print(f"{nomor}. {expenses["deskripsi"]} - Rp{expenses["harga"]}")
            remove_expense = int(input("Choose expense in number to remove: "))
            if remove_expense > len(expense) or remove_expense < 1:
                print("")
                print("Invalid input, please try again")
                print("")
            else:
                remove_expense = remove_expense - 1
                i = expense.pop(remove_expense)
                print(f"Removed: {i["deskripsi"]} - Rp{i["harga"]}")
                print("")
    elif choice == "5":
        print("==== EDIT EXPENSE ====")
        if not expense:
            print("There's no expenses to edit.")
        else:
            for nomor, expenses in enumerate(expense, start=1):
                print(f"{nomor}. {expenses["deskripsi"]} - Rp{expenses["harga"]}")
            print("")
            while True: 
                try:   
                    edit = int(input("Choose expense number to edit: "))
                    if edit < 1 or edit > len(expense):
                        print("Invalid input. Please choose the number of expense to edit it.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please input a number to edut an expense.")
            print("")
            if edit > len(expense) or edit < 1:
                print("invalid input. Please try again next time.")
            else:
                index = edit - 1
                expenses = expense[index]
                deskripsi = input("Input description: ")
                while True:
                    try: 
                        harga = int(input("Input price: "))
                        if harga <= 0:
                            print("Please input the price > 0.")
                        else:    
                            break
                    except ValueError:
                        print("Invalid input. Please input the price with integers.")
                kategori = (input("Input category: "))
                expenses["deskripsi"] = deskripsi
                expenses["harga"] = harga
                expenses["kategori"] = kategori
                print("\nExpense edited successfully.")
                print("")
    elif choice == "6":
        print("==== CATEGORY SUMMARY ====")
        if not expense:
            print("There's no expenses to summarize.")
            print("")
        else:
            counted = []
            for expenses in expense:
                kategori = expenses['kategori']
                if expenses["kategori"] not in counted:
                    counted.append(kategori)
                    total = 0
                    for item in expense:
                        if item['kategori'] == kategori:
                            total += item['harga']
                    print(f"{kategori} = Rp{total}")
            print("") 
    elif choice == "7":
        if not expense:
            print("==== TOTAL EXPENSES ====")
            print("There's no expenses to measure")
            print("")
        else:
            print("==== TOTAL EXPENSES ====")
            for expenses in expense:
                print(f"{expenses["deskripsi"]} - Rp{expenses["harga"]}")
                print(f"Category : {expenses['kategori']}")
                print("")
            total = 0
            for expenses in expense:
                total += expenses["harga"]
            print("The total price is: Rp" + str(total))
            print("")