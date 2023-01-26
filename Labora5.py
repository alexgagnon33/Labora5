#Montrer tous les animaux avec leur nutrition

import random

class Animal:
    def __init__(self, alimentation, nom, type):
        self.alimentation = alimentation
        self.nom = nom
        self.type = type

Dragon = ("Viande", "Dragon", "Carnivore")
Cheval = ("Herbivore", "Dragon", "Carnivore")
Panda = ("Omnivore", "Dragon", "Carnivore")
Wapiti = ("Omnivore", "Dragon", "Carnivore")
Gnous = ("Herbivore", "Dragon", "Carnivore")
Lynx = ("Viande", "Dragon", "Carnivore")
Ours = ("Omnivore", "Dragon", "Carnivore")
Bison = ("Herbivore", "Dragon", "Carnivore")
Loup = ("Viande", "Dragon", "Carnivore")
Cochon = ("Omnivore", "Dragon", "Carnivore")

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
        réponse_question1 = print(int("Quel type d'animaux est" + animal_random.nom )) 
        if réponse_question1 == animal_random.type:
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")

def Question2():
    for animal_random in animaux_liste:
        print(animal_random.nom + animal_random.alimentation)
