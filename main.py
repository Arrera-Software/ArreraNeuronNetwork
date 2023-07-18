from chatBots import *
import webbrowser
nom =  "Opale"
genre = "Monsieur"
user = "dev"
createur = "Baptiste Pauchet"
bute = "developper un algo de ChatBot qui sera inclut dans SIX et Ryley"
valeur =  0 
print("Beinvenu sur le programme de teste du chatbot. ")
mode = int(input("Facon de s'exprimer du chatbot\n1.Vousvoiment\n2.Tutoiment\n$"))
if mode == 1 : 
    chatBots = neuroneDiscution(nom,user,genre,createur,bute,True)
else :
    chatBots = neuroneDiscution(nom,user,genre,createur,bute,False)
print("Programme de teste d'algorythme de chatBots.\nPour stopper la discution avec le chats bots marquer 'stop' ou 'quitter' \nquand c'est a votre tours de parler. \nSi vous voulez accedez a la page github du projet taper 'github'. \nDepuis cette page github vous pourrais consulter le code et proposer de \namélioration et correctif sur le serv discord ")
print(nom+" $ "+ chatBots.boot())
while valeur != 15 :
    requette =  input("Vous $ ")
    if requette == "github" :
        webbrowser.open("https://github.com/Arrera-Software/ArreraChatBots")
    else :
        valeur , sortie = chatBots.neurone(requette)
        print(valeur)
        print(nom + " $ "+sortie)               