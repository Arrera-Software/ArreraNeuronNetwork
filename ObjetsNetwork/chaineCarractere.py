class chaine :
    def netoyage(chaine):
        chaine = str(chaine)
        chaine.replace("-"," ")
        chaine.replace('"'," ")
        chaine.replace("_"," ")
        chaine.replace('/'," ")
        chaine.replace("é","e")
        chaine.replace("è","e")
        chaine.replace("à","a")
        chaine.replace("ç","c")
        return chaine.lower()