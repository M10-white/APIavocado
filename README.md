# APIavocado

## Description

**APIavocado** est un projet qui permet de prédire les prix des avocats en combinant une API Flask (back-end) et une interface utilisateur Vue.js (front-end).  
Le projet est organisé en deux parties principales : 

- **APIavocadoFRONT** : Interface utilisateur pour interagir avec l'API et soumettre des données.\
 -> https://github.com/M10-white/APIavocadoFRONT.git

- **APIavocadoBACK** : Serveur Flask pour gérer les requêtes, traiter les données et renvoyer les résultats.\
 -> https://github.com/M10-white/APIavocadoBACK.git

---

## Prérequis

### Outils nécessaires :

- [Python](https://www.python.org/) (version 3.8 ou supérieure)
- [Node.js](https://nodejs.org/) (version 14 ou supérieure)
- [npm](https://www.npmjs.com/)
- [Vue CLI](https://cli.vuejs.org/) (optionnel, si vous souhaitez développer le front)

---

## Installation
### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/M10-white/APIavocado.git
```

 ### Étape 2 : Configurer le back-end (APIavocadoBACK)
Accédez au répertoire du back-end :
```bash
cd src/back
```

Installez les dépendances Python nécessaires :
```bash
pip install flask pandas
```

Lancez le serveur Flask :
```bash
python app.py
```

L'API sera disponible par défaut à :
```bash
http://127.0.0.1:5000/
```

### Étape 3 : Configurer le front-end (APIavocadoFRONT)
Accédez au répertoire du front-end :
```bash
cd src/front
```

Installez les dépendances Node.js :
```bash
npm install
```

Lancez le serveur de développement Vue.js :
```bash
npm run serve
```

L'application sera disponible par défaut à :
```bash
http://localhost:8080/
```

## Utilisation

Accéder au Front-End : Ouvrez http://localhost:8080/ dans votre navigateur pour interagir avec l'interface utilisateur.

Accéder au Back-End : Ouvrez http://127.0.0.1:5000/ pour consulter directement les routes disponibles, comme l'affichage du fichier CSV.
