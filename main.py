from quiz_app.question import Question
from quiz_app.quiz import Quiz
from quiz_app.storage import Storage
from quiz_app.player import Player
import pandas as pd

def menu(): 
    print("\n=== Menu Quiz ===") 
    print("1. Créer un nouveau quiz") 
    print("2. Charger un quiz") 
    print("3. Lancer un quiz") 
    print("4. Créer / Charger un joueur") 
    print("5. Sauvegarder le joueur") 
    print("6. Charger le joueur") 
    print("7. Quitter") 
    choix = input("Votre choix : ") 
    return choix 

def main(): 
    quiz = None 
    joueur = None 
 
    print("Bienvenue dans le Quiz App !") 
    print("Vous pouvez créer un quiz, le lancer, et sauvegarder vos résultats.") 
    while True:
        choix = menu()
        if choix == "1":
            titre = input("Titre du quiz : ") 
            quiz = Quiz(titre) 
            n = int(input("Combien de questions ? ")) 
            for i in range(n): 
                enonce = input(f"Question {i+1} : ") 
                options = input("Options (séparées par des virgules) : ").split(",") 
                options = [opt.strip() for opt in options] 
                bonne = input("Bonne réponse (ou plusieurs séparées par des virgules) : ").split(",") 
                if len(bonne) == 1: 
                    bonne = bonne[0].strip() 
                else: 
                     bonne = [b.strip() for b in bonne] 
                question = Question(enonce, options, bonne) 
                quiz.ajouter_question(question) 
            fichier = input("Nom du fichier pour sauvegarder le quiz : ") 
            Storage.sauvegarder_quiz(quiz, fichier) 
        elif choix == "2": 
            fichier = input("Nom du fichier à charger : ") 
            quiz = Storage.charger_quiz(fichier)   
        elif choix == "3": 
            if quiz: 
                score = quiz.lancer() 
                if joueur: 
                    joueur.enregistrer_score(quiz, score) 
            else: 
                print("Aucun quiz chargé.")  
        elif choix == "4": 
            nom = input("Nom du joueur : ") 
            joueur = Player(nom) 
            print(f"Joueur {nom} créé.") 
        elif choix == "5": 
            if joueur: 
                fichier = input("Nom du fichier pour sauvegarder le joueur : ") 
                Storage.sauvegarder_player(joueur, fichier) 
            else: 
                print("Aucun joueur créé.")
        elif choix == "6": 
            fichier = input("Nom du fichier à charger : ") 
            joueur = Storage.charger_player(fichier) 
        elif choix == "7": 
            print("Au revoir !") 
            break
        else: 
            print("Choix invalide.") 

if __name__ == "__main__":
    main()
    