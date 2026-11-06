class Student:
    universitas = "UPNVJ"
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, daftar_nilai):
        self.nama = nama
        self.nim = nim
        self.daftar_nilai = daftar_nilai
        Student.jumlah_mahasiswa += 1

    def tampilkan_data(self):
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Universitas : {self.universitas}")
        print(f"Daftar Nilai : {self.daftar_nilai}\n")

    def hitung_rata_rata(self):
        jumlah = sum(self.daftar_nilai)
        rata_rata = jumlah / len(self.daftar_nilai)
        return rata_rata

    def cek_status_kelulusan(self):
        rata_rata = self.hitung_rata_rata()
        if rata_rata >= 60:
            status = "Lulus\n"
        else:
            status = "Tidak Lulus\n"
        return status

    @classmethod
    def ubah_universitas(cls, universitas_baru):
        cls.universitas = universitas_baru

    @classmethod
    def tampilkan_jumlah(cls):
        print(f"Universitas : {cls.universitas}")
        print(f"Jumlah Mahasiswa : {cls.jumlah_mahasiswa}\n")

    @staticmethod
    def cek_kelulusan(nilai):
        if nilai >= 60:
            status = "Lulus\n"
        else:
            status = "Tidak Lulus\n"
        return status

    def __str__(self):
        return f"Nama : {self.nama}\nNIM : {self.nim}\n"

    def __len__(self):
        return len(self.daftar_nilai)

    def __eq__(self, other):
        return self.nim == other.nim

    def __add__(self, other):
        total = self.daftar_nilai + other.daftar_nilai
        return Student("Hasil Gabungan", "-", total)
    
student1 = Student("Hasbi", 101, [100, 90, 85])
student2 = Student("Arina", 102, [95, 90, 85])
student3 = Student("Ikvina", 103, [90, 80, 70])

student1.tampilkan_data()
student2.tampilkan_data()
student3.tampilkan_data()

print(student1.hitung_rata_rata())
print(student1.cek_status_kelulusan())

Student.ubah_universitas("Universitas Indonesia")

Student.tampilkan_jumlah()

print(Student.cek_kelulusan(85))
print(Student.cek_kelulusan(50))

print(student1)

print(len(student1))

print(student1 == student2)

student4 = student1 + student2
print(student4.daftar_nilai)