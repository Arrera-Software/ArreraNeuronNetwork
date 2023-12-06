from ObjetsNetwork.arreraNeuron import *
import webbrowser
from librairy.travailJSON import *

nom =  jsonWork("configNeuron1.json").lectureJSON("name")
valeur =  0 
print("Beinvenu sur le programme de teste du chatbot. ")
mode = int(input("Facon de s'exprimer du chatbot\n1.Vousvoiment\n2.Tutoiment\n(1,2) $ "))
if mode == 1 : 
    neuron = ArreraNetwork("configUser.json","configNeuron1.json","listFete.json") 
else :
    neuron = ArreraNetwork("configUser.json","configNeuron2.json","listFete.json")
print("Programme de teste d'algorythme de chatBots.\nPour stopper la discution avec le chats bots marquer 'stop' ou 'quitter' \nquand c'est a votre tours de parler. \nSi vous voulez accedez a la page github du projet taper 'github'. \nDepuis cette page github vous pourrais consulter le code et proposer de \namélioration et correctif sur le serv discord ")
print(nom+" $ "+ neuron.boot())
while valeur != 15 :
    requette =  str(input("Vous $ "))
    if requette == "github" :
        webbrowser.open("https://github.com/Arrera-Software/ArreraChatBots")
    else :
        valeur , sortie = neuron.neuron(requette)
        print(valeur)
        if ((valeur==12) or (valeur==11) or (valeur==3)) :
            if (valeur == 3) : 
                print(nom+" $ Actu :\n"+sortie[0]+"\n"+sortie[1]+"\n"+sortie[2])
            else :
                if (valeur == 12 or valeur == 11):
                    print("Opale : Voici votre resumer")
                    print(sortie)
        else :
            print(nom + " $ "+sortie[0])               