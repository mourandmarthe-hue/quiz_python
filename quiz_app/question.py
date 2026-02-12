class Question:
    def __init__(self, enonce, options, bonne_reponse):
        """
        Permet d'initialiser une question (QCM)
        Comme arguments :
        enonce : str, texte de la question
        options : list de str (list[str]), options possibles
        bonne_reponsse : list[str] ou str, bonne(s) réponse(s)
        """
        self.enonce = enonce
        self.options = options
        self.bonne_reponse = bonne_reponse
    
    def poser(self):
        """
        Permet d'afficher la question à l'utilisateur, ainsi que les options.
        Récupère ensuite les réponses sous forme de str ou list[str]
        """
        #Affiche l'énoncé de la question
        print("\n" + self.enonce)

        #Affiche les options, numérotées
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        
        #Récupère la réponse de l'utilisateur, les numéros séparés par des virgules si plusieurs choix
        reponse = input("Votre réponse (chaque numéro séparé par une virgule si plusieurs choix) :")

        #Pour convertir les numéros donnés en indices (0-based) afin de récupérer les options qui correspondent (comme l'utilisateur tape un numéro, pas le texte exact de la réponse)
        indices = [int(x.strip()) - 1 for x in reponse.split(",")]

        #Récupère donc les réponses correspondantes, choisies par l'utilisateur
        reponses_utilisateur = [self.options[i] for i in indices]
        
        #Boucle : si une seule bonne réponse, return str, else return list[str] (vérification du type de l'object avec isinstance)
        if isinstance(self.bonne_reponse, str):
            return reponses_utilisateur[0] #retourne la première (donc seule) réponse choisie
        else :
            return reponses_utilisateur #retourne la liste des réponses choisies
        
    def verifier_reponse(self, reponse_utilisateur):
        """ 
        Permet de vérifier si la réponse donnée par l'utilisateur est la bonne, ou non.
        reponse_utilisateur : str ou list[str], réponse donnée par l'utilisateur
        booléen : retourne True si la réponse est bonne, False sinon
        """
        #Si la bonne réponse est sous forme de liste, il faut comparer, comme des ensembles, les réponses données (fonction : set())
        if isinstance(self.bonne_reponse, list):
            return set(reponse_utilisateur) == set(self.bonne_reponse)
        else:
            #sinon, il faut comparer les deux strings
            return reponse_utilisateur == self.bonne_reponse
        
    def to_dict(self):
        """
        Permet de convertir la question en dictionnaire pour la stocker dans un fichier JSON
        retourne : dict
        """
        return {
            "enonce": self.enonce,
            "options": self.options,
            "bonne_reponse": self.bonne_reponse
        }

    @classmethod
    #la méthode appartient à la classe et non à une instance, la première variable est cls qui représente la classe, ici Question
    def from_dict(cls, data):
