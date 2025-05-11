class car:
    model = "Porsche"
    year = 2023
    color = "red"

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

car1 = car("Porsche", 2023, "red")
car2 = car("BMW", 2022, "blue")

print(car1.model)
print(car2.year)