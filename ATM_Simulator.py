saldo = 500000
running = True

while running:
    print("==== ATM SIMULATOR ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("")
    
    option = input("Choose option: ")

    if option == "1":
        print("")
        print("==== BALANCE ====")
        format_saldo = f"{saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"Your balance : Rp.{format_saldo}")
        print("")
    elif option == "2":
        print("")
        print("==== DEPOSIT ====")
        print("")
        deposit = int(input("Input your deposit: "))
        if deposit <= 49999:
            print("")
            print("Invalid deposit amount.")
            print("Minimum deposit : Rp.50.000,00")
            print("")
        else: 
            saldo += deposit
            print("")
            print("Deposit successful.")
            print("")
    elif option == "3":
            print("")
            print("==== WITHDRAW ====")
            print("")
            withdraw = int(input("Input your withdraw: "))
            if withdraw >= saldo or withdraw <= 0 or saldo - withdraw < 50000:
                print("")
                print("invalid withdraw amount.")
                print("Your balance cannot be 0.")
                print("Your minimum balance value after withdraw is Rp.50.000,00")
                print("")
            else:
                saldo -= withdraw 
                print("")
                print("Withdraw successful")
                print("")
    elif option == "4":
        running = False
        print("")
        print("==== EXIT ====")
        print("")
        print("Thank you for using our program.")
        print("")
    else:
        print("")
        print("Invalid input.")
        print("Please choose a number between 1 - 4 to use this program.")
        print("")