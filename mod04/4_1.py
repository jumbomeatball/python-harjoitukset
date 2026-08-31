kuha = input("Mikä on kuhan pituus senttimetreinä? ")
print(f"Kuhan pituus on {kuha} senttimetriä.")

if int(kuha) < 37:
    print("Kuhan pituus on alle 37 cm, joten se on alamittainen. Laske kuha takaisin järveen.")
    print(f"Kuhan pituus on {37 - int(kuha)} senttimetriä alimmasta sallitusta pyyntimitasta.")
