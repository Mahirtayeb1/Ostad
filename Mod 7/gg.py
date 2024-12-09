def add(a, b):
    print(f"Adding {a} + {b} ")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b} ")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b} ")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b} ")
    return a / b

print(f"= {add(30, 10)}")
print(f"= {subtract(30, 10)}")
print(f"= {multiply(30, 10)}")
print(f"= {divide(30, 10)}")
print(f"= {int(divide(30, 10))}")

print(0b1011010, ord('Z'), chr(90))

def sorted_words(words):
    return sorted(words)
    
def break_words(word):
    words = word.split(" ")
    return words
print(break_words("coder from Amazon"))

def print_1st_word(word):
    words = word.pop(0)
    return words

def print_last_word(word):
    words = word.pop(-1)
    return words
def print_1st_last_sentence(sentence):
    sen = break_words(sentence)
    fword = print_1st_word(sen)
    lword = print_last_word(sen)
    return fword, lword


print(print_1st_word(['job', 'coder', 'Amazon', 'Google', 'Apple']))
print(print_last_word(['job', 'coder', 'Amazon', 'Google', 'Apple']))
print(sorted_words("fiyeggeakjw"))
print(print_1st_last_sentence('Mahir is a ML engineer who works at Google'))




from sys import argv
script, inp_file = argv

