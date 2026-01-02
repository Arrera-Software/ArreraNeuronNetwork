# Intégration d'Arrera Neuron dans un projet d'assistant

## Dossier

Déplacer les dossiers ```asset/```, ```brain/```, ```config/```, ```fnc/```, ```gestionnaire/```, ```gui/```, ```keywork/```, ```librairy/```, ```neuron/``` et ```objet/``` dans la racine de votre projet d'assistant.

Une fois ça fait, choisissez un langage que vous voulez dans le dossier ```language/```, soit ```tutoiment``` ou ```vouvoiment```.

## Configuration

Dans votre fichier main.py

Avant d'essayer de lancer votre assistant, il faut le configurer avec l'objet confNeuron.

Voici l'exemple de la configuration de l'assistant de développement Arrera OPALE


```python
config = confNeuron(name="Opale",
                   lang="fr",
                   asset="asset/",
                   icon="asset/icon.png",
                   assistant_color="white",
                   assistant_texte_color="black",
                   bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
                   createur="Pauchet Baptiste",
                   listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                                 "faire un résumer des actualités"],
                   moteurderecherche="google",
                   etatService=1,
                   etatTime=1,
                   etatOpen=1,
                   etatSearch=1,
                   etatChatbot=1,
                   etatApi=1,
                   etatCodehelp=1,
                   etatWork=1,
                   etatSocket=1,
                   lienDoc="www.google.com",
                   fichierLangue="language/",
                   fichierKeyword="keyword/",
                    voiceAssistant=True)
```
Les paramètres qui commencent par ```etat``` sont des paramètres à mettre soit à 1 ou 0, ce qui correspond au fait que vous voulez activer telle ou telle fonction de l'assistant.  
Le paramètre ```asset``` correspond à l'emplacement des assets de l'assistant.  
```icon``` est le paramètre pour l'icône de l'assistant.  
```assistant_color``` et ```assistant_texte_color``` sont la couleur et la couleur du texte de l'interface de l'assistant.  
```lienDoc``` est le lien vers la documentation en ligne.  
```fichierLangue``` est l'emplacement du dossier où se trouvent tous les fichiers de langue.  
```fichierKeyword``` est l'emplacement du dossier où se trouvent tous les fichiers de keyword.

## Intégration et utilisation dans un projet

Une fois la configuration faite, on peut démarrer l'assistant.


### Étape 1 : Initialisation de l'objet brain

```python
try :
    assistantBrain = ABrain(config=config)
    return True
except Exception as e:
    print(f"Erreur lors du démarrage de l'assistant Brain : {e}")
    return False
```

Il est conseillé d'utiliser un try pour éviter les crashs complets du programme.

Paramètre demandé : config, qui est la configuration que l'on a faite juste avant.

### Étape 2 : Démarrage

```python
try :
    self.__labelAssistantText.configure(text=assistantBrain.boot(), wraplength=200
    ,justify=LEFT)
except Exception as e:
    self.__labelAssistantText.configure(text=f"Erreur lors du boot de l'assistant : {e}",wraplength=200
    ,justify=LEFT)
```

La méthode ```boot()``` de l'objet ```ABrain``` permet de lancer l'assistant et retourne la formulation de salutation de l'assistant.

### Étape 3 : Envoi de requête à l'assistant

```python
def __sendAssistantMessage(self,entry:ctk.CTkEntry,screen:ctk.CTk):
    if not self.__thAssistant.is_alive():
        message = entry.get()
        if message:
            self.__thAssistant = th.Thread(target=self.__assistantBrain.neuron,args=(message,))
            self.__thAssistant.start()
            entry.delete(0, 'end')  # Clear the entry after sending
            self.__updateRequetteAssistant(screen,message)
        else:
            self.__labelAssistantText.configure(text="Veuillez entrer un message.", wraplength=200
                                                ,justify=LEFT)

def __updateRequetteAssistant(self,screen:ctk.CTk,message:str):
    if self.__thAssistant.is_alive():
        self.__arrTK.placeBottomRight(self.__labelGeneration)
        screen.after(1000,self.__updateRequetteAssistant,screen,message)
    else :
        del self.__thAssistant
        self.__labelGeneration.place_forget()
        self.__thAssistant = th.Thread()
        nb = self.__assistantBrain.getValeurSortie()
        texte = self.__assistantBrain.getListSortie()
        self.__labelAssistantText.configure(text=texte[0], wraplength=200
                                            ,justify=LEFT)
        self.__labelAssistantNumber.configure(text=str(nb))
        self.__addLog(nb,texte[0],message)
        if nb == 15:
            self.__close()
```

Il est conseillé, si vous utilisez une interface, d'utiliser un thread pour gérer les requêtes envoyées à l'assistant, car cela peut prendre un peu de temps pour le retour de la réponse à cause de l'utilisation d'une IA locale.

Une fois la réflexion de l'assistant finie, il faut utiliser la méthode ```getValeurSortie()``` pour récupérer la valeur de sortie, dont voici les sorties possibles :

- 0 : Aucune sortie
- 1 : Sortie normale
- 3 : Sortie actu
- 4 : Météo / température / GPS
- 5 : Sortie avec fenêtre tkinter
- 6 : Erreur actu
- 7 : Ouverture de fichier
- 8 : Fermeture de fichier
- 9 : Lecture fichier
- 10 : Création d'un projet
- 11 : Erreur du résumé actualités
- 12 : Réussite du résumé actualités
- 13 : Lecture tableur
- 14 : Ouverture d'un projet
- 15 : Arrêt de l'assistant
- 16 : Création d'un fichier dans un projet
- 17 : Affichage aide
- 18 : Résumé tâche / agenda
- 19 : Résumé all ok
- 20 : Résumé all fail
- 21 : Close projet
- 22 : Lancement de radio
- 23 : GUI Codehelp

Et pour récupérer les textes qu'a générés l'assistant, il faut utiliser la méthode ```getListSortie()``` qui ressort une liste Python, et le texte se trouve à l'index 0.

### Étape 4 : Récupération des requêtes envoyées par le socket

Les assistants développés sur la base de l'Arrera Neuron Network peuvent être connectés à l'application Arrera par l'intermédiaire d'un websocket.  
Pour en profiter, il faut créer une méthode qui tourne tout le temps pour récupérer les requêtes :  
Voici un exemple

```python
def __updateAssistant(self,screen:ctk.CTk=None):
    if self.__assistantBrain.updateAssistant():
        varOut = self.__assistantBrain.getValeurSortie()
        self.__labelAssistantText.configure(text=self.__assistantBrain.getListSortie()[0], wraplength=200)
        self.__labelAssistantNumber.configure(text=str(varOut))
        if varOut == 15:
            self.__close()

    screen.after(1000,self.__updateAssistant,screen)
```