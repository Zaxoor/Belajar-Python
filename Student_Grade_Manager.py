students = [
    {
        "nama": "Hasbi",
        "nim": "260101",
        "nilai": [80, 75, 90]
    },
    {
        "nama": "Arina",
        "nim": "260102",
        "nilai": [90, 85, 95]
    },
    {
        "nama": "Ikvina",
        "nim": "260103",
        "nilai": [75, 80, 85]
    }
]

running = True

while running:
    print("\n==== STUDENT GRADE MANAGER ====\n" \
    "1. Show Students\n" \
    "2. Add Students\n" \
    "3. Search Students\n" \
    "4. Calculate Average\n" \
    "5. Show Highest Grade\n" \
    "6. Delete Student\n" \
    "7. Exit\n")
    choice = input("Choose option: ")

    if choice == "1":
        print("\n==== STUDENT LIST ====\n")
        for nomor, student in enumerate(students, start=1):
            nilai = ", ".join(map(str, student["nilai"]))
            print(
                f"{nomor}. Nama  : {student['nama']}\n"
                f"   NIM   : {student['nim']}\n"
                f"   Nilai : {nilai}\n"
            )
    elif choice == "2":
        print("\n==== ADD STUDENT ====\n")
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai1 = int(input("Masukkan nilai pertama: "))
        nilai2 = int(input("Masukkan nilai kedua: "))
        nilai3= int(input("Masukkan nilai ketiga: "))

        new_student = {
            "nama": nama,
            "nim": nim,
            "nilai": [nilai1, nilai2, nilai3]
        }
        students.append(new_student)
        print("\nProses input data baru berhasil.")
    elif choice == "3":
        print("\n==== SEARCH STUDENT ====")
        cari = input("\nMasukkan nama/NIM: ").lower()
        for student in students:
            if cari == student["nama"].lower() or cari == student["nim"]:
                nilai = ", ".join(map(str, student["nilai"]))
                print("\nData ditemukan!\n" \
                f"Nama  : {student['nama']}\n"
                f"Nim   : {student['nim']}\n"
                f"Nilai : {nilai}\n")
    elif choice == "4":
        print("\n==== CALCULATE AVERAGE ====\n")
        for nomor, student in enumerate(students, start=1):
            total = sum(student["nilai"])
            jumlah = len(student["nilai"])
            rata_rata = total / jumlah
            print(f"{nomor}. Nama : {student['nama']}\n"
            f"   Rata-rata : {rata_rata}\n")
    elif choice == "5":
        print("\n==== HIGHEST GRADE ====\n")
        nilai_tertinggi = 0
        student = ""
        for student in students:
            nilai_student = max(student["nilai"])
            if nilai_student > nilai_tertinggi:
                nilai_tertinggi = nilai_student
                nama_student = student["nama"]
                nim_student = student["nim"]
        print("Nilai tertinggi ditemukan!")
        print(f"Nama            : {nama_student}\n"
            f"Nim             : {nim_student}\n"
            f"Nilai tertinggi : {nilai_tertinggi}\n")
    elif choice == "6":
        print("\n==== DELETE STUDENT ====\n")
        for nomor, student in enumerate(students, start=1):
            print(f"{nomor}. {student['nama']}")
        pilihan = int(input("\nMasukkan nomor data yang ingin dihapus: "))
        index = pilihan - 1
        nama_student = students[index]['nama']
        students.pop(index)
        print(f"\nData {nama_student} berhasil dihapus.")
    elif choice == "7":
        running = False
        print("\n==== EXIT ====\n")
        print("Terima kasih telah menggunakan program kami!\n")