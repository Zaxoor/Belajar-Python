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

def calculate_average(nilai):
    total = sum(nilai)
    jumlah = len(nilai)
    rata_rata = total / jumlah
    return rata_rata
        
def show_average():
    print("\n==== CALCULATE AVERAGE ====\n")
    for nomor, student in enumerate(students, start=1):
        rata_rata = calculate_average(student['nilai'])
        print(f"{nomor}. {student['nama']} | Rata-rata: {rata_rata:.2f}")

def find_highest_grade():
    highest = 0
    for student in students:
        if max(student['nilai']) > highest:
            highest = max(student['nilai'])
            name_highest = student['nama']
    return highest, name_highest

def show_highest_grade():
    print("\n==== HIGHEST GRADE ====")
    nilai, nama = find_highest_grade()
    print(f"Name : {nama} | Grade : {nilai}")

def find_student(cari):
    for student in students:
        if cari.lower() == student['nama'].lower() or cari == student['nim']:
            return student
    else:
        return None

def show_found_student():
    print("\n==== SEARCH STUDENT ====")
    cari = input("Input name/NIM: ")
    status = find_student(cari)
    if status is None:
        print("\nNo matching data found.")
    else:
        print("\nData found!")
        print(f"Name : {status['nama']} \nNIM : {status['nim']} \nNilai: {status['nilai']} ")

def delete_student(data):
    if data > len(students) or data < 1:
        return None
    else:
        data = data - 1
        i = students.pop(data)
        return i

def show_deleted_student():
    print("\n==== DELETE STUDENT ====")
    if not students:
        print("There's no data available.")
        return
    for nomor, student in enumerate(students, start=1):
        print(
            f"{nomor}. Nama  : {student['nama']}\n"
            f"   NIM   : {student['nim']}\n"
            f"   Nilai : {student['nilai']}\n"
        )
    try:
        data_choice = int(input("Enter the data sequence of the student: "))
    except ValueError:
        print("Invalid input, please input a number next time.")
        return
    status = delete_student(data_choice)
    if status is None:
        print("No matching data found.")
    else:
        print(f"{status['nama']}'s data has been deleted successfully.")

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
        show_found_student()
    elif choice == "4":
        show_average()
    elif choice == "5":
        show_highest_grade()
    elif choice == "6":
        show_deleted_student()
    elif choice == "7":
        running = False
        print("\n==== EXIT ====\n")
        print("Terima kasih telah menggunakan program kami!\n")