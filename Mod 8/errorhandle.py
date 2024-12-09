n1 = input("enter a number ")
n1 = int(n1)
n2 = input("enter annother number ")
n2 = int(n2)
try:
    print(n1/n2)
except ZeroDivisionError:
    print("can not enter a zero. enter a non-zero number")
except ValueError:
    print("enter number only!")
except TypeError:
    print("Error!! please contact the programmer")
