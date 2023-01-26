#Je dois trouver une façon de random la liste d'une classe puis de poser la question et la réponse
#Montrer tous les animaux avec leur nutrition



class Animal:
    def __init__(self, nom, type):
        self.nom = nom
        self.type = type

menu = {1 : "Viande",
        2: "Plante",
        3: "Viande et Plante"}

Dragon = (1, "Dragon", "Carnivore")
Cheval = (2, "Dragon", "Carnivore")
Panda = (3, "Dragon", "Carnivore")
Wapiti = (3, "Dragon", "Carnivore")
Gnous = (2, "Dragon", "Carnivore")
Lynx = (1, "Dragon", "Carnivore")
Ours = (3, "Dragon", "Carnivore")
Bison = (2, "Dragon", "Carnivore")
Loup = (1, "Dragon", "Carnivore")
Cochon = (3, "Dragon", "Carnivore")

animaux_liste = [Dragon, Cheval, Panda, Wapiti, Gnous, Lynx, Ours, Bison, Loup, Cochon]

def Question():
    while True:
        print("Choisez le bon type d'animaux dans la liste")
        print("Voir ce que mange tous les animaux dans la liste")
        réponse_utilisateur = print(int("Choisisez une question: "))
        if réponse_utilisateur == 1:
            pass
        elif réponse_utilisateur == 2:
            pass
        else:
            print("Votre réponse est mauvaise, choisisez une autre réponse")
            False

def Question1():