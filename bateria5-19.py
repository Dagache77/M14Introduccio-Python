# Fes un programa que pregunta valors de números sencers a l'usuari i els guarda en una llista fins que l'usuari introdueix la paraula final, i després torna la suma de tots els números introduïts.
llista=[]
while True:
    num = input("Introdueix un número: ")
    if num == "final":
        break
    else:
        llista.append(int(num))
resultat = 0
print(llista)
for i in llista:
    resultat = resultat + i
print ("El resultat és: ", resultat)
