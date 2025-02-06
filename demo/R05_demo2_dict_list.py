# Trois dictionnaires ayant les mêmes clefs
voiture1 =  {"marque":"Ford", "modele":"Escape", "annee": 2018,"kilometrage":150020,"accessoires":["dés en minou","gros muffler"]}
voiture2 = {"marque":"toyota", "modele":"Camry","annee": 2005,"kilometrage":200000,"accessoires":[]}
voiture3 = {"marque":"toyota","modele":"Corolla","annee": 2015,"kilometrage":138000}

# On peut faire une liste contennant les trois variables
# On aurait pu aussi crée une seule variable contenant une liste des trois dictionnaires.
voitures = [voiture1,voiture2,voiture3]
voitures_2 = []


# Impression de toutes les paires de clef et valeurs
for auto in voitures :
    print("Les paires clef: valeurs sont :")
    for clefs, valeur in auto.items():
        print(f"        clef : {clefs}  Valeur : {valeur}")
