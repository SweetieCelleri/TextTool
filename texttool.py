#!/usr/bin/env python3



def process_line(line):
    """
    Analyse une ligne de commande au format 'commande texte'
    et applique la transformation correspondante.

    Commandes disponibles :
    - uppercase      : met le texte en majuscules
    - lowercase      : met le texte en minuscules
    - length         : renvoie la longueur du texte
    - count-words    : renvoie le nombre de mots
    - prefix         : renvoie les 10 premiers caractères

    Paramètres :
        line (str) : la ligne entrée par l'utilisateur

    Retour :
        str : le résultat de la commande ou un message d'erreur
    """
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "length":
        return str(len(text))
    # B : commande count-words
    if cmd == "count-words":
        return str(len(text.split()))

    return "Unknown command " + cmd



def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))



if __name__ == "__main__":
    main()
