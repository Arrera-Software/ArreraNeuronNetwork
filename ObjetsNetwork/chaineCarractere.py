class chaine :
    def netoyage(carractere:str):
        chaine = str(carractere)
        chaine = chaine.replace("-"," ")
        chaine = chaine.replace('"'," ")
        chaine = chaine.replace("_"," ")
        chaine = chaine.replace('/'," ")
        chaine = chaine.replace("é","e")
        chaine = chaine.replace("è","e")
        chaine = chaine.replace("à","a")
        chaine = chaine.replace("ç","c")
        chaine = chaine.replace("ê","e")
        return chaine.lower()
    
    def firstMots(chaine:str,liste:list):
        listeMots = liste
        indexMin = float('inf')
        motsMin = ""
        for mots in listeMots:
            index = chaine.find(mots)
            if index != -1 and index < indexMin:
                indexMin = index
                motsMin = mots

        return motsMin