import json 
from quiz_app import quiz
from quiz_app import player
from quiz_app.quiz import Quiz 
from quiz_app.player import Player
class Storage: 
        def sauvegarder_quiz(quiz, fichier): 
            with open(fichier, "w", encoding="utf-8") as f: 
                json.dump(quiz.to_dict(), f, indent=2, ensure_ascii=False)
            print(f"Quiz sauvegardé dans {fichier}")
        
        def charger_quiz(fichier):
            with open(fichier, "r", encoding="utf-8") as f: 
                data = json.load(f)
            quiz = Quiz.from_dict(data) 
            print(f"Quiz chargé depuis {fichier}") 
            return quiz 
    
        def sauvegarder_player(player, fichier): 
             with open(fichier, "w", encoding="utf-8") as f: 
                json.dump({"nom": player.nom, "scores": player.scores}, f, indent=2, ensure_ascii=False) 
             print(f"Joueur {player.nom} sauvegardé dans {fichier}") 

        def charger_player(fichier):
            with open(fichier, "r", encoding="utf-8") as f: 
               data = json.load(f) 
            joueur = Player(data["nom"]) 
            joueur.scores = data["scores"]  
            print(f"Joueur {joueur.nom} chargé depuis {fichier}") 
            return joueur 


