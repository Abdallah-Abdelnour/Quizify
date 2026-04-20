"""
Fonctions utilitaires
"""

import json
import os


BASE_DIR = os.path.dirname(__file__)
QUESTIONS_PATH = os.path.join(BASE_DIR, "data", "questions.json")
USERS_PATH = os.path.join(BASE_DIR, "data", "utilisateurs.json")


def charger_questions():
    """
    Charger les questions depuis le fichier JSON
    """
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def charger_utilisateurs():
    """
    Charger les utilisateurs depuis le fichier JSON
    """
    if os.path.exists(USERS_PATH) and os.path.getsize(USERS_PATH) > 0:
        with open(USERS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def sauvegarder_utilisateurs(data):
    """
    Sauvegarder les utilisateurs dans le fichier JSON
    """
    with open(USERS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
