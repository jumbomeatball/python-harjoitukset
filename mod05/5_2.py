done = False
while (done == False):
    tuuma = input("Anna luku tuumina: ")
    if float(tuuma) < 0:
        print("Ohjelma päättyy.")
        done  = True
    else:
        sentit = float(tuuma) * 2.54
        print(sentit, "senttimetriä")