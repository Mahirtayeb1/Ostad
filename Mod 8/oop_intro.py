class Car:
    kind = "SUV"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def update_odometer(self, odo):
        if odo > self.odometer:
            self.odometer = odo
        else:
            print("Cannot update odometer")

    def __str__(self):
        return "The Car is {} {} and Year: {}".format(self.make, self.model, self.year)
    
    def __eq__(self, value):
        if  self.make == value.make and self.model == value.model and self.year == value.year:
            return "Both the Cars are same"
        else:
            return "The Cars are not same"
    

c1 = Car("Tata Motors", "Jaguar F-Pace", 2024)
c2 = Car("Tata Motors", "Range Rover", 2023)
c3 = Car("Tata Motors", "Jaguar F-Pace", 2024)

print(c1)
#print(c2.make, c2.model, c2.year)
print(c2)
c2.update_odometer(50)
print(c2.odometer)
c2.update_odometer(20)
print(c2.odometer)
print(c1 == c3)

print(Car.update_odometer)

class Complex:
    def __init__(self, realpart, imaginepart):
        self.rp = realpart
        self.ip = imaginepart

x = Complex(30, -4.5)
print(x.rp, x.ip)


class Dog:
    #tricks = []     # will print for all instances. To use it specifically for a particuler object we need to 
                     # use it in the constructor.

    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Messi")
e = Dog('Rashford')

d.add_trick("play with the ball")
print(d.tricks)
print(e.tricks)