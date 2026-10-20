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

## Déployer en ligne

### Option A : page HTML seule sur GitHub Pages (gratuit)

Héberge uniquement `tirage_equipes.html` (tirage sur l'écran de l'organisateur, sans QR code).

1. Sur GitHub : **Settings, Pages**, source **Deploy from a branch**, branche `main`, dossier `/ (root)`.
2. La page est disponible sur `https://VOTRE-NOM.github.io/tirage-equipes/tirage_equipes.html`.

### Option B : serveur avec QR code sur Render (gratuit)

1. Créez un compte sur [render.com](https://render.com) et reliez votre compte GitHub.
2. **New, Blueprint**, choisissez ce dépôt. Render lit `render.yaml`.
3. Renseignez la variable **PASSWORD** (mot de passe de la page organisateur) puis lancez le déploiement.
4. Ouvrez `https://VOTRE-SERVICE.onrender.com/organisateur` : le QR code pointe automatiquement vers l'adresse publique.

Limites de l'offre gratuite de Render :
- le service s'endort après un moment d'inactivité, le premier chargement peut prendre environ une minute : ouvrez la page organisateur avant l'événement ;
- le disque est effacé à chaque redémarrage, les tirages en cours sont alors perdus.

Le serveur lit les variables d'environnement `PORT` (port d'écoute) et `PASSWORD` (mot de passe organisateur).
