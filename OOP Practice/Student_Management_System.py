class Student:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, daftar_nilai):
        self.nama = nama
        self.nim = nim
        self.daftar_nilai = daftar_nilai
        Student.jumlah_mahasiswa += 1

    def __str__(self):
        status = self.cek_kelulusan(self.hitung_rata_rata())
        return f"Nama : {self.nama}\nNIM : {self.nim}\nDaftar Nilai: {self.daftar_nilai}\nStatus : {status}\n"

    def hitung_rata_rata(self):
        jumlah = sum(self.daftar_nilai)
        rata_rata = jumlah / len(self.daftar_nilai)
        return rata_rata

    @staticmethod
    def cek_kelulusan(rata_rata):
        if rata_rata >= 75:
            status = "Lulus"
        else:
            status = "Tidak Lulus"
        return status

class StudentManager():
    def __init__(self):
        self.daftar_mahasiswa = {}

    def tambah_mahasiswa(self, student):
        if student.nim in self.daftar_mahasiswa:
            return False
        else:
            self.daftar_mahasiswa[student.nim] = student
            return True

    def tampilkan_semua(self):
        for mahasiswa in self.daftar_mahasiswa.values():
            print(mahasiswa)

    def cari_mahasiswa(self, nim):
        if nim in self.daftar_mahasiswa:
            return self.daftar_mahasiswa[nim]
        else:
            return None

    def hapus_mahasiswa(self, nim):
        if nim in self.daftar_mahasiswa:
            del self.daftar_mahasiswa[nim]
            return True
        else:
            return False

    def edit_mahasiswa(self, nim, nama_baru, nilai_baru):
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa is None:
            return False
        else:
            mahasiswa.nama = nama_baru
            mahasiswa.daftar_nilai = nilai_baru
            return True

manager = StudentManager()
s1 = Student("Hasbi", "2410511001", [80, 90, 85])
print(manager.tambah_mahasiswa(s1))  # harusnya True
print(manager.tambah_mahasiswa(s1))  # harusnya False (duplikat)
manager.tampilkan_semua()
print("")

print(manager.cari_mahasiswa("2410511001"))   # data Hasbi lengkap
print(manager.cari_mahasiswa("9999"))         # None
print(manager.hapus_mahasiswa("2410511001"))  # True
print(manager.hapus_mahasiswa("2410511001"))  # False (udah kehapus)
manager.tampilkan_semua()                     # kosong
print("")

s2 = Student("Budi", "2410511002", [60, 70, 65])
manager.tambah_mahasiswa(s2)

print(manager.edit_mahasiswa("2410511002", "Budi Santoso", [80, 85, 90]))  # True
print(manager.edit_mahasiswa("9999", "Siapa", [100]))                     # False
manager.tampilkan_semua()   # Budi Santoso, status berubah jadi Lulus