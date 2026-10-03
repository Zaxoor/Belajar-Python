contacts = [
    {
        "nama": "Hasbi",
        "nomor": "081234567890",
        "email": "hasbi@email.com"
    },
    {
        "nama": "Arina",
        "nomor": "081122223333",
        "email": "arina@email.com"
    },
    {
        "nama": "Ikvina",
        "nomor": "080987654321",
        "email": "ikvina@email.com"
    }
]

running = True

while running:
    print("==== CONTACT BOOK ====")
    print("1. Show contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")
    choice = input("Choose : ")
    print("")

    if choice == "1":
        print("==== CONTACT LIST ====")
        for nomor, contact in enumerate(contacts, start=1):
            print(f"{nomor}, {contact['nama']}")
            print(f"   Nomor: {contact['nomor']}")
            print(f"   Email: {contact['email']}")
            print("")
    elif choice == "2":
        print("==== ADD CONTACT ====")
        nama = input("Masukkan nama : ")
        nomor = input("Masukkan nomor : ")
        email = input("Masukkan email : ")
        new_contact = {
            "nama": nama,
            "nomor": nomor,
            "email": email
        }
        contacts.append(new_contact)
        print("")
    elif choice == "3":
        print("==== SEARCH CONTACT ====")
        cari_kontak = input("Search contact: ")
        ditemukan = False
        for contact in contacts:
            if contact["nama"].lower() == cari_kontak.lower():
                print("Kontak ditemukan!")
                print(f"Nama : {contact['nama']}")
                print(f"Nomor : {contact['nomor']}")
                print(f"Email : {contact['email']}")
                print("")
                ditemukan = True
        if not ditemukan:
            print("Maaf, kontak tidak ditemukan.")
            print("")
    elif choice == "4":
        print("==== CONTACT LIST ====")
        for nomor, contact in enumerate(contacts, start=1):
            print(f"{nomor}, {contact['nama']}")
            print(f"   Nomor: {contact['nomor']}")
            print(f"   Email: {contact['email']}")
            print("")
        print("==== EDIT CONTACT ====")
        pilihan = int(input("Masukkan nomor kontak yang ingin diedit : "))
        if pilihan < 1 or pilihan > len(contacts):
            print("Maaf, pilihan kontak anda tidak valid.")
            print("")
        else:
            index = pilihan - 1
            contact = contacts[index]
            nama_baru = input("Masukkan nama baru: ")
            nomor_baru = input("Masukkan nomor baru: ")
            email_baru = input("Masukkan email baru: ")
            contact["nama"] = nama_baru
            contact["nomor"] = nomor_baru
            contact["email"] = email_baru
            print("Kontak berhasil diedit.")
            print("")
    elif choice == "5":
        print("==== CONTACT LIST ====")
        for nomor, contact in enumerate(contacts, start=1):
            print(f"{nomor}, {contact['nama']}")
        print("")
        print("==== DELETE CONTACT ====")
        pilihan = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        if pilihan < 1 or pilihan > len(contacts):
            print("Maaf, nomor kontak tidak valid.")
            print("")
        else: 
            index = pilihan - 1
            contact = contacts[index]
            nama_dihapus = contacts[index]["nama"]
            contacts.pop(index)
            print(f"Kontak {nama_dihapus} berhasil dihapus")
            print("")
    elif choice == "6":
        running = False
        print("==== EXIT ====")
        print("Terima kasih telah menggunakan program kami!")
        print("")