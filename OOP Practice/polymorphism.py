class Student:
    def aktivitas(self):
        print("Saya sedang belajar.")

class Lecturer:
    def aktivitas(self):
        print("Saya sedang mengajar.")

class Programmer:
    def aktivitas(self):
        print("Saya sedang menulis kode.")

def jalankan_aktivitas(person):
    person.aktivitas()

student1 = Student()
lecturer1 = Lecturer()
programmer1 = Programmer()

jalankan_aktivitas(student1)
jalankan_aktivitas(lecturer1)
jalankan_aktivitas(programmer1)