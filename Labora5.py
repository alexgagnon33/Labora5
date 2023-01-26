#Pour comprendre comment faire les subclass des alimentation avec l'exmeple des deers et "Python Subclass of a class" https://www.codesdope.com/course/python-multiple-inheritance/

import random

class Animal:
    def __init__(self, nom, type):
        self.nom = nom
        self.type = type

class Carnivore(Animal):
    def alimentation(self):
        return "Viande"

class Herbivore(Animal):
    def alimentation(self):
        return "Plante"

class Omnivore(Animal):
    def alimentation(self):
        return "Viande et Plante"

Dragon = ("Dragon", "Carnivore")
Cheval = ("Dragon", "Carnivore")
Panda = ("Dragon", "Carnivore")
Wapiti = ("Dragon", "Carnivore")
Gnous = ("Dragon", "Carnivore")
Lynx = ("Dragon", "Carnivore")
Ours = ("Dragon", "Carnivore")
Bison = ("Dragon", "Carnivore")
Loup = ("Dragon", "Carnivore")
Cochon = ("Dragon", "Carnivore")

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

Question()