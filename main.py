from chatBots import *
import webbrowser
nom =  "SIX"
genre = "Monsieur"
user = "Baptiste"
valeur =  0 

chatBots = neuroneDiscution(nom,user,genre)
print("Programme de texte d'algorythme de chatBots.\nPour stopper la discution avec le chats bots marquer 'stop' ou 'quitter'\nquand c'est a votre tours de parler")
print("Si vous voulez accedez a la page github du projet taper 'github'. \nDepuis cette page github vous pourrais consulter le code et proposer de \namélioration et correctif sur le serv discord ")
while valeur != 15 :
    requette =  input("Vous $ ")
    if requette == "quitter" or requette == "stop" or requette == "Quitter" or requette == "Stop" :
        valeur =  15
    else :
        if requette == "github" :
            webbrowser.open("https://github.com/Arrera-Software/ArreraChatBots")
        else :
            valeur , sortie = chatBots.neurone(requette)
            print(valeur)
            if valeur ==  0 :
                print(nom + " $ "+"Je ne comprend ce que vous m'avez dit ou je ne peux pas vous répondre")
            else :
                print(nom + " $ "+sortie)