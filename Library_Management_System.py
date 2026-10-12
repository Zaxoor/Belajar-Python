books = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "status": "Available"},
    {"judul": "Bumi", "penulis": "Tere Liye", "status": "Borrowed"},
    {"judul": "Atomic Habits", "penulis": "James Clear", "status": "Available"}
]

running = True

while running:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("\n1. Show Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    
    option = input("\nChoose option: ")

    if option == "7":
        running = False
        print("\n===== EXIT =====")
        print("\nThank you for using our program.\n")
    elif option == "1":
        print("\n===== BOOKS =====")
        for number, book in enumerate(books, start=1):
            print(f"\n{number}. Title  : {book['judul']}")
            print(f"   Writer : {book['penulis']}")
            print(f"   Status : {book['status']}")
    elif option == "2":
        print("\n===== ADD BOOK =====")
        title = input("\nInput book title : ")
        writer = input("Input book writer : ")
        new_book = {
            "judul" : title,
            "penulis" : writer,
            "status" : "Available"
        }
        books.append(new_book)
        print("\nNew book added successfully!")
    elif option == "3":
        print("\n===== SEARCH BOOK =====")
        search = input("\nInput book title : ")
        found = False
        for book in books:
            if book['judul'].lower() == search.lower():
                found = True
                print("\nBook found!")
                print(f"Title  : {book['judul']}")
                print(f"Writer : {book['penulis']}")
                print(f"Status : {book['status']}")
        if not found:
            print("\nBook not found.")
    elif option == "4":
        print("\n===== BORROW BOOK =====")
        search = input("\nInput book title : ")
        found = False
        for book in books:
            if book['judul'].lower() == search.lower():
                found = True
                if book['status'] == "Available":
                    print(f"\nThe book is available! \nNow You borrow the book.")
                    book['status'] = "Borrowed"
                else:
                    print(f"\nThe book is not available.")
        if not found:
            print("\nBook not found")
    elif option == "5":
        print("\n===== RETURN BOOK =====")
        search = input("\nInput book title : ")
        found = False
        for book in books:
            if book['judul'].lower() == search.lower():
                found = True
                if book['status'] == "Borrowed":
                    print("\nYou return the book.")
                    book['status'] = "Available"
                else:
                    print("\nThis book has not been borrowed.")
        if not found:
            print("\nBook not found.")
    elif option == "6":
        print("\n===== DELETE BOOK =====\n")
        for number, book in enumerate(books, start=1):
            print(f"{number}. Title  : {book['judul']}")
        delete = int(input("\nInput the number of book to delete it : "))
        if delete < 1 or delete > len(books):
            print("\ninvalid input.")
        else:
            index = delete - 1
            book = books[index]
            deleted_book = books[index]['judul']
            books.pop(index)
            print(f"{deleted_book} deleted successfully.")
    else:
        print("\nInvalid input. \nPlease input your option between 1-7.")