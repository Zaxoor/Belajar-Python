import operations as op

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            break
        except ValueError:
            print("Input must be a number.\nPlease try again.")
    return angka

def output(angka_pertama, angka_kedua):
    hasil_penjumlahan = op.penjumlahan(angka_pertama, angka_kedua)
    hasil_pengurangan = op.pengurangan(angka_pertama, angka_kedua)
    hasil_perkalian = op.perkalian(angka_pertama, angka_kedua)
    hasil_pembagian = op.pembagian(angka_pertama, angka_kedua)
    
    print("\n==== CALCULATOR ====")
    print(f"Addition : {hasil_penjumlahan}")
    print(f"Substraction : {hasil_pengurangan}")
    print(f"Multiplication : {hasil_perkalian}")
    print(f"Division : {hasil_pembagian}")

angka_pertama = input_angka("Input first number: ")
angka_kedua = input_angka("Input second number: ")
output(angka_pertama, angka_kedua)