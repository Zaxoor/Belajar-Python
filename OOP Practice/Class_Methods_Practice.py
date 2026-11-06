## Sistem Pengelolaan Mahasiswa ##

class Student:
    universitas = "UPNVJ"
    jumlah_mahasiswa = 0

    def __init__(self, nama):
        self.nama = nama
        Student.jumlah_mahasiswa += 1

    @classmethod
    def ubah_universitas(cls, universitas_baru):
        cls.universitas = universitas_baru
        print(f"Universitas baru: {cls.universitas}")

    @classmethod
    def tampilkan_universitas(cls):
        print(f"Universitas: {cls.universitas}")

    @classmethod
    def tampilkan_jumlah(cls):
        print(f"Jumlah mahasiswa: {cls.jumlah_mahasiswa}")

student1 = Student("Hasbi")
student2 = Student("Arina")

Student.tampilkan_universitas()
Student.tampilkan_jumlah()
print("")
Student.ubah_universitas("UI")
Student.tampilkan_jumlah()