from quiz_app.question import Question

class Quiz:
    """
    Permet de représenter un quiz, avec un titre et une liste de questions.
    titre : str, titre (nom) du quiz
    questions : list[Question], la liste des questions du quiz
    """
    def __init__(self, titre):
        """
        Permet d'initialiser un quiz avec un titre et une liste de questions vide.
        (titre : str, titre du quiz)
        """
        self.titre = titre
        self.questions = [] #c'est la liste qui va contenir les objets Question du quiz
    
    def ajouter_question(self,question):
        """
        Permet d'ajouter une question à cette liste de questions du quiz.
        question : Question (instance de la classe Question), c'est la question à ajouter à la liste
        """
        self.questions.append(question)

    def lancer(self):
        """
        Permet de lancer le quiz, le faire passer à l'utilisateur.
        Pour chaque question, on affiche l'énoncé et les options, on récupère la réponse donnée par l'utilisateur, on vérifie si celle-ci est correcte, et on affiche "Correct" ou "Faux" ainsi que le score actuel.
        Enfin, à la fin on affiche le score total (chque réponse correcte rapporte 1 point)
        return : int, soit le score total
        """
        print(f"\n== QUIZ : {self.titre} ==\n") # on affiche le titre
        score = 0 # on initialise le score à 0
        max_score = self.score_max() # le score max possible

        # On parcourt toutes les questions du quiz, avec un compteur (boucle for avec enumerate)
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/{len(self.questions)}") # permet d'afficher le numéro de la question et le nombre total de questions posées

            # On pose la question à l'utilisateur avant de récupérer sa réponse (avec la méthode poser de Question)
            reponse = question.poser()

            # On calcule le score partiel
            points = question.score_utilisateur(reponse)
            score += points

            if points == 0:
                print (f"Faux... La bonne réponse est : {question.bonne_reponse}")
            elif isinstance(question.bonne_reponse, list) and points < len(question.bonne_reponse):
                print (f"Partiellement correct. Score : (+{points} point{'s' if points > 1 else ''})")
            else:
                print (f"Correct ! Score : (+{points} point{'s' if points > 1 else ''})")
            
            print ("-"*40) # permet d'afficher une ligne de tirets, pour faire plus propre

        print (f"\n Score final : {score} / {max_score()}")
        return score
    
    def score_max(self):
        """
        Permet de calculer le score max possible du quiz.
        Le QCM simple rapporte 1 point par question, celui multiple, autant que le nombre de bonnes réponses.
        """
        total = 0
        for q in self.questions:
            if isinstance((q.bonne_reponse, list)):
                total += len(q.bonne_reponse)
            else:
                total += 1
        return total
    
    def to_dict(self):
        """Pour sérialiser le quiz, afin de le sauvegarder sous forme de fichier JSON"""
        return {
            "titre" : self.titre,
            "questions" : [q.to_dict() for q in self.question]
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Permet de créer une instance Quiz à partir, donc, d'un dictionnaire (JSON)
        retourne : Quiz
        """
        quiz = cls(data["titre"]) # permet de créer une nouvelle instance de quiz, avec le titre de celui-ci stocké dans data
        for q_data in data ["questions"]:
            quiz.ajouter_question(Question.from_dict(q_data)) # pour contenir toutes les questions sous forme d'objets Question
        return quiz