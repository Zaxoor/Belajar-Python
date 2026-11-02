class Student:
    def __init__(self, nama, nim, nilai, jurusan):
        self.nama = nama
        self.nim = nim
        self.__nilai = nilai
        self.jurusan = jurusan

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Nilai harus berada di rentang 0-100!")
    def perkenalan(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

    def tampilkan_nilai(self):
        print(f"Nilai: {self.__nilai}")

    def cek_kelulusan(self):
        if self.__nilai >= 60:
            self.status = "Lulus"
        else:
            self.status = "Tidak lulus"
        print(f"Status: {self.status}\n")

student1 = Student("Hasbi", 260101, 100, "Informatika")

student1.perkenalan()
print(student1.get_nilai())
student1.set_nilai(80)
student1.tampilkan_nilai()
student1.cek_kelulusan()
student1.set_nilai(150)
student1.tampilkan_nilai()