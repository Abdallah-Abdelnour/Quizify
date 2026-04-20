"""
Gestion des questions via une API externe
"""

import requests
from utils import charger_questions


# Remplace ce lien par TON vrai lien RAW GitHub
URL_QUESTIONS = (
    "https://raw.githubusercontent.com/"
    "Abdallah-Abdelnour/questions/main/questions.json"
)


def recuperer_questions_depuis_api():
    """
    Récupère les questions depuis une API externe (GitHub RAW)
    Retourne une liste de questions si succès, sinon None
    """
    try:
        response = requests.get(URL_QUESTIONS, timeout=5)
        response.raise_for_status()

        questions = response.json()

        if isinstance(questions, list):
            print("Questions chargées depuis l'API externe.")
            return questions

        print("Format JSON invalide depuis l'API.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Erreur API : {e}")
        return None


def charger_questions_api_ou_locale():
    """
    Essaie de charger les questions depuis l'API.
    Si échec, charge le fichier local.
    """
    questions_api = recuperer_questions_depuis_api()

    if questions_api:
        return questions_api

    print("Chargement des questions locales...")
    return charger_questions()
