class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

c1 = Car("Tata Motors", "Jaguar F-Pace", 2024)
c2 = Car("Tata Motors", "Range Rover", 2023)

print(c1.make, c1.model, c1.year)
print(c2.make, c2.model, c2.year)