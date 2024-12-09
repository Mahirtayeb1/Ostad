# lambda argument : expression

def greet(name):
    return "hello " + name
print(greet("tayeb"))


greeting = lambda name : "from inside lambda function, hello " + name
print(greeting("tayeb"))

numbers = [1,2,3,4]
double_number = list(map(lambda num : num*2, numbers))
print(double_number)