question_1 = {
    "soal": "Apa ibukota negara Indonesia?",
    "pilihan": ["Jakarta","Bandung", "Surabaya", "Medan"],
    "jawaban": "Jakarta"
}

question_2 = {
    "soal": "Berapa biji Prabowo?",
    "pilihan": ["1", "2", "3", "4", "5"],
    "jawaban": "1"
}

question_3 = {
    "soal": "Berapa lama Jokowi menjabat?",
    "pilihan": ["1", "2", "3"],
    "jawaban": "2"
}

question_4 = {
    "soal": "Apa kalimat ikonik Jokowi?",
    "pilihan": ["Saya akan lawan!", "YNTKTS"],
    "jawaban": "Saya akan lawan!"
}

question_5 = {
    "soal": "Lebih gantengan mana?",
    "pilihan": ["Hasbi", "Cortis"],
    "jawaban": "Hasbi"
}

Dictionary =[
    question_1, question_2, question_3, question_4, question_5
]
running = True
while running:
    print("")
    print("==== QUIZ ====")
    print("Selamat datang di Quiz Game!")
    print("1. Mulai Quiz")
    print("2. Tutorial")
    print("3. Keluar")
    print("")
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "3":
        print("")
        print("==== KELUAR ====")
        print("Terima kasih telah bermain!")
        print("")
        running = False
    elif choice == "2":
        print("")
        print("==== TUTORIAL ====")
        print("1. Pilih 'Mulai Quiz' untuk memulai permainan.")
        print("2. Setiap pertanyaan memiliki beberapa pilihan jawaban.")
        print("3. Pilih jawaban yang benar dengan mengetikkan pilihan yang sesuai.")
        print("4. Setelah menjawab semua pertanyaan, skor Anda akan ditampilkan.")
        print("")
        print("Selamat bermain!")
        print("")
    elif choice == "1":
        print("")
        print("==== MULAI QUIZ ====")
        print("Jawablah pertanyaan berikut dengan mengetikkan pilihan yang sesuai.")
        print("")
        skor = 0
        for i, question in enumerate(Dictionary, start=1):
            print(f"==== Pertanyaan {i} ====")
            print(f"Pertanyaan {i}: {question['soal']}")
            for i, option in enumerate(question['pilihan'], start=1):
                print(f"{i}. {option}")
            answer = input("Masukkan jawaban Anda (1/2/3/...): ")
            if answer == "1":
                print("")
                print("Jawaban Anda benar!")
                skor += 1
                print(f"Skor sementara: {skor}/{len(Dictionary)}")
                print("")
            else:
                print("")
                print("Jawaban Anda salah!")
                print(f"Jawaban yang benar adalah: {question['jawaban']}")
                print(f"Skor sementara: {skor}/{len(Dictionary)}")
                print("")
        print("")
        print("==== HASIL QUIZ ====")
        print("Selamat! Anda telah menyelesaikan quiz.")
        print(f"Total skor: {skor}/{len(Dictionary)}")
