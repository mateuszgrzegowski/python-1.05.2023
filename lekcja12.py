x = 12
y = 0

try:
    lista = []
    print(lista[0])
    print (x + "!")
    print(x / y)
    print("Linijka po")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Inny błąd!")
finally:
    print("FINALLY wykonam się i tak!")

print("Dalsze instrukcje ...")