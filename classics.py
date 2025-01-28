class Student():
    def __init__(self,name,age,major):
        self.name = name
        self.age = age
        self.major = major
        
    def create_student(self):
        print(f"Hi guys, my name is {self.name} and I am {self.age} years old")
        
    def academics(self):
        print (f"I am taking {self.major}")


Muut = Student("Muthaka",23,"ACS")
Muut.create_student()
Muut.academics()