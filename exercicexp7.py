fruits=input("entrez vos fruits préféré en les séparé d'un espace :")
list_fruit=fruits.split()
x=input("entrez le nom d'un fruit: ")
if x in list_fruit:
    print("vous avez choisi", x, "l'un de vos fruit préféré.")
else:
    print("vous avez choisi", x, "un nouveau fruit j'espere que tu apprécies.")    
