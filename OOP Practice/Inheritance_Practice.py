class Person:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Nama : {self.__nama}")
        print(f"Umur : {self.umur}")

class Student(Person):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan

class Lecturer(Person):
    def __init__(self, nama, umur, nidn, mata_kuliah):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

student1 = Student("Hasbi", 19, 260101, "Informatika")
student1.perkenalan()
print(f"NIM : {student1.nim}")
print(f"Jurusan : {student1.jurusan}\n")

lecturer1 = Lecturer("Pak Budi", 35, 123456, "Pemrograman Python")
lecturer1.perkenalan()
print(f"NIDN : {lecturer1.nidn}")
print(f"Mata kuliah : {lecturer1.mata_kuliah}\n")