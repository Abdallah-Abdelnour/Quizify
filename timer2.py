"""
Gestion du scoreboard global en CSV
"""

import csv
import os


BASE_DIR = os.path.dirname(__file__)
SCOREBOARD_PATH = os.path.join(BASE_DIR, "scoreboard.csv")


def initialiser_scoreboard():
    """
    Crée le fichier scoreboard.csv s'il n'existe pas
    """
    if not os.path.exists(SCOREBOARD_PATH):
        with open(SCOREBOARD_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Utilisateur", "Theme", "Score", "Date"])


def ajouter_scoreboard(utilisateur, theme, score, date):
    """
    Ajoute une ligne dans le scoreboard CSV
    """
    initialiser_scoreboard()

    with open(SCOREBOARD_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([utilisateur, theme, score, date])


def lire_scoreboard():
    """
    Lit le scoreboard et retourne les lignes
    """
    initialiser_scoreboard()

    scores = []
    with open(SCOREBOARD_PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            ligne["Score"] = int(ligne["Score"])
            scores.append(ligne)

    return scores


def afficher_scoreboard():
    """
    Affiche le classement global trié par score décroissant
    """
    scores = lire_scoreboard()

    if not scores:
        print("Aucun score dans le classement global.")
        return

    scores_tries = sorted(scores, key=lambda x: x["Score"], reverse=True)

    print("\n===== CLASSEMENT GLOBAL =====")
    print(
        f"{'Rang':<5} {'Utilisateur':<15} {'Thème':<12} {'Score':<8} {'Date'}"
    )
    print("-" * 55)

    for i, s in enumerate(scores_tries, start=1):
        print(
           f"{i:<5} {s['Utilisateur']:<15} "
           f"{s['Theme']:<12} {s['Score']:<8} {s['Date']}"
        )
