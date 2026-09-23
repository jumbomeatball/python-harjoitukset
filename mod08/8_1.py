kuukauden_numero = int(input("Anna kuukauden numero: "))
kevät = [3, 4, 5]
kesä = [6, 7, 8]
syksy = [9, 10, 11]
talvi = [12, 1, 2]
if kuukauden_numero in kevät:
    print("Kuukausi kuuluu kevääseen.")
elif kuukauden_numero in kesä:
    print("Kuukausi kuuluu kesään.")
elif kuukauden_numero in syksy:
    print("Kuukausi kuuluu syksyyn.")
else:
    print("Kuukausi kuuluu talveen.")