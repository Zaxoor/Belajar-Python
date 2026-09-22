# Expense Tracker

expense = [
    {"deskripsi": "Makan", "harga": 25000},
    {"deskripsi": "Bensin", "harga": 50000},
    {"deskripsi": "Kopi", "harga": 25000}
]
running = True

while running:
    print("==== EXPENSE TRACKER ====")
    print("1. Show expenses")
    print("2. Add expense")
    print("3. Remove expense")
    print("4. Show total")
    print("5. Exit")

    choice = input("Choose: ")
    print("")

    if choice == "5":
        running = False
        print("Thank you for using our program!")
        print("")
    elif choice == "1":
        print("==== EXPENSES ====")
        if not expense:
            print("There's no available expense to show")
            print("")
        else:
            for expenses in expense:
                print(f"{expenses["deskripsi"]} - Rp{expenses["harga"]}")
            print("")
    elif choice == "2":    
        print("==== ADD EXPENSE ====")
        new_expense = {
            "deskripsi": input("Masukan deskripsi: "),
            "harga": int(input("Masukan harga: "))
        }
        print("")
        expense.append(new_expense)
    elif choice == "3":
        print("==== REMOVE EXPENSE ====")
        if not expense:
            print("There's no expense to remove")
            print("")
        else:
            for nomor, expenses in enumerate(expense, start=1):
                print(f"{expenses["deskripsi"]} - Rp{expenses["harga"]}")
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
    elif choice == "4":
        if not expense:
            print("==== TOTAL EXPENSES ====")
            print("There's no expenses to measure")
            print("")
        else:
            print("==== TOTAL EXPENSES ====")
            for expenses in expense:
                print(f"{expenses["deskripsi"]} - Rp{expenses["harga"]}")
            total = 0
            for expenses in expense:
                total += expenses["harga"]
            print("The total price is: Rp" + str(total))
            print("")