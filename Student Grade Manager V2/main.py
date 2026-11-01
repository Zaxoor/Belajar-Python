import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
    {"nama": "Hasbi", "nim": "260101", "nilai": [80, 75, 90]},
    {"nama": "Arina", "nim": "260102", "nilai": [90, 85, 95]},
    {"nama": "Ikvina", "nim": "260103", "nilai": [75, 80, 85]}
    ]
    except json.JSONDecodeError:
        print("Error: students.json contains invalid JSON!")
        print("Please repair the file before running the program.")
        raise SystemExit

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

def calculate_average(nilai):
        total = sum(nilai)
        jumlah = len(nilai)
        rata_rata = total / jumlah
        return rata_rata
        
def show_average():
    print("\n==== CALCULATE AVERAGE ====\n")
    if not check_students():
        return
    else:
        for nomor, student in enumerate(students, start=1):
            rata_rata = calculate_average(student['nilai'])
            print(f"{nomor}. {student['nama']} | Rata-rata: {rata_rata:.2f}")

def find_highest_grade():
    highest = max(students[0]['nilai'])
    name_highest = students[0]['nama']
    for student in students:
        if max(student['nilai']) > highest:
            highest = max(student['nilai'])
            name_highest = student['nama']
    return highest, name_highest

def show_highest_grade():
    print("\n==== HIGHEST GRADE ====")
    if not check_students():
        return
    else:
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
    if not check_students():
        return
    else:
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
    if not check_students():
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
        save_students()
        print(f"{status['nama']}'s data has been deleted successfully.")

def add_student():
    print("\n==== ADD STUDENT ====\n")
    nama = input_nama("Input the Name: ")
    nim = input_nim("Input the NIM: ")
    nilai1 = input_nilai("Input the first value: ")
    nilai2 = input_nilai("Input the second value: ")
    nilai3 = input_nilai("Input the third value: ")
    new_student = {
        "nama": nama,
        "nim": nim,
        "nilai": [nilai1, nilai2, nilai3]
    }
    students.append(new_student)
    save_students()
    print("\nNew data input process successful.")

def input_nama(pesan):
    while True:
        nama = input(pesan).strip()
        if not nama:
            print("Name cannot be empty!")
        else:
            return nama

def input_nim(pesan):
    while True:
        nim = (input(pesan)).strip()
        if not nim:
            print("NIM Cannot be empty!")
            continue
        for student in students:
            if nim == student['nim']:
                print("NIM already exist!")
                break
        else:
            return nim

def input_nilai(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if (0 <= nilai <= 100):
                return nilai
            else:
                print("Invalid input, please input between 0 - 100.")
        except ValueError:
            print("Invalid input, please input number only.")

def show_student_list():
    print("\n==== STUDENT LIST ====\n")
    if not check_students():
        return
    else:
        for nomor, student in enumerate(students, start=1):
            nilai = ", ".join(map(str, student["nilai"]))
            print(
            f"{nomor}. Nama  : {student['nama']}\n"
            f"   NIM   : {student['nim']}\n"
            f"   Nilai : {nilai}\n"
            )

def show_menu():
    print("\n==== STUDENT GRADE MANAGER ====\n")
    print("1. Show Students")
    print("2. Add Students")
    print("3. Search Students")
    print("4. Calculate Average")
    print("5. Show Highest Grade")
    print("6. Delete Student")
    print("7. Exit")
    choice = input("\nChoose option: ")
    return choice

def check_students():
    if not students:
        print("There's no students available.")
        return False
    else:
        return True

running = True

while running:
    choice = show_menu()
    if choice == "1":
        show_student_list()
    elif choice == "2":
        add_student()
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
        print("Thank you for using our program!\n")
    else:
        print("\nInvalid menu selection!\nPlease choose between 1 - 7.")