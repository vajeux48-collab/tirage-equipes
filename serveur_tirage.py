#!/usr/bin/env python3
"""Tirage au sort aléatoire : répartit des participants en 8 équipes de 10.

Utilisation :
    python tirage_equipes.py                 # utilise Participant 1..80
    python tirage_equipes.py noms.txt        # un nom par ligne (80 noms)
    python tirage_equipes.py noms.txt 42     # graine fixe pour un tirage reproductible
"""
import random
import sys

NB_EQUIPES = 8
TAILLE_EQUIPE = 10
TOTAL = NB_EQUIPES * TAILLE_EQUIPE


def charger_noms(chemin=None):
    if chemin is None:
        return [f"Participant {i}" for i in range(1, TOTAL + 1)]
    with open(chemin, encoding="utf-8") as f:
        noms = [ligne.strip() for ligne in f if ligne.strip()]
    if len(noms) != TOTAL:
        raise SystemExit(f"Erreur : {len(noms)} noms trouvés, {TOTAL} attendus.")
    if len(set(noms)) != len(noms):
        raise SystemExit("Erreur : il y a des doublons dans la liste.")
    return noms


def tirage(noms, graine=None):
    rng = random.Random(graine)
    melange = noms[:]
    rng.shuffle(melange)
    return [melange[i * TAILLE_EQUIPE:(i + 1) * TAILLE_EQUIPE] for i in range(NB_EQUIPES)]


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else None
    graine = int(sys.argv[2]) if len(sys.argv) > 2 else None

    equipes = tirage(charger_noms(chemin), graine)

    for numero, equipe in enumerate(equipes, start=1):
        print(f"\n=== Équipe {numero} ===")
        for nom in equipe:
            print(f"  - {nom}")


if __name__ == "__main__":
    main()


