from librairy.arrera_tk import *
"""
Todo : 
1 . GUI qui permet de decider la conf qu'on veux 
2 . GUI avec Sortie TEXTE et NOMBRE et UNE Zone d'entrer de texte
"""

class GUIOpale:
    def __init__(self):
        self.__arrTK = CArreraTK()

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
        self.__checkService = ctk.CTkCheckBox(frameNeuron,text="Neuron service")
        self.__checkSoftware = ctk.CTkCheckBox(frameNeuron, text="Neuron Logiciel")
        self.__checkTime = ctk.CTkCheckBox(frameNeuron, text="Neuron Temps")
        self.__checkOpen = ctk.CTkCheckBox(frameNeuron, text="Neuron Open")
        self.__checkRecherche = ctk.CTkCheckBox(frameNeuron, text="Neuron Recherche")
        self.__checkChatbot = ctk.CTkCheckBox(frameNeuron, text="Neuron Chatbots")
        self.__checkAPI = ctk.CTkCheckBox(frameNeuron, text="Neuron API")
        self.__checkCodeHelp = ctk.CTkCheckBox(frameNeuron, text="Neuron CodeHelp")
        self.__checkWork = ctk.CTkCheckBox(frameNeuron, text="Neuron Work")
        self.__checkSocket = ctk.CTkCheckBox(frameNeuron, text="Utilisation des socket")
        # Widget FrameLangue
        labelTitleLangue = self.__arrTK.createLabel(frameLangue,text="Gestion de la langue",ptaille=25)
        self.__btnVous = self.__arrTK.createButton(frameLangue,text="Vouvoiment",ptaille=20)
        self.__btnTutoiement = self.__arrTK.createButton(frameLangue,text="Tutoiement",ptaille=20)
        # Widget FrameValidate
        btnValidate = self.__arrTK.createButton(frameValidate,text="Valider",ptaille=25)
        # Affichage
        # FrameNeuron
        self.__arrTK.placeTopCenter(labelTitleNeuron)

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



