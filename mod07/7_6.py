from math import pi
def pizza(num, hinta):
    m = num / 100
    h = m / 2
    p = pi*(h*h)
    c = hinta / p
    f = round (c, 2)
    return f
num = float (input("Syötä halkaisija: "))
hinta = float (input("Syötä hinta: "))
pizza1 = pizza(num, hinta)
num = float (input("Syötä seuraava halkaisija: "))
hinta = float (input("Syötä seuraavahinta: "))
pizza2 = pizza(num, hinta)
if pizza1 < pizza2:
    print (f"Ensimmäinen pizza on edullisempi")
elif pizza1 > pizza2:
    print (f"Toinen pizza on edullisempi")
else:
    print (f"Pizzat ovat yhtä edullisia")