from librairy.arrera_tk import *
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
        frameNeuron = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameLangue = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameValidate = self.__arrTK.createFrame(screen,width=500,height=50,wightBoder=True)
        # Widget FrameNeuron
        labelTitleNeuron = self.__arrTK.createLabel(screen,text="Gestion de neurone",ptaille=25)
        self.__checkService = ctk.CTkCheckBox(frameNeuron,text="Neuron\nservice")
        self.__checkSoftware = ctk.CTkCheckBox(frameNeuron, text="Neuron\nLogiciel")
        self.__checkTime = ctk.CTkCheckBox(frameNeuron, text="Neuron\nTemps")
        self.__checkOpen = ctk.CTkCheckBox(frameNeuron, text="Neuron\nOpen")
        self.__checkRecherche = ctk.CTkCheckBox(frameNeuron, text="Neuron\nRecherche")
        self.__checkChatbot = ctk.CTkCheckBox(frameNeuron, text="Neuron\nChatbots")
        self.__checkAPI = ctk.CTkCheckBox(frameNeuron, text="Neuron\nAPI")
        self.__checkCodeHelp = ctk.CTkCheckBox(frameNeuron, text="Neuron\nCodeHelp")
        self.__checkWork = ctk.CTkCheckBox(frameNeuron, text="Neuron\nWork")
        self.__checkSocket = ctk.CTkCheckBox(frameNeuron, text="Utilisation des socket")
        # Widget FrameLangue
        labelTitleLangue = self.__arrTK.createLabel(frameLangue,text="Gestion de la langue",ptaille=25)
        self.__btnVous = self.__arrTK.createButton(frameLangue,text="Vouvoiment",ptaille=20,command=lambda: self.__setLangue(1))
        self.__btnTutoiement = self.__arrTK.createButton(frameLangue,text="Tutoiement",ptaille=20,command=lambda: self.__setLangue(2))
        # Widget FrameValidate
        btnValidate = self.__arrTK.createButton(frameValidate,text="Valider",ptaille=25)
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
