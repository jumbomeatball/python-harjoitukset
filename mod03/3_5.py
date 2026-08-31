leiviskat = int(input("Leiviskat: "))
naulat = int(input("Naulat: "))
luodit = float(input("Luodit: "))

naulat = leiviskat * 20 + naulat
luodit = naulat * 32 + luodit
grammat = luodit * 13.3

kilot = int(grammat // 1000)
grammat = round(grammat % 1000, 2)

print("Massa nykymittojen mukaan: \n "+ str(kilot) + " kilogrammaa ja " + str(grammat) + " grammaa.")