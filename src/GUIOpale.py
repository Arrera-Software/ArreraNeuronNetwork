import tkinter

from librairy.arrera_tk import *
from config.confNeuron import confNeuron
"""
Todo : 
1 . GUI qui permet de decider la conf qu'on veux 
2 . GUI avec Sortie TEXTE et NOMBRE et UNE Zone d'entrer de texte
"""

class GUIOpale:
    def __init__(self):
        self.__arrTK = CArreraTK()
        self.__emplacementLangue = "language/vouvoiment/"


    def active(self):
        self.__guiConf()
        self.__arrTK.view()

    def __guiConf(self):
        screen = self.__arrTK.aTK(width=500,height=500,
                                  title = "Opale",resizable=False,
                                  icon="asset/icon.png")
        self.__var = tkinter.BooleanVar(value=True)
        frameNeuron = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameLangue = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameValidate = self.__arrTK.createFrame(screen,width=500,height=50,wightBoder=True)
        # Widget FrameNeuron
        labelTitleNeuron = self.__arrTK.createLabel(screen,text="Gestion de neurone",ptaille=25)
        self.__checkService = ctk.CTkCheckBox(frameNeuron,text="Neuron\nservice",variable=self.__var)
        self.__checkSoftware = ctk.CTkCheckBox(frameNeuron, text="Neuron\nLogiciel",variable=self.__var)
        self.__checkTime = ctk.CTkCheckBox(frameNeuron, text="Neuron\nTemps",variable=self.__var)
        self.__checkOpen = ctk.CTkCheckBox(frameNeuron, text="Neuron\nOpen",variable=self.__var)
        self.__checkRecherche = ctk.CTkCheckBox(frameNeuron, text="Neuron\nRecherche",variable=self.__var)
        self.__checkChatbot = ctk.CTkCheckBox(frameNeuron, text="Neuron\nChatbots",variable=self.__var)
        self.__checkAPI = ctk.CTkCheckBox(frameNeuron, text="Neuron\nAPI",variable=self.__var)
        self.__checkCodeHelp = ctk.CTkCheckBox(frameNeuron, text="Neuron\nCodeHelp",variable=self.__var)
        self.__checkWork = ctk.CTkCheckBox(frameNeuron, text="Neuron\nWork",variable=self.__var)
        self.__checkSocket = ctk.CTkCheckBox(frameNeuron, text="Utilisation des socket",variable=self.__var)
        # Widget FrameLangue
        labelTitleLangue = self.__arrTK.createLabel(frameLangue,text="Gestion de la langue",ptaille=25)
        self.__btnVous = self.__arrTK.createButton(frameLangue,text="Vouvoiment",ptaille=20,command=lambda: self.__setLangue(1))
        self.__btnTutoiement = self.__arrTK.createButton(frameLangue,text="Tutoiement",ptaille=20,command=lambda: self.__setLangue(2))
        # Widget FrameValidate
        btnValidate = self.__arrTK.createButton(frameValidate, text="Valider", ptaille=25,
                                                command=lambda : self.__activateAssistantGUI(screen))
        # Affichage
        # FrameNeuron
        self.__arrTK.placeTopCenter(labelTitleNeuron)
        self.__checkService.place(x=10,  y=30,anchor="nw")
        self.__checkSoftware.place(x=130, y=30,anchor="nw")
        self.__checkTime.place(x=260, y=30,anchor="nw")
        self.__checkOpen.place(x=380, y=30,anchor="nw")
        self.__checkRecherche.place(x=10,  y=85,anchor="nw")
        self.__checkChatbot.place(x=130, y=85,anchor="nw")
        self.__checkAPI.place(x=260, y=85,anchor="nw")
        self.__checkCodeHelp.place(x=380, y=85,anchor="nw")
        self.__checkWork.place(x=130, y=160,anchor="nw")
        self.__checkSocket.place(x=260, y=160,anchor="nw")
        # FrameLangue
        self.__arrTK.placeTopCenter(labelTitleLangue)
        self.__arrTK.placeLeftCenter(self.__btnVous)
        self.__arrTK.placeRightCenter(self.__btnTutoiement)
        # FrameValidate
        self.__arrTK.placeCenter(btnValidate)
        # Frame
        self.__arrTK.pack(frameNeuron)
        self.__arrTK.pack(frameLangue)
        self.__arrTK.pack(frameValidate)

    def __setLangue(self,mode:int):
        """
        1. Vouvoiement
        2. Tutoiement
        """
        match mode:
            case 1 :
                self.__emplacementLangue = "language/vouvoiment/"
            case 2 :
                self.__emplacementLangue = "language/tutoiment/"
            case _ :
                self.__emplacementLangue = "language/vouvoiment/"

    def __setConfig(self):
        try :
            self.__config = confNeuron(name="Opale",
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
                                       etatService=int(self.__checkService.get()),
                                       etatSoftware=(int(self.__checkSoftware.get())),
                                       etatTime=int(self.__checkTime.get()),
                                       etatOpen=int(self.__checkOpen.get()),
                                       etatSearch=int(self.__checkRecherche.get()),
                                       etatChatbot=int(self.__checkChatbot.get()),
                                       etatApi=int(self.__checkAPI.get()),
                                       etatCodehelp=int(self.__checkWork.get()),
                                       etatWork=int(self.__checkSocket.get()),
                                       etatSocket=int(self.__checkSocket.get()),
                                       lienDoc="www.google.com",
                                       fichierLangue=str(self.__emplacementLangue))
            return True
        except Exception as e:
            print(f"Erreur lors de la création de la configuration : {e}")
            return False


    def __activateAssistantGUI(self,screen:ctk.CTk):
        """
        Fonction qui permet de lancer l'assistant GUI
        """
        if self.__setConfig():
            screen.destroy()
            self.__GUIAssistant()
            self.__arrTK.view()
            print("OK")
        else:
            print("Erreur lors de la création de la configuration de l'assistant.")


    def __GUIAssistant(self):
        screen = self.__arrTK.aTK(width=500, height=500,
                                  title="Opale Assistant", resizable=False,
                                  icon="asset/icon.png")

        # Frame
        frameAssistant = self.__arrTK.createFrame(screen, width=500, height=150)
        frameUser = self.__arrTK.createFrame(screen, width=350, height=50)

        # Widget
        labelTitle = self.__arrTK.createLabel(screen, text="Assistant Opale", ptaille=25)

        labelAssistantText = self.__arrTK.createLabel(frameAssistant, text="TEXTE", ptaille=20)
        labelAssistantNumber = self.__arrTK.createLabel(frameAssistant, text="NUMBER", ptaille=20)

        entryUser = self.__arrTK.createEntry(frameUser, width=200)
        btnSend = self.__arrTK.createButton(frameUser, text="Envoyer",ptaille=15)

        # Affichage

        self.__arrTK.placeTopCenter(labelTitle)
        self.__arrTK.placeCenter(frameAssistant)
        self.__arrTK.placeBottomCenterNoStick(frameUser)

        self.__arrTK.placeTopCenter(labelAssistantText)
        self.__arrTK.placeBottomCenter(labelAssistantNumber)

        self.__arrTK.placeLeftCenter(entryUser)
        self.__arrTK.placeRightCenter(btnSend)

