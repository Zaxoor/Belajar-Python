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
        print(f"Daftar nilai : {self.daftar_nilai}")

    def hitung_rata_rata(self):
        jumlah = sum(self.daftar_nilai)
        rata_rata = jumlah / len(self.daftar_nilai)
        return rata_rata

    def __str__(self):
        return f"Nama : {self.nama}\nNIM : {self.nim}"

    def __len__(self):
        return len(self.daftar_nilai)

    def __eq__(self, other):
        return self.nim == other.nim

    def __add__(self, other):
        nilai_gabungan = self.daftar_nilai + other.daftar_nilai
        return Student("Hasil Gabungan", "-", nilai_gabungan)

student1 = Student("Hasbi", "123", [80, 85])
student2 = Student("Arina", "456", [90, 95])

student3 = student1 + student2

print(student3)
print(len(student3))
print(Student.jumlah_mahasiswa)