from ObjetsNetwork.arreraNeuron import *
import webbrowser
nom =  "Opale"
genre = "Monsieur"
user = "dev"
createur = "Baptiste Pauchet"
bute = "developper un algo de ChatBot qui sera inclut dans SIX et Ryley"
valeur =  0 
listeFonction = ["ouvrir une application"
                 ,"aider sur les recherches de internet",
                 "donner la meteo",
                 "faire un résumer des actualités"]
print("Beinvenu sur le programme de teste du chatbot. ")
mode = int(input("Facon de s'exprimer du chatbot\n1.Vousvoiment\n2.Tutoiment\n(1,2) $ "))
if mode == 1 : 
    neuron = ArreraNetwork(nom,user,genre,createur,bute,True,listeFonction) 
else :
    neuron = ArreraNetwork(nom,user,genre,createur,bute,False,listeFonction)
print("Programme de teste d'algorythme de chatBots.\nPour stopper la discution avec le chats bots marquer 'stop' ou 'quitter' \nquand c'est a votre tours de parler. \nSi vous voulez accedez a la page github du projet taper 'github'. \nDepuis cette page github vous pourrais consulter le code et proposer de \namélioration et correctif sur le serv discord ")
print(nom+" $ "+ neuron.boot())
while valeur != 15 :
    requette =  str(input("Vous $ "))
    if requette == "github" :
        webbrowser.open("https://github.com/Arrera-Software/ArreraChatBots")
    else :
        valeur , sortie = neuron.neuron(requette)
        print(valeur)
        print(nom + " $ "+sortie)               