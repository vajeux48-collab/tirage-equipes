# Tirage d'équipes

Répartition aléatoire de participants en équipes (par défaut 8 équipes de 10), en deux versions.

## 1. Page HTML seule : `tirage_equipes.html`

Double-cliquez sur le fichier pour l'ouvrir dans le navigateur. Aucun serveur, aucune connexion internet.

1. Collez les noms (un par ligne).
2. Réglez le nombre d'équipes et leur taille.
3. Cliquez sur « Tirer au sort ». Vous pouvez copier le résultat ou l'enregistrer en `.txt`.

Une graine facultative permet de refaire exactement le même tirage.

## 2. Serveur avec QR code : `serveur_tirage.py`

Chaque joueur scanne un QR code, saisit son nom, appuie sur **Jouer** et reçoit son numéro d'équipe. Aucun compte n'est nécessaire. L'organisateur voit les noms arriver en direct.

Python 3 suffit, rien à installer.

```bash
python3 serveur_tirage.py
python3 serveur_tirage.py --port 8000 --password monmotdepasse
python3 serveur_tirage.py --url https://mon-adresse-publique.example   # derrière un tunnel
```

- Joueurs : l'adresse affichée au démarrage (celle du QR code).
- Organisateur : la même adresse + `/organisateur`, avec le mot de passe affiché au démarrage.
- Les joueurs doivent pouvoir joindre l'ordinateur : même Wi-Fi, ou tunnel (cloudflared, ngrok) avec `--url`.
- Les résultats sont gardés dans `tirage_etat.json` (ignoré par git).
- Chaque navigateur ne peut tirer qu'une fois.
