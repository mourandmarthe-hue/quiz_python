from rich.console import Console
from rich.table import Table
console = Console()

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
        Utilisation de la librairie rich pour que les questions s'affichent sous forme de tableau.
        """
        #Affiche l'énoncé de la question
        console.print(f"\n[bold cyan]{self.enonce}[/bold cyan]\n")

        #Affiche les options, numérotées + création d'un tableau pour les afficher
        table = Table(title="Options")
        table.add_column("Numéro", style="cyan", justify="center")
        table.add_column("Réponse(s)", style="magenta")

        #On ajoute les lignes du tableau
        for i, option in enumerate(self.options, 1):
            table.add_row(str(i), option)

        #Affiche le tableau
        console.print(table)

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
    
    def score_utilisateur(self, reponse_utilisateur):
        """
        Permet de calculer le score partiel : combien de points l'utilisateur gagne, même si sa réponse est partiellement correcte.
        S'il s'agit d'un QCM simple : 1 si la réponse est la bonne, 0 sinon.
        S'il s'agit d'un QCM multiple : score est le nombre de réponses correctes choisies.
        """
        # QCM multiple :
        if isinstance(self.bonne_reponse, list):
            return len(set(reponse_utilisateur) & set(self.bonne_reponse)) # nombre de réponses correctes choisies par l'utilisateur
        else: # QCM simple
            return int(reponse_utilisateur == self.bonne_reponse)      
        
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
        """
        Permet de créer une instance Question à partir, donc, d'un dictionnaire (JSON)
        data : dict qui contient les clés "enonce", "options" et "bonne_reponse"
        retourne : Question
        """
        return cls(
            enonce = data["enonce"],
            options = data["options"],
            bonne_reponse = data["bonne_reponse"]
        )