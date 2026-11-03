class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Nama : {self.nama}")
        print(f"Umur : {self.umur}")

class Student(Person):
    def __init__(self, nama, umur, nim, jurusan, nilai):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan
        self.__nilai = nilai

    def perkenalan(self):
        print("=== INFORMASI MAHASISWA ===")
        print(f"Nama    : {self.nama}")
        print(f"Umur    : {self.umur}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}\n")

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Nilai harus berada di rentang 0-100!")

    def cek_kelulusan(self):
        if self.__nilai >= 60:
            self.status = "Lulus"
        else:
            self.status = "Tidak lulus"
        return self.status

    def tampilkan_akademik(self):
        print("=== INFORMASI AKADEMIK ===")
        print(f"Nama : {self.nama}")
        print(f"Nilai : {self.get_nilai()}")
        print(f"Status : {self.cek_kelulusan()}\n")

class Lecturer(Person):
    def __init__(self, nama, umur, nidn, mata_kuliah):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def perkenalan(self):
        print("=== INFORMASI DOSEN ===")
        print(f"Nama        : {self.nama}")
        print(f"Umur        : {self.umur}")
        print(f"NIDN        : {self.nidn}")
        print(f"Mata Kuliah : {self.mata_kuliah}\n")

def tampilkan_informasi(person):
    person.perkenalan()

def tampilkan_semua_informasi(daftar_person):
    for person in daftar_person:
        person.perkenalan()

student1 = Student("Hasbi", 19, 260101, "Informatika", 67)
student2 = Student("Cuki", 19, 260102, "Sastra Mesin", 59)
lecturer1 = Lecturer("Budi", 35, 123456, "Python")
lecturer2 = Lecturer("Andi", 40, 123457, "Kalkulus")

daftar_person = [student1, student2, lecturer1, lecturer2]

tampilkan_semua_informasi(daftar_person)

student1.tampilkan_akademik()
student2.tampilkan_akademik()