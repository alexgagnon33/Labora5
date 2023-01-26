#Montrer tous les animaux avec leur nutrition

import random

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
        animal_random = random.choice(animaux_liste)
        réponse_question1 = print(int("Quel type d'animaux est" + animal_random )) 
        if réponse_question1 == animal_random:
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")

def Question2():
    for animal_random in animaux_liste:
        print(animal_random + animal_random)
