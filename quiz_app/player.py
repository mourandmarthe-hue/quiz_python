class Player:
    """
    Permet de représenter un joueur qui passe un quiz.
    """
    def __init__(self, nom):
        """
        Permet d'initialiser le joueur, avec un nom et un dictionnaire pour ses scores.
        nom : str, le nom du joueur
        """
        self.nom = nom
        self.scores = {} # les données sont alors stockées de la façon : {titre_quiz: score_obtenu}
    
    def enregistrer_score(self, quiz, score):
        """
        Permet d'enregistrer un score d'un joueur, pour un quiz défini.
        quiz : Quiz, instance du quiz que le joueur a passé.
        score : int, score obtenu par le joueur dans pour ce quiz.
        """
        self.scores[quiz.titre] = score

    def afficher_scores(self):
        """
        Permet d'afficher la totalité des scores obtenus par le joueur.
        """
        print (f"\n Scores de {self.nom} :")
        for titre, score in self.scores.items(): # self.scores renvoie une vue de chque éléments (items), ici (titre_quiz, score_obtenu)
            print (f"{titre} : {score}")