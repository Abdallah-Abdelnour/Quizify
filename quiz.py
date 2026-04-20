"""
Module quiz.py
"""

import time
from datetime import datetime
from user import sauvegarder_score
# from bonus.timer import demander_reponse_avec_timer, input_propre
from bonus.api import charger_questions_api_ou_locale
from bonus.scoreboard import ajouter_scoreboard
from bonus.timer import demander_reponse_avec_timer, input_propre

class Question:
    """
    Représente une question du quiz
    """

    def __init__(self, question_data):
        self.id = question_data["id"]
        self.theme = question_data["theme"]
        self.question = question_data["question"]
        self.options = question_data["options"]
        self.reponse = question_data["reponse"]

    def verifier_reponse(self, reponse_utilisateur):
        """
        Vérifie si la réponse est correcte
        """
        if reponse_utilisateur is None:
            return False
        return (
            reponse_utilisateur.strip().lower() ==
            self.reponse.strip().lower()
        )


class Quiz:
    """
    Représente un quiz pour user
    """

    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur
        self.questions = []
        # self.questions =
        # [Question(q) for q in charger_questions_api_ou_locale()]

    def choisir_theme(self):
        """
        Choisir le thème du quiz
        """
        print("\nChoisissez un thème :")
        print("1. Python")
        print("2. Histoire")

        while True:
            choix = input_propre("Entrez le numéro du thème : ")
            if choix in ["1", "2"]:
                return choix
            else:
                print("Choix invalide. Veuillez réessayer.")

    def filtrer_questions_par_theme(self, theme_choisi):
        """
        Retourne les questions du thème choisi
        """
        if theme_choisi == "1":
            return [q for q in self.questions if q.theme == "Python"], "Python"
        elif theme_choisi == "2":
            return [
                q for q in self.questions
                if q.theme == "Histoire"
            ], "Histoire"
        return [], ""

    def jouer(self):
        """
        Lance une partie de quiz
        """
        print("Chargement des questions...")
        self.questions = [
            Question(q) for q in charger_questions_api_ou_locale()
        ]

        theme_choisi = self.choisir_theme()
        # theme_txt ==> soit "Python" soit "Histoire" soit ""
        questions_theme, theme_txt = self.filtrer_questions_par_theme(
            theme_choisi
        )

        if not questions_theme:
            print("Aucune question trouvée pour ce thème.")
            return

        score = 0

        for idx, question in enumerate(questions_theme, start=1):
            reponse_utilisateur = demander_reponse_avec_timer(
                question=question.question,
                options=question.options,
                temps=15,
                numero=idx
            )

            if reponse_utilisateur is None:
                print(f"La bonne réponse était : {question.reponse}")
            elif question.verifier_reponse(reponse_utilisateur):
                print(" Bonne réponse !")
                score += 1
            else:
                print(
                    " Mauvaise réponse ! "
                    f"La bonne réponse était : {question.reponse}"
                )

            time.sleep(2)

        print("\n=== RÉSULTAT FINAL ===")
        print(
            f"Votre score final est : "
            f"{score * 10}/{len(questions_theme) * 10}"
        )

        result = {
            self.nom_utilisateur: {
                "scores": [
                    {
                        "theme": theme_txt,
                        "score": score * 10,
                        "date": datetime.now().strftime("%Y-%m-%d")
                    }
                ]
            }
        }

        sauvegarder_score(self.nom_utilisateur, result)
        ajouter_scoreboard(
            utilisateur=self.nom_utilisateur,
            theme=theme_txt,
            score=score * 10,
            date=datetime.now().strftime("%Y-%m-%d")
        )
