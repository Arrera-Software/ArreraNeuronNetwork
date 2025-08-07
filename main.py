from src.GUIOpale import GUIOpale
"""
from brain.brain import *
import webbrowser
from librairy.travailJSON import *
from config.confNeuron import confNeuron

conf = confNeuron(name="Opale",
                  lang="fr",
                  icon="asset/icon.png",
                  assetHorloge="asset/horloge/",
                  assetCalculatrice="asset/calculatrice/",
                  assetMicro = "",
                  assistant_color="white",
                  assistant_texte_color="black",
                  bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
                  createur="Pauchet Baptiste",
                  listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                          "faire un résumer des actualités"],
                  moteurderecherche="google",
                  etatService=1,
                  etatSoftware=1,
                  etatTime=1,
                  etatOpen=1,
                  etatSearch=1,
                  etatChatbot=1,
                  etatApi=1,
                  etatCodehelp=1,
                  etatWork=1,
                  etatSocket=1,
                  lienDoc="www.google.com",
                  fichierLangue="language/vouvoiment/")

def main():
    nom =  jsonWork("JSON/configNeuron1.json").getContentJsonFlag("name")
    valeur =  0
    print("Beinvenu sur le programme des assistants Arrera. ")
    mode = int(input("Facon de s'exprimer d'Opale\n1.Vousvoiment\n2.Tutoiment\n(1,2) $ "))
    assistant = ABrain(conf)
    print("Programme de teste de base des assistant d'arrera.\nPour arreter de parler avec l'assistant marquer 'stop' ou 'quitter' \nquand c'est a votre tours de parler. \nSi vous voulez accedez a la page github du projet taper 'github'. \nDepuis cette page github vous pourrais consulter le code et proposer de \namélioration et correctif sur le serv discord ")

    hist = int(input("Comment voulez-vous demarer l'assistant avec l'historique\n1.NON\n2.OUI\n(1,2) $"))
    if (hist == 1):
        print(nom+" $ "+ assistant.boot(1))
    else :
        print(nom+" $ "+ assistant.boot(2))

    while valeur != 15 :
        requette =  str(input("Vous $ "))
        if requette == "github" :
            webbrowser.open("https://github.com/Arrera-Software/ArreraChatBots")
        else :
            assistant.neuron(requette)
            valeur = assistant.getValeurSortie()
            sortie = assistant.getListSortie()
            neuronUsed = assistant.getNeuronUsed()
            print(valeur)
            print(neuronUsed)
            if ((valeur==12) or (valeur==11) or (valeur==3)
                    or (valeur ==13) or (valeur == 18) or (valeur == 19)
                    or (valeur == 20)) :
                if valeur == 3:
                    print(nom+" $ Actu :\n"+sortie[0]+"\n"+sortie[1]+"\n"+sortie[2])
                else :
                    if valeur == 12 or valeur == 11:
                        if valeur == 12:
                            print(nom+" $ "+sortie[6]+"\n \n")
                            print(sortie[0]+"\n"+sortie[1]+"\n"+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n"+sortie[5])
                        else :
                            print(nom+" $ "+"Erreur resumer actulitees")
                    else :
                        if valeur == 18:
                            print(nom + " $ "+sortie[0]+"\n"+nom + " $ "+sortie[1])
                        else :
                            if valeur == 19:
                                print(nom+" $ "+sortie[6]+"\n \n")
                                print(sortie[0]+"\n"+sortie[1]+"\n"+sortie[2]+"\n"+sortie[3]+"\n"+sortie[4]+"\n"+sortie[5]+"\n"+sortie[7]+"\n"+sortie[8])
                            else :
                                if valeur == 20:
                                    print(nom+" $ "+sortie[0])
                                else :
                                    nb = len(sortie)
                                    for i in range(0,nb):
                                        print("\n"+str(sortie[i]))
            else :
                print(nom + " $ "+sortie[0])
"""
def main():
    GUIOpale().active()

if __name__ == "__main__":
    main()