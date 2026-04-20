"""
Module main.py
"""

from quiz import Quiz
from user import demander_nom_utilisateur, afficher_resultats
from bonus.timer import input_propre
from bonus.scoreboard import afficher_scoreboard


def main():
    """
    Fonction principale
    """
    nom = demander_nom_utilisateur()
    quiz = Quiz(nom)

    while True:
        print("\n=== MENU QUIZ ===")
        print("1. Jouer")
        print("2. Voir les résultats")
        print("3. Voir le classement global")
        print("4. Quitter")

        choix = input_propre("Choisissez une option : ")

        if choix == "1":
            quiz.jouer()
        elif choix == "2":
            afficher_resultats(nom)
        elif choix == "3":
            afficher_scoreboard()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


main()
