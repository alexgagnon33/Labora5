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

Dragon = Carnivore("Dragon", "Carnivore")
Cheval = Herbivore("Cheval", "Herbivore")
Panda = Omnivore("Panda", "Omnivore")
Wapiti = Omnivore("Wapiti", "Omnivore")
Gnous = Herbivore("Gnous", "Herbivore")
Lynx = Carnivore("Lynx", "Carnivore")
Ours = Omnivore("Ours", "Omnivore")
Bison = Herbivore("Bison", "Herbivore")
Loup = Carnivore("Loup", "Carnivore")
Cochon = Omnivore("Cochon", "Omnivore")

animaux_liste = [Dragon, Cheval, Panda, Wapiti, Gnous, Lynx, Ours, Bison, Loup, Cochon]

def Question():
    while True:
        print("Choisez le bon type d'animaux dans la liste")
        print("Voir ce que mange tous les animaux dans la liste")
        réponse_utilisateur = input("Choisisez une question: ")
        if réponse_utilisateur == "1":
            Question1()
        elif réponse_utilisateur == "2":
            Question2()
        else:
            print("Votre réponse est mauvaise, choisisez une autre réponse")

def Question1():
        animal_random = random.choice(animaux_liste)
        réponse_question1 = input("Quel type d'animaux est le/la/l' " + animal_random.nom )
        if réponse_question1 == animal_random.type:
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")

def Question2():
    for animal_random in animaux_liste:
        print("Animal    Alimentation")
        print(animal_random.nom + "  |  " + animal_random.alimentation())

Question()