import json

# on ouvre un fichier avec "with open...."
# On peut ensuite livre le contenue du fichier avec la méthode .read()
with open("produit_a_vendre.json", "r") as fichier_json :
    fichier_lu = fichier_json.read()

# Pour convertir la chaine de caractères en objet Python, on utilise le module json
produit = json.loads(fichier_lu)


# Imprimer le prix du produit 


# Modifier le prix


# Pour écrire dans un fichier json,
#       on ouvre d'abord le fichier avec un "with open( ....."
#       on convertit l'objet Python en une chaine de caractères
#       on peut ensuite écrire le str dans le fichier.
with open("produit2.json", "w") as fichier :
       chaine_format_json = json.dumps(produit,indent=4)
       fichier.write(chaine_format_json)

print()