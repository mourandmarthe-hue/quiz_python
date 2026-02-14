# QUIZ_PYTHON

## Description du projet

Le projet permet de créer, lancer, gérer des quiz, qui sont interactifs, et permet de gérer des joueurs, et stocker, recharger des résultats.

Le projet utilise :
- 'rich' pour des affichages sous forme de tableaux, colorés, davantage interactifs
- 'pandas' pour illustrer des questions numériques et afficher des tableaux

## Structure du projet

quiz_python/
|
|-quiz_app/ # package contenant les classes principales du projet
|   |-init.py 
|   |-player.py # classe player
|   |-question.py # classe question
|   |-quiz.py # classe quiz
|   |-storage.py # classe storage
|-main.py # interface pour intéragir avec l'utilisateur
|-requirements.txt # dépendances (rich, pandas)
|-README.md
|-venv/ # environnement virtuel

## Classes
- Question : gère une question, les options de réponse, la ou les bonnes réponses et le score partiel ;
- Quiz : gère plusieurs questions et le calcul du score ;
- Player : représente un joueur ainsi que ses scores selon les quiz réalisés ;
- Storage : permet de sauvegarder ainsi que recharger les quiz et joueurs, via JSON.

## Installation du projet 

- Clôner le dépot du projet via GitHub :
    bash :
        git clone https://github.com/mourandmarthe-hue/quiz_python.git
        cd quiz_python
- Activer le venv :
    WSL :
        python3 -m venv .venv.
        source .venv/bin/activate
- Installer les dépendances :
    pip install -r requirements.txt

## Utilisation du projet

Lancer le projet :
    python main.py

## Le menu qui est proposé

- Créer un nouveau quiz
- Charger un quiz pré-existant
- Lancer un quiz
- Créer ou charger un joueur
- Sauvegarder le joueur
- Charger le joueur
- Quitter

Quand un quiz est lancé, les options de réponses aux questions s'affichent dans un tableau, avec rich. Les bonnes réponses sont en vert, celles partiellement correctes en jaune et celles fausses en rouge.
Il est également possible de sauvegarder les résultats d'un joueur pour les recharger plus tard.
Pour les questions numériques, un petit tableau peut s'afficher, avec pandas, pour par exemple illustrer les réponses ou résultats.

## Avec Git

- Créer une branche pour coder, ne pas tout coder directement sur main :
    git checkout -b feature-nom de la branche
- Après chaque action (programmation, etc.)
    git add .
    git commit -m "Action, modification réalisée"
    git push -u origin feature-nom de la branche
- Quand c'est terminé, créer un Pull-Request afin de merger la branche crée sur la branche main.

## Autrices

Yasmine Mhijy et Marthe Mourand
L3EIF

Merci !
