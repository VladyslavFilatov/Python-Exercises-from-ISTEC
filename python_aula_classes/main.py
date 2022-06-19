class Person:
    def __init__(self, name, lastname, age=None):
        self.fname = name
        self.lname = lastname
        self.age = age

    def bom(self, hora):
#        print(f"Bom/a {hora} {self.fname} {self.lname}")
        print(f"Bom/a {hora} {self.fname} {self.lname}, {self.age}")



class Student(Person):
    def __init__(self, tel, *args, **kwargs):
        self.tel = tel
        super().__init__(*args, **kwargs)


#s1 = Student("91234", "Zé", "Paredes")
#s1 = Student("91234", name="Zé", lastname="Paredes")
#s1 = Student("91234", "Zé", lastname="Paredes")
s1 = Student("91234", "Zé", lastname="Paredes", age=10)


print(s1.fname)
print(s1.lname)
s1.bom("dia")