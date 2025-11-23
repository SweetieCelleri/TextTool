#!/usr/bin/env python3
"""
TextTool : petit outil en ligne de commande permettant
d'appliquer différentes transformations sur un texte.

Ce fichier contient la fonction process_line qui analyse
les commandes entrées par l'utilisateur, ainsi que la boucle
principale exécutée dans main().
"""


def process_line(line):
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
# C commande prefix
    if cmd == "prefix":
        return text[:10]
    if cmd == "length":
        return str(len(text))
    # B : commande count-words
    if cmd == "count-words":
        return str(len(text.split()))

    return "Unknown command " + cmd



def main():
    """
        Boucle principale du programme.

        Affiche un prompt et lit les lignes saisies par l'utilisateur.
        Chaque ligne est transmise à process_line pour traitement,
        puis le résultat est affiché.

        La boucle prend fin lorsque l'utilisateur envoie EOF
        (Ctrl+D sous Linux/macOS ou Ctrl+Z sous Windows).
    """
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
