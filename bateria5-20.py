# Fes un programa com l'anterior que mostra el valor màxim i mínim de la llista.
llista=[]
while True:
    num = input("Introdueix un número: ")
    if num == "final":
        break
    else:
        llista.append(int(num))
llista.sort()
print("El mínim valor és: ", llista[0])
print("El màxim valor és: ", llista[-1])
