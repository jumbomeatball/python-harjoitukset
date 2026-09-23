käyttäjätunnus = "python"
salasana = "rules"
yritykset = 0

while yritykset < 5:
    syötetty_tunnus = input("Anna käyttäjätunnus: ")
    syötetty_salasana = input("Anna salasana: ")

    if syötetty_tunnus == käyttäjätunnus and syötetty_salasana == salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print(f"Väärä käyttäjätunnus tai salasana. Yrityksiä jäljellä: {5 - yritykset}")

if yritykset == 5:
    print("Pääsy evätty.")