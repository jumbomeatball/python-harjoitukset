def summa(lista):
    y = sum(lista)
    return y
lista = [1, 2, 3, 4]
num = 0
while num != "":
    try:
        num = int(input("Syötä seuraava kokonaisluku: "))
        lista.append(num)
    except ValueError:
       break
print(summa(lista))

#tietotyypit ??? näil on tietotyypit