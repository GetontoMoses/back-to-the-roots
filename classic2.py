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
        
        self.color = "black"
        
    def what_color(self):
        print(f"{self.name} is {self.color} in color")
        
my_doug = Escobar("bravo",23)
my_doug.roll_over()
my_doug.what_color()