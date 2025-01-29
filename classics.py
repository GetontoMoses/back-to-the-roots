class Student():
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major
        
    def create_student(self):
        print(f"Hi guys, my name is {self.name} and I am {self.age} years old")
        
    def academics(self):
        print (f"I am taking {self.major}")


class Senior(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age, major)
        
        super().__init__(self,name,age,major)
        self.State_status="senior"

    def student_status(self):
        print("I am a senior student")

Muut = Student("Muthaka", 23, "ACS")
Muut.create_student()
Muut.academics()
Muut.student_status()