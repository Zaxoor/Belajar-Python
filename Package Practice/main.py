from matematika import penjumlahan, perkalian, pengurangan

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            break
        except ValueError:
            print("Invalid input, input must be a number.")
    return angka

angka_pertama = input_angka("Input the first number : ")
angka_kedua = input_angka("Input the second number : ")

hasil_penjumlahan = penjumlahan.tambah(angka_pertama, angka_kedua)
hasil_perkalian = perkalian.kali(angka_pertama, angka_kedua)
hasil_pengurangan = pengurangan.kurang(angka_pertama, angka_kedua)

print(f"\nAddition : {hasil_penjumlahan}")
print(f"Multiplication : {hasil_perkalian}")
print(f"Substraction : {hasil_pengurangan}")