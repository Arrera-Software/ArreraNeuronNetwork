import json

class jsonWork : 
    def __init__(self,file):
        self.fichier = file
        
    def lectureJSON(self,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            dict = json.load(openfile)[flag]
        return str(dict)
    
    def lectureJSONList(self,flag):
        with open(self.fichier, 'r' , encoding='utf-8') as openfile:
            liste = json.load(openfile)[flag]
        return list(liste)
     
    def EcritureJSON(self,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
        openfile = open(self.fichier, 'r' , encoding='utf-8')
        dict = json.load(openfile)
        openfile.close()
        writeFile = open(self.fichier, 'w', encoding='utf-8')
        dict[flag] = valeur
        json.dump(dict,writeFile,indent=2)