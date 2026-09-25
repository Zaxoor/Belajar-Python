contacts = [
    {
        "nama": "Hasbi",
        "nomor": "081234567890",
        "email": "hasbi@email.com"
    },
    {
        "nama": "Arina",
        "nomor": "081122223333",
        "email": "arina@email.com"
    },
    {
        "nama": "Ikvina",
        "nomor": "080987654321",
        "email": "ikvina@email.com"
    }
]

for nomor, contact in enumerate(contacts, start=1):
    print(f"{nomor}, {contact['nama']}")
    print(f"   Nomor: {contact['nomor']}")
    print(f"   Email: {contact['email']}")
    print("")