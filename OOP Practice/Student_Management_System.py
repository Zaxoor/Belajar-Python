# ===== 1. CLASS (logika, tanpa input/print buat user) ===== #
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

# ===== 2. FUNCTION MENU (urusan input/print ke user) ===== #
def tampilkan_menu():
    print("=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Edit Mahasiswa")
    print("5. Hapus Mahasiswa")
    print("6. Keluar")

def menu_tambah(manager):
    print("\n=== TAMBAH MAHASISWA ===")
    nama = input("Masukkan nama: ")
    while True:
        nim = input("Masukkan NIM: ")
        if manager.cari_mahasiswa(nim) is not None:
            print("NIM sudah digunakan, silahkan gunakan NIM lain.")
        else:
            break
    while True:
        nilai = input("Masukkan daftar nilai: ")
        try:
            potongan = nilai.split(",")
            daftar_nilai = []
            for item in potongan:
                angka = int(item)
                daftar_nilai.append(angka)
            break
        except ValueError:
            print("Mohon masukkan angka untuk daftar nilai.")
    mahasiswa = Student(nama, nim, daftar_nilai)
    manager.tambah_mahasiswa(mahasiswa)
    print("Mahasiswa berhasil ditambahkan!")

# ===== 3. MAIN (pengatur alur) ===== #
def main():
    manager = StudentManager()
    while True:
        tampilkan_menu()
        opsi_menu = input("Pilih Menu: ")
        
        if opsi_menu == "1":
            print("Coming soon!")
        elif opsi_menu == "2":
            print("Coming soon!")
        elif opsi_menu == "3":
            print("Coming soon!")
        elif opsi_menu == "4":
            print("Coming soon!")
        elif opsi_menu == "5":
            print("Coming soon!")
        elif opsi_menu == "6":
            print("Terima kasih sudah menggunakan program kami!")
            break
        else:
            print("Pilihan tidak valid!")

# ===== 4. JALANKAN PROGRAM =====
if __name__ == "__main__":
    main()

teks = "80,90,85"
daftar_nilai = []
potongan = teks.split(",")
for item in potongan:
    angka = int(item)
    daftar_nilai.append(angka)
print(daftar_nilai)