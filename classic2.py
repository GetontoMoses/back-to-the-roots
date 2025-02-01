class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def roll_over(self):
        print(f"{self.name} is rolling over")
        
    def sit(self):
        print(f"{self.name} is now sitted")
        
class Escobar(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        
my_doug = Dog("bravo",23)
my_doug.roll_over()