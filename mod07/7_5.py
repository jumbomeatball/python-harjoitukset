def jako(lista):
    uusi_lista = []
    for num in (lista):
      if num % 2 == 0:
        uusi_lista.append(num)
    return uusi_lista
lista = [1, 2, 3, 4, 5]
uusi = jako(lista)
print(lista)
print(uusi)