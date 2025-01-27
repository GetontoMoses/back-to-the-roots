orders = [
    "Bently",
    "Range Rover",
    "Mercedes",
    "Toyota",
    "Bently",
    "Bently",
    "Subaru",
]
print("Unfortunately we are out of Bently's")

while "Bently" in orders:
    orders.remove("Bently")
    
print("This is what we have instead: ")
for cars in orders:
    print(cars)