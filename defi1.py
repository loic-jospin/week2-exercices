multiples = []
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

for i in range(1, length + 1):
    resultat=number*i
    multiples.append(resultat)

print(multiples)
