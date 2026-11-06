## Static Method Practice ##

class Student:
    universitas = "UPNVJ"

    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def tampilkan_data(self):
        print(f"Nama : {self.nama}")
        print(f"Nilai : {self.nilai}")

    @classmethod
    def ubah_universitas(cls, universitas_baru):
        cls.universitas = universitas_baru
        print(f"Universitas : {cls.universitas}")

    @staticmethod
    def cek_kelulusan(nilai):
        if nilai >= 60:
            status = "Lulus"
        else:
            status = "Tidak lulus"
        return status

student1 = Student("Hasbi", 85)

student1.tampilkan_data()
print(f"Status : {Student.cek_kelulusan(student1.nilai)}\n")
student1.ubah_universitas("UI")