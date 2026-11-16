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
        return f"Nama : {self.nama}\nNIM : {self.nim}\nDaftar Nilai: {self.daftar_nilai}\nStatus : {status}"

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
        for nomor, mahasiswa in enumerate (self.daftar_mahasiswa.values(), start=1):
            print(f"Data ke-{nomor}:")
            print(mahasiswa)
            print("")

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
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Edit Mahasiswa")
    print("5. Hapus Mahasiswa")
    print("6. Keluar")

def input_daftar_nilai():
    while True:
        nilai = input("Masukkan daftar nilai: ")
        try:
            potongan = nilai.split(",")
            daftar_nilai = []
            for item in potongan:
                angka = int(item)
                daftar_nilai.append(angka)
            return daftar_nilai
        except ValueError:
            print("Mohon masukkan angka untuk daftar nilai.")

def menu_tambah(manager):
    print("\n=== TAMBAH MAHASISWA ===")
    nama = input("Masukkan nama mahasiswa: ")
    while True:
        nim = input("Masukkan NIM mahasiswa: ")
        if manager.cari_mahasiswa(nim) is not None:
            print("NIM sudah digunakan, silahkan gunakan NIM lain.")
        else:
            break
    daftar_nilai = input_daftar_nilai()
    mahasiswa = Student(nama, nim, daftar_nilai)
    manager.tambah_mahasiswa(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan!")

def menu_tampilkan_semua(manager):
    print("\n=== DATA SEMUA MAHASISWA ===")
    manager.tampilkan_semua()

def menu_cari(manager):
    print("\n=== CARI MAHASISWA ===")
    nim = input("Masukkan NIM yang dicari: ")
    mahasiswa = manager.cari_mahasiswa(nim)
    if mahasiswa is None:
        print("Data mahasiswa tidak ditemukan.")
    else:
        print("Data ditemukan!")
        print(mahasiswa)

def menu_edit(manager):
    print("\n=== EDIT DATA MAHASISWA ===")
    nim = input("Masukkan NIM mahasiswa: ")
    if manager.cari_mahasiswa(nim) is None:
        print("Data mahasiswa tidak ditemukan.")
    else:
        nama_baru = input("Masukkan nama mahasiswa: ")
        daftar_nilai_baru = input_daftar_nilai()
        manager.edit_mahasiswa(nim, nama_baru, daftar_nilai_baru)
        print("Data mahasiswa berhasil diubah!")

def menu_hapus(manager):
    print("\n=== HAPUS DATA MAHASISWA ===")
    nim = input("Masukkan NIM data yang ingin dihapus: ")
    mahasiswa = manager.cari_mahasiswa(nim)
    if mahasiswa is None:
        print("Data mahasiswa tidak ditemukan.")
    else:
        print("Data ditemukan!")
        print(mahasiswa)
        konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ")
        if konfirmasi.lower() == "y":
            manager.hapus_mahasiswa(nim)
            print("Data mahasiswa berhasil dihapus!")
        else:
            print("Data mahasiswa batal dihapus.")

def menu_exit():
    print("\n=== KELUAR ===")
    print("Terima kasih telah menggunakan program kami!")

# ===== 3. MAIN (pengatur alur) ===== #
def main():
    manager = StudentManager()
    while True:
        tampilkan_menu()
        opsi_menu = input("Pilih Menu: ")
        
        if opsi_menu == "1":
            menu_tambah(manager)
        elif opsi_menu == "2":
            menu_tampilkan_semua(manager)
        elif opsi_menu == "3":
            menu_cari(manager)
        elif opsi_menu == "4":
            menu_edit(manager)
        elif opsi_menu == "5":
            menu_hapus(manager)
        elif opsi_menu == "6":
            menu_exit()
            break
        else:
            print("Pilihan tidak valid!")

# ===== 4. JALANKAN PROGRAM ===== #
if __name__ == "__main__":
    main()