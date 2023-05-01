print("Funkcja")

def funkcja_test():
    print("Funkcja....")
funkcja_test()

def dodaj(x):
    print(x+1)
dodaj(2)

def dodaj(x, y):
    print(x + y)
dodaj(2, 3)

def dodaj(x, y=1, z=0):
    print(x + y + z)
dodaj(2, 3)
dodaj(2)
dodaj(2, 3, 5)

def dodaj(x, y=1, z=0):
    return x + y + z
print(dodaj(2, 3))
print(dodaj(2))
wynik = dodaj(2, 3, 5)
print(wynik)

def dodaj(x):
    print(x+1)
zmienna = dodaj(2)
print(zmienna)

def dodaj(x, y=1, z=0):
    print("Czy ja istnieje?")
    return x + y +z
