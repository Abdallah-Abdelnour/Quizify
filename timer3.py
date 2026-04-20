"""
Module timer.py
"""

import os
import sys
import time

if os.name == "nt":
    import msvcrt
else:
    import select
    import termios
    import tty


def vider_buffer_clavier():
    """
    Vide les touches restantes dans le buffer clavier.
    Compatible Windows/Linux.
    """
    if os.name == "nt":
        while msvcrt.kbhit():
            msvcrt.getwch()


def input_propre(message=""):
    """
    Vide le buffer clavier avant un input classique.
    """
    vider_buffer_clavier()
    return input(message).strip()


def lire_touche_linux():
    """
    Lit une touche sur Linux sans bloquer.
    Retourne None si aucune touche n'est pressée.
    """
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)
    return None


def demander_reponse_avec_timer(question, options, temps=15, numero=1):
    """
    Affiche une question avec un timer interactif.
    Compatible Windows et Linux.
    """
    reponse = ""
    debut = time.time()
    dernier_restant = None
    ancienne_reponse = None

    vider_buffer_clavier()

    fd = None
    ancien_terminal = None

    if os.name != "nt":
        fd = sys.stdin.fileno()
        ancien_terminal = termios.tcgetattr(fd)
        tty.setcbreak(fd)

    try:
        while True:
            ecoule = int(time.time() - debut)
            restant = temps - ecoule

            if restant < 0:
                print("\nTemps écoulé !")
                time.sleep(0.2)
                vider_buffer_clavier()
                return None

            if restant != dernier_restant or reponse != ancienne_reponse:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Temps restant : {restant}s")
                print(f"Question {numero}: {question}")
                for i, option in enumerate(options, start=1):
                    print(f"{i}. {option}")
                print(f"Votre réponse : {reponse}", end="", flush=True)

                dernier_restant = restant
                ancienne_reponse = reponse

            touche = None

            if os.name == "nt":
                if msvcrt.kbhit():
                    touche = msvcrt.getwch()
            else:
                touche = lire_touche_linux()

            if touche:
                # Entrée
                if touche in ("\r", "\n"):
                    reponse_finale = reponse.strip().lower()
                    time.sleep(0.2)
                    vider_buffer_clavier()
                    print()
                    return reponse_finale

                # Retour arrière
                if touche in ("\b", "\x7f"):
                    reponse = reponse[:-1]

                # Touches spéciales Windows
                elif os.name == "nt" and touche in ("\x00", "\xe0"):
                    if msvcrt.kbhit():
                        msvcrt.getwch()

                # Touches spéciales Linux (échappement, flèches...)
                elif touche == "\x1b":
                    lire_touche_linux()
                    lire_touche_linux()

                else:
                    reponse += touche

            time.sleep(0.03)

    finally:
        if os.name != "nt" and fd is not None and ancien_terminal is not None:
            termios.tcsetattr(fd, termios.TCSADRAIN, ancien_terminal)
