# Le Trésor de Valou — sans Render

## Version GitHub Pages (statique)

- `index.html` : renvoi vers la page joueur
- `joueur.html` : prénom, code individuel, équipe
- `admin.html` : préparer des équipes et exporter les codes CSV
- `shared.js` et `style.css` : tirage et thème féria, Cévennes, Pays Basque

**Activer GitHub Pages :** Settings > Pages > Deploy from a branch > main > / (root) > Save.

Adresse joueur : https://vajeux48-collab.github.io/tirage-equipes/joueur.html

Adresse admin : https://vajeux48-collab.github.io/tirage-equipes/admin.html

L'organisateur génère les codes dans admin.html, télécharge le CSV et donne un code distinct à chaque invité. Les codes déterminent des équipes équilibrées. Aucun compte ni base de données nécessaire.

**Limites :** GitHub Pages n'exécute pas le serveur Python. Les inscriptions ne sont pas synchronisées entre téléphones ; la page admin n'est pas protégée ; les codes peuvent être réutilisés sur d'autres appareils. Le fichier `serveur_tirage.py` est conservé dans le dépôt, mais n'est pas exécuté par GitHub Pages.
