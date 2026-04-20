"""
Module user.py
"""

from utils import charger_utilisateurs, sauvegarder_utilisateurs
from bonus.timer import input_propre


def demander_nom_utilisateur():
    """
    Demande le nom de l'utilisateur
    """
    input("Press Enter to start...")
    while True:
        nom = input_propre("Entrer votre nom : ")
        if nom == "":
            print("Nom invalide. Veuillez réessayer.")
        else:
            print(f"Bonjour {nom} !")
            return nom


def sauvegarder_score(nom, result):
    """
    Sauvegarder le score dans utilisateurs.json
    """
    data = charger_utilisateurs()

    if nom in data:
        data[nom]["scores"].extend(result[nom]["scores"])
    else:
        data.update(result)

    sauvegarder_utilisateurs(data)
    print(" Score sauvegardé avec succès !")


def afficher_resultats(nom):
    """
    Affiche les résultats d'un utilisateur
    """
    data = charger_utilisateurs()

    if not data:
        print(" Aucun résultat enregistré.")
        return

    if nom not in data:
        print(f" Aucun résultat trouvé pour '{nom}'.")
        return

    print(f"\n===== RÉSULTATS DE {nom} =====")
    for s in data[nom]["scores"]:
        print(
            f"Thème : {s['theme']} | Score : {s['score']} | Date : {s['date']}"
        )
