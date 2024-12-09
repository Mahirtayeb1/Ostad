class Maths:
    t = "Tayeb works for Google as a Data Scientist"
    def add(self, a, b):
        return a+b
    def substract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b
    def testsub(self):
        print(self.substract(120, 40))

m1 = Maths()
m1.testsub()
# n1 = Maths()
# print("Instances of m1 ")
# print(m1.add(10,5))
# print(m1.t)
# print("Instances of n1 ")
# print(n1.multiply(20,5))

class Person:
    def __init__(self, s):
        self.name = s
    
    def hello(self):
        print("hello", self.name)
    def hellow(self, age):
        print("hellow", self.name, "! Is your age", age, "?")

t = Person("Mahir")
t.hello()
t.hellow(24)
# print(t.hello())