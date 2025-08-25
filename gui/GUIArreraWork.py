from gui.guibase import GuiBase,gestionnaire
from tkinter.filedialog import askdirectory,askopenfilename
import customtkinter as ctk
from tkinter.messagebox import showerror
from tkinter import StringVar

class CAnWorkGUI(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Arrera Work")
        # Attributs
        self.__tableurOpen = False
        self.__wordOpen = False
        self.__projectOpen = False
        # Variables d'interface
        self.__var = None
        self.__nameProjet = None
        # asset
        self.__emplacementAsset = self._gestionnaire.getConfigFile().asset+"work/"


    def __createWindows(self):
        self._screen.rowconfigure(0, weight=1)
        self._screen.rowconfigure(1, weight=0)
        self._screen.columnconfigure(0, weight=1)
        self._screen.columnconfigure(1, weight=2)
        self._screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableurAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/tableur.png",
                                                    tailleX=100, tailleY=100)
        imgWordAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/word.png",
                                                 tailleX=100, tailleY=100)
        imgProjectAcceuil = self._arrtk.createImage(self.__emplacementAsset + "acceuil/project.png",
                                                    tailleX=100, tailleY=100)

        imgTableurDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/tableur.png",
                                                 tailleX=50, tailleY=50)
        imgWordDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/word.png",
                                              tailleX=50, tailleY=50)
        imgProjectDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/project.png",
                                                 tailleX=50, tailleY=50)
        imgAnnulerDock = self._arrtk.createImage(self.__emplacementAsset + "acceuil/annuler.png",
                                                 tailleX=50, tailleY=50)

        # Images pour la frame Tableur
        imgAddComptage = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-comptagexcf.png",
                                                 tailleX=90, tailleY=90)
        imgAddMaxmum = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-maxmum.png",
                                               tailleX=90, tailleY=90)
        imgAddMinimum = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-minimum.png",
                                                tailleX=90, tailleY=90)
        imgAddMoyenne = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-moyenne.png",
                                                tailleX=90, tailleY=90)
        imgAddSomme = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-somme.png"
                                              , tailleX=90, tailleY=90)
        imgAddValeur = self._arrtk.createImage(self.__emplacementAsset + "tableur/add-valeur.png"
                                               , tailleX=90, tailleY=90)
        imgCloseTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/close-tableur.png"
                                                  , tailleX=90, tailleY=90)
        imgOpenTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/open-tableur.png"
                                                 , tailleX=90, tailleY=90)
        imgOpenTableurCoputerSoft = self._arrtk.createImage(self.__emplacementAsset + "tableur/open-tableur-coputer-soft.png"
                                                            , tailleX=90, tailleY=90)
        imgReadTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/read-tableur.png"
                                                 , tailleX=90, tailleY=90)
        imgSupprValeur = self._arrtk.createImage(self.__emplacementAsset + "tableur/suppr-valeur.png"
                                                 , tailleX=90, tailleY=90)
        imgViewTableur = self._arrtk.createImage(self.__emplacementAsset + "tableur/view-tableur.png"
                                                 , tailleX=90, tailleY=90)

        # Images pour la frame Word
        imgOpenWord = self._arrtk.createImage(self.__emplacementAsset + "word/open-word.png",
                                              tailleX=90, tailleY=90)
        imgOpenWordWithComputer = self._arrtk.createImage(self.__emplacementAsset + "word/open-word-coputer-soft.png",
                                                          tailleX=90, tailleY=90)
        imgCloseWord = self._arrtk.createImage(self.__emplacementAsset + "word/close-word.png",
                                               tailleX=90, tailleY=90)
        imgReadWord = self._arrtk.createImage(self.__emplacementAsset + "word/read-word.png",
                                              tailleX=90, tailleY=90)
        imgWriteWord = self._arrtk.createImage(self.__emplacementAsset + "word/write-word.png",
                                               tailleX=90, tailleY=90)

        # Images pour la frame Projet
        imgCreateFileProjet = self._arrtk.createImage(self.__emplacementAsset + "project/create-file-project.png",
                                                      tailleX=90, tailleY=90)
        imgCreateProject = self._arrtk.createImage(self.__emplacementAsset + "project/create-projet.png",
                                                   tailleX=90, tailleY=90)
        imgOpenFileProjet = self._arrtk.createImage(self.__emplacementAsset + "project/open-file-project.png",
                                                    tailleX=90, tailleY=90)
        imgOpenProjet = self._arrtk.createImage(self.__emplacementAsset + "project/open-project.png",
                                                tailleX=90, tailleY=90)
        imgSetTypeProjet = self._arrtk.createImage(self.__emplacementAsset + "project/setType-project.png",
                                                   tailleX=90, tailleY=90)
        imgTaskSayProjet = self._arrtk.createImage(self.__emplacementAsset + "project/task-say.png",
                                                   tailleX=90, tailleY=90)
        imgTaskViewProjet = self._arrtk.createImage(self.__emplacementAsset + "project/view-task-project.png",
                                                    tailleX=90, tailleY=90)
        imgViewTypeFileProjet = self._arrtk.createImage(self.__emplacementAsset + "project/view-type.png",
                                                        tailleX=90, tailleY=90)
        imgCloseProjet = self._arrtk.createImage(self.__emplacementAsset + "project/close-project.png",
                                                 tailleX=90, tailleY=90)

        # Frames
        self.__fAcceuil = self._arrtk.createFrame(self._screen)
        self.__fDock = self._arrtk.createFrame(self._screen, bg="grey", height=70)
        self.__fTableur = self._arrtk.createFrame(self._screen)
        self.__fTableurNoOpen = self._arrtk.createFrame(self._screen)
        self.__fWord = self._arrtk.createFrame(self._screen)
        self.__fWordNoOpen = self._arrtk.createFrame(self._screen)
        self.__fProjet = self._arrtk.createFrame(self._screen)
        self.__fProjetNoOpen = self._arrtk.createFrame(self._screen)

        # Widgets dans la frame d'accueil
        labelTitleAcceuil = self._arrtk.createLabel(self.__fAcceuil, text=self._gestionnaire.getConfigFile().name + " : Arrera Work",
                                                    ppolice="Arial", ptaille=25)
        btnArreraTableurAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,
                                                           height=100, image=imgTableurAcceuil,
                                                           command=self.__activeTableur)
        btnArreraWordAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,
                                                        height=100, image=imgWordAcceuil,
                                                        command=self.__activeWord)
        btnArreraProjectAcceuil = self._arrtk.createButton(self.__fAcceuil, width=100,
                                                           height=100, image=imgProjectAcceuil,
                                                           command=self.__activeProjet)

        # Widgets dans la frame dock
        btnArreraTableurDock = self._arrtk.createButton(self.__fDock, width=60,
                                                        height=60, image=imgTableurDock,
                                                        command=self.__activeTableur)
        btnArreraWordDock = self._arrtk.createButton(self.__fDock, width=60,
                                                     height=60, image=imgWordDock,
                                                     command=self.__activeWord)
        btnArreraProjectDock = self._arrtk.createButton(self.__fDock, width=60,
                                                        height=60, image=imgProjectDock,
                                                        command=self.__activeProjet)
        btnCloseAcceuilDock = self._arrtk.createButton(self.__fDock, width=60,
                                                       height=60, image =imgAnnulerDock,
                                                       command=self.__closeDock)

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = self._arrtk.createLabel(self.__fTableurNoOpen, text="Travail sur un tableur",
                                                          ppolice="Arial", ptaille=25)
        btnOpenTableur = self._arrtk.createButton(self.__fTableurNoOpen, width=90, height=90,
                                                  image=imgOpenTableur, command=self.__openTableur)
        labelTitleTableur = self._arrtk.createLabel(self.__fTableur, text="Travail sur un tableur",
                                                    ppolice="Arial", ptaille=25)
        btnOpenTableurWithComputer = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                              image=imgOpenTableurCoputerSoft,
                                                              command=self.__openTableurCoputerSoft)
        btnCloseTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                   image=imgCloseTableur, command=self.__closeTableur)
        # btnReadTableur = self.__arrTk.createButton(self.__fTableur,width=90,height=90,image=imgReadTableur,command=self.__addValeurTableur())

        btnAddValeurTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                       image=imgAddValeur, command=self.__addValeurTableur)
        btnAddMoyenneTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                        image=imgAddMoyenne, command=self.__addMoyenneTableur)
        btnAddSommeTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                      image=imgAddSomme, command=self.__addSommeTableur)
        btnAddComptageTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                         image=imgAddComptage, command=self.__addComptageTableur)
        btnAddMinimumTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                        image=imgAddMinimum, command=self.__addMinimumTableur)
        btnAddMaximumTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                        image=imgAddMaxmum, command=self.__addMaximumTableur)
        btnAffichageTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                       image=imgViewTableur, command=self.__viewTableur)
        btnSupprDataTableur = self._arrtk.createButton(self.__fTableur, width=90, height=90,
                                                       image=imgSupprValeur,
                                                       command=self.__supprValeurTableur)

        # Widgets dans la frame Word
        labelTitleNoOpenWord = self._arrtk.createLabel(self.__fWordNoOpen, text="Travail sur un document Word",
                                                       ppolice="Arial", ptaille=25)
        btnOpenWord = self._arrtk.createButton(self.__fWordNoOpen, width=90, height=90, image=imgOpenWord,
                                               command=self.__openWord)

        labelTitleWord = self._arrtk.createLabel(self.__fWord, text="Travail sur un document Word",
                                                 ppolice="Arial", ptaille=25)
        btnOpenWordWithComputer = self._arrtk.createButton(self.__fWord, width=90, height=90,
                                                           image=imgOpenWordWithComputer, command=self.__openWordCoputerSoft)
        btnCloseWord = self._arrtk.createButton(self.__fWord, width=90, height=90,
                                                image=imgCloseWord, command=self.__closeWord)
        # btnReadWord = self.__arrTk.createButton(self.__fWord,width=90,height=90,
        #image=imgReadWord,command=self.__readWord)
        btnWriteWord = self._arrtk.createButton(self.__fWord, width=90, height=90, image=imgWriteWord,
                                                command=self.__writeWord)

        # Widget dans la frame Projet
        # No OPEN
        labelTitleNoOpenProjet = self._arrtk.createLabel(self.__fProjetNoOpen, text="Travail sur un projet",
                                                         ppolice="Arial", ptaille=25)

        btnOpenProjet = self._arrtk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                 image=imgOpenProjet
                                                 , command=self.__openProjet)

        btnCreateProjet = self._arrtk.createButton(self.__fProjetNoOpen, width=90, height=90,
                                                   image=imgCreateProject,
                                                   command=self.__windowsNameNewProjet)

        # OPEN
        labelTitleProjet = self._arrtk.createLabel(self.__fProjet, text="Travail sur un projet",
                                                   ppolice="Arial", ptaille=25)
        btnAddTypeProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90,
                                                    image=imgSetTypeProjet, command=self.__windowsTypeFileProjet)
        btnCreateFileProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgCreateFileProjet,
                                                       command=self.__windowsCreateFileProjet)
        btnOpenFileProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgOpenFileProjet,
                                                     command=self.__openFileProjet)
        btnViewTaskProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgTaskViewProjet,
                                                     command=self.__openTaskProjet)
        btnSayAllTaskProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90,
                                                       image=imgTaskSayProjet, command=self.__sayTaskProjet)

        btnCloseProjet = self._arrtk.createButton(self.__fProjet, width=90, height=90, image=imgCloseProjet,
                                                  command=self.__closeProjet)

        # Grille des frame
        self.__fAcceuil.rowconfigure(0, weight=1)
        self.__fAcceuil.rowconfigure(1, weight=0)
        self.__fAcceuil.rowconfigure(2, weight=1)

        # Colonnes pareil pour leur largeur
        self.__fAcceuil.columnconfigure(0, weight=1)
        self.__fAcceuil.columnconfigure(1, weight=2)
        self.__fAcceuil.columnconfigure(2, weight=1)

        self.__fDock.grid_columnconfigure(0, weight=1)
        self.__fDock.grid_columnconfigure(5, weight=1)

        self.__fTableurNoOpen.grid_rowconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_rowconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(2, weight=0)
        self.__fTableurNoOpen.grid_rowconfigure(3, weight=1)

        self.__fTableurNoOpen.grid_columnconfigure(0, weight=1)
        self.__fTableurNoOpen.grid_columnconfigure(1, weight=0)
        self.__fTableurNoOpen.grid_columnconfigure(2, weight=1)

        self.__fTableur.grid_columnconfigure(0, weight=1)
        self.__fTableur.grid_columnconfigure(1, weight=1)
        self.__fTableur.grid_columnconfigure(2, weight=1)

        self.__fWordNoOpen.grid_rowconfigure(0, weight=1)
        self.__fWordNoOpen.grid_rowconfigure(1, weight=0)
        self.__fWordNoOpen.grid_rowconfigure(2, weight=0)
        self.__fWordNoOpen.grid_rowconfigure(3, weight=1)

        self.__fWordNoOpen.grid_columnconfigure(0, weight=1)
        self.__fWordNoOpen.grid_columnconfigure(1, weight=0)
        self.__fWordNoOpen.grid_columnconfigure(2, weight=1)

        self.__fWord.grid_columnconfigure(0, weight=1)
        self.__fWord.grid_columnconfigure(1, weight=1)
        self.__fWord.grid_columnconfigure(2, weight=1)

        self.__fProjetNoOpen.grid_rowconfigure(0, weight=1)
        self.__fProjetNoOpen.grid_rowconfigure(1, weight=0)
        self.__fProjetNoOpen.grid_rowconfigure(2, weight=0)
        self.__fProjetNoOpen.grid_rowconfigure(3, weight=1)

        self.__fProjetNoOpen.grid_columnconfigure(0, weight=1)
        self.__fProjetNoOpen.grid_columnconfigure(1, weight=0)
        self.__fProjetNoOpen.grid_columnconfigure(2, weight=1)

        # Centrage vertical par lignes vides
        self.__fProjet.grid_rowconfigure(0, weight=1)
        self.__fProjet.grid_rowconfigure(5, weight=1)

        # Centrage horizontal
        self.__fProjet.grid_columnconfigure(0, weight=1)
        self.__fProjet.grid_columnconfigure(1, weight=0)
        self.__fProjet.grid_columnconfigure(2, weight=1)


        # Affichage des frames
        labelTitleAcceuil.grid(row=0, column=0, columnspan=3, sticky='new', pady=20)  # En haut, centré, espacé en haut

        # Placement des boutons sur la même ligne et centrés
        btnArreraTableurAcceuil.grid(row=1, column=0, padx=10, pady=60)
        btnArreraWordAcceuil.grid(row=1, column=1, padx=10, pady=60)
        btnArreraProjectAcceuil.grid(row=1, column=2, padx=10, pady=60)

        # PLacement des boutons dans le dock
        btnArreraTableurDock.grid(row=0, column=1, padx=5, pady=5)
        btnArreraWordDock.grid(row=0, column=2, padx=5, pady=5)
        btnArreraProjectDock.grid(row=0, column=3, padx=5, pady=5)
        btnCloseAcceuilDock.grid(row=0, column=4, padx=5, pady=5)

        # Placement widget des frame Tableur
        labelTitleNoOpenTableur.grid(row=0, column=1, sticky="n")
        btnOpenTableur.grid(row=2, column=1, sticky="n")

        labelTitleTableur.grid(row=0, column=0, columnspan=3, sticky='ew')

        btnOpenTableurWithComputer.grid(row=1, column=0, padx=20, pady=20)


        btnAddValeurTableur.grid(row=1, column=1, padx=20, pady=20)
        btnAddMoyenneTableur.grid(row=1, column=2, padx=20, pady=20)
        btnAddSommeTableur.grid(row=2, column=0, padx=20, pady=20)
        btnAddComptageTableur.grid(row=2, column=1, padx=20, pady=20)
        btnAddMinimumTableur.grid(row=2, column=2, padx=20, pady=20)
        btnAddMaximumTableur.grid(row=3, column=0, padx=20, pady=20)
        btnAffichageTableur.grid(row=3, column=1, padx=20, pady=20)
        btnSupprDataTableur.grid(row=3, column=2, padx=20, pady=20)
        btnCloseTableur.grid(row=4, column=0, padx=20, pady=20)
        #btnReadTableur.grid(row=4, column=1, padx=20, pady=20)

        labelTitleNoOpenWord.grid(row=0, column=1, sticky="n")
        btnOpenWord.grid(row=2, column=1, sticky="n")

        labelTitleWord.grid(row=0, column=0, columnspan=3, sticky='ew')
        btnOpenWordWithComputer.grid(row=1, column=0, padx=20, pady=20)
        btnCloseWord.grid(row=1, column=1, padx=20, pady=20)
        btnWriteWord.grid(row=1, column=2, padx=20, pady=20)
        # btnReadWord.grid(row=2, column=0, padx=20, pady=20)

        # Placement des widgets dans la frame Projet
        labelTitleProjet.grid(row=0, column=0, columnspan=3, sticky='new')
        labelTitleNoOpenProjet.grid(row=0, column=1, sticky="n")
        btnOpenProjet.grid(row=2, column=0, sticky="n")
        btnCreateProjet.grid(row=2, column=2, sticky="n")

        # labelTitleProjet.grid(row=1, column=0, columnspan=3, pady=(10, 30))
        btnAddTypeProjet.grid(row=2, column=0, padx=5, pady=5)
        btnCreateFileProjet.grid(row=2, column=1, padx=5, pady=5)
        btnOpenFileProjet.grid(row=2, column=2, padx=5, pady=5)
        btnViewTaskProjet.grid(row=3, column=0, padx=5, pady=5)
        btnSayAllTaskProjet.grid(row=3, column=1, padx=5, pady=5)
        btnCloseProjet.grid(row=3, column=2, padx=5, pady=5)


    def activeAcceuil(self):
        self.__createWindows()
        self.__activeAcceuil()

    def activeProjet(self):
        self.__createWindows()
        self.__activeProjet()

    def activeTableur(self):
        self.__createWindows()
        self.__activeTableur()

    def activeWord(self):
        self.__createWindows()
        self.__activeWord()

    def __disabelFrame(self):
        self.__fAcceuil.grid_forget()
        self.__fDock.grid_forget()
        self.__fTableur.grid_forget()
        self.__fWord.grid_forget()
        self.__fProjet.grid_forget()
        self.__fTableurNoOpen.grid_forget()
        self.__fWordNoOpen.grid_forget()
        self.__fProjetNoOpen.grid_forget()

    def __activeAcceuil(self):
        self.__disabelFrame()
        self.__fAcceuil.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self._screen.update()

    def __activeTableur(self):
        self.__disabelFrame()
        if not self.__tableurOpen:
            self.__fTableurNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    def __activeWord(self):
        self.__disabelFrame()
        if not self.__wordOpen:
            self.__fWordNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fWord.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    def __activeProjet(self):
        self.__disabelFrame()

        if not self.__projectOpen:
            self.__fProjetNoOpen.grid(row=0, column=0, columnspan=3, sticky='nsew')
        else:
            self.__fProjet.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self._screen.update()

    # Partie fonctionnelle de l'application

    # Dock

    def __closeDock(self):
        if self.__projectOpen :
            self.__closeProjet()
        elif self.__tableurOpen :
            self.__closeTableur()
        elif self.__wordOpen :
            self.__closeWord()
        else :
            self.__activeAcceuil()

    def updateEtat(self):
        """
        Met à jour l'état des frames en fonction de l'ouverture des outils.
        """
        self.__wordOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatWord()
        self.__tableurOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatTableur()
        self.__projectOpen = self._gestionnaire.getGestFNC().getFNCWork().getEtatProject()

    # Partie Tableur
    def __openTableur(self):
        """
        Ouvre le tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableur()
        self.updateEtat()
        self.__activeTableur()

    def __readTableur(self):
        pass


    def __openTableurCoputerSoft(self):
        """
        Ouvre le tableur avec un logiciel de tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableurOs()

    def __closeTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().closeTableur()
        self.updateEtat()
        self.__activeTableur()

    def __addValeurTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addValeurOnTableur("A1","5")

    def __addMoyenneTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addMoyenneOnTableur("A1","A10","A11")

    def __addSommeTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addSommeOnTableur("A1","A10","A11")

    def __addComptageTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addComptageOnTableur("A1","A10","A11")

    def __addMinimumTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addMinimumOnTableur("A1","A10","A11")

    def __addMaximumTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().addMaximumOnTableur("A1","A10","A11")

    def __viewTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().getReadTableur()

    def __supprValeurTableur(self):
        self._gestionnaire.getGestFNC().getFNCWork().delValeur("A1")


    # Partie Word
    def __openWord(self):
        """
        Ouvre le document Word.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openWord()
        self.updateEtat()
        self.__activeWord()

    def __openWordCoputerSoft(self):
        """
        Ouvre le document Word avec un logiciel de traitement de texte.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openWordOs()

    def __closeWord(self):
        """
        Ferme le document Word.
        """
        self._gestionnaire.getGestFNC().getFNCWork().closeWord()
        self.updateEtat()
        self.__activeWord()

    def __writeWord(self):
        """
        Écrit dans le document Word.
        """
        self._gestionnaire.getGestFNC().getFNCWork().writeWord("")

    def __readWord(self):
        """
        Lit le document Word.
        """
        self._gestionnaire.getGestFNC().getFNCWork().readWord()
    # Partie Projet

    def __openProjet(self):
        """
        Ouvre le projet.
        """
        emplacementProjects = self._gestionnaire.getUserConf().getWorkFolder()

        dossier = askdirectory(initialdir=emplacementProjects,
                                          title="Selection du projet")
        dossier = (dossier.replace
                   (emplacementProjects,"").replace
                   ("/","").replace("\\","")).strip()
        self._gestionnaire.getGestFNC().getFNCWork().openProjet(dossier)
        self.updateEtat()
        self.__activeProjet()
        self.__nameProjet = dossier

    def __windowsTexteProjet(self,title:str, texte:str,fnc:callable):
        screen = self._arrtk.aTopLevel(width=225, height=100,resizable=False,title=title)
        self._arrtk.placeTopCenter(self._arrtk.createLabel(screen, text=texte,
                                                           ppolice="Arial", ptaille=15))
        self.__entryNameProjet = self._arrtk.createEntry(screen)
        self._arrtk.placeCenter(self.__entryNameProjet)
        self._arrtk.placeBottomCenter(self._arrtk.createButton(screen, text="Valider",
                                                               command= lambda :fnc(screen)))

    def __windowsNameNewProjet(self):
        """
        Crée un nouveau projet.
        """
        self.__windowsTexteProjet("Création d'un projet","Nom du nouveau projet",self.__createNewProjet)


    def __sayTaskProjet(self):
        """
        Ouvre une fenêtre pour dire une tâche dans le projet.
        """
        pass

    def __createNewProjet(self,screen:ctk.CTkToplevel):
        name = self.__entryNameProjet.get()
        screen.destroy()
        if not name:
            showerror("Erreur", "Le nom du projet ne peut pas être vide.")
            return

        self._gestionnaire.getGestFNC().getFNCWork().createProjet(name)
        self.updateEtat()
        self.__activeProjet()
        self.__nameProjet = name

    def __windowsTypeFileProjet(self):
        """
        Ouvre une fenêtre pour définir le type de fichier du projet.
        """
        self.__windowsTexteProjet("Type de fichier du projet",
                                  "Definir le type du projet",
                                  self.__setTypeFileProjet)

    def __setTypeFileProjet(self, screen: ctk.CTkToplevel):
        """
        Définit le type de fichier du projet.
        """
        type_file = self.__entryNameProjet.get()
        screen.destroy()
        if not type_file:
            showerror("Erreur", "Le type du projet ne peut pas être vide.")
            return

        self._gestionnaire.getGestFNC().getFNCWork().addTypeProjet(type_file)

    def __windowsCreateFileProjet(self):
        """
        Ouvre une fenêtre pour créer un fichier de projet.
        """
        listType = [" word","odt","txt",
                    "python","en tete","json",
                    "html","css","md","cpp",
                    "language c++","language c",
                    "exel","php","js","java","kt"]
        screen = ctk.CTkToplevel()
        screen.title("Création d'un fichier de projet")
        screen.geometry("300x200")
        screen.resizable(False, False)

        self.__var = StringVar(screen)

        self._arrtk.placeTopCenter(self._arrtk.createLabel(screen, text="Creation d'un fichier dans le projet",
                                                           ppolice="Arial", ptaille=15))
        self.__entryNameFile = self._arrtk.createEntry(screen)
        self._arrtk.placeLeftCenter(self.__entryNameFile)
        self._arrtk.placeRightCenter(self._arrtk.createOptionMenu(screen, value=listType, var=self.__var))
        self.__var.set(listType[0])
        self._arrtk.placeBottomCenter(self._arrtk.createButton(screen, text="Valider",
                                                               command=lambda: self.__createFileProjet(screen)))

    def __createFileProjet(self, screen: ctk.CTkToplevel):
        name_file = self.__entryNameFile.get()
        if not name_file:
            showerror("Erreur", "Imposible de créer un fichier sans nom.")
            return

        type_file = self.__var.get()
        screen.destroy()


    def __openFileProjet(self):
        """
        Ouvre un fichier de projet.
        """
        emplacementProjects = self._gestionnaire.getUserConf().getWorkFolder()+self.__nameProjet+"/"
        file_path = askopenfilename(initialdir=emplacementProjects,
                                               title="Selection du fichier du projet",
                                               filetypes=[("All files", "*.*")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.updateEtat()
            self.__activeProjet()

    def __openTaskProjet(self):
        """
        Ouvre une tâche dans le projet.
        """
        pass
        # A faire quand le GUI task sera fais et fonctionnel

    def __closeProjet(self):
        """
        Ferme le projet.
        """
        self._gestionnaire.getGestFNC().getFNCWork().closeProjet()
        self.updateEtat()
        self.__activeAcceuil()
        self.__nameProjet = None