from gui.guibase import GuiBase,gestionnaire
from tkinter.filedialog import askdirectory,askopenfilename
from librairy.arrera_tk import *
from tkinter.messagebox import showerror, showinfo
from tkinter import StringVar
from gui.GUITaskProject import GUITaskProject

class GUIWork(GuiBase):
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
        # GUI
        self.__guiTaskProject = None


    def _mainframe(self):
        # var
        self.__listFormule = self._gestionnaire.getGestFNC().getFNCWork().getListFormuleTableur()
        self.__varFormule = StringVar(self._screen)
        # Conf de la fenetre
        self._screen.rowconfigure(0, weight=1)
        self._screen.rowconfigure(1, weight=0)
        self._screen.columnconfigure(0, weight=1)
        self._screen.columnconfigure(1, weight=2)
        self._screen.columnconfigure(2, weight=1)

        # Recuperation des image
        imgTableurAcceuil = aImage(path_light=self.__emplacementAsset + "acceuil/tableur.png",width=100, height=100)
        imgWordAcceuil = aImage(path_light=self.__emplacementAsset + "acceuil/word.png",
                                                 width=100, height=100)
        imgProjectAcceuil = aImage(path_light=self.__emplacementAsset + "acceuil/project.png",
                                                    width=100, height=100)

        imgTableurDock = aImage(path_light=self.__emplacementAsset + "acceuil/tableur.png",
                                                 width=50, height=50)
        imgWordDock = aImage(path_light=self.__emplacementAsset + "acceuil/word.png",
                                              width=50, height=50)
        imgProjectDock = aImage(path_light=self.__emplacementAsset + "acceuil/project.png",
                                                 width=50, height=50)
        imgAnnulerDock = aImage(path_light=self.__emplacementAsset + "acceuil/annuler.png",
                                                 width=50, height=50)

        # Images pour la frame Tableur
        imgAddComptage = aImage(path_light=self.__emplacementAsset + "tableur/add-comptagexcf.png",
                                                 width=90, height=90)
        imgAddMaxmum = aImage(path_light=self.__emplacementAsset + "tableur/add-maxmum.png",
                                               width=90, height=90)
        imgAddMinimum = aImage(path_light=self.__emplacementAsset + "tableur/add-minimum.png",
                                                width=90, height=90)
        imgAddMoyenne = aImage(path_light=self.__emplacementAsset + "tableur/add-moyenne.png",
                                                width=90, height=90)
        imgAddSomme = aImage(path_light=self.__emplacementAsset + "tableur/add-somme.png"
                                              , width=90, height=90)
        imgAddValeur = aImage(path_light=self.__emplacementAsset + "tableur/add-valeur.png"
                                               , width=90, height=90)
        imgCloseTableur = aImage(path_light=self.__emplacementAsset + "tableur/close-tableur.png"
                                                  , width=90, height=90)
        imgOpenTableur = aImage(path_light=self.__emplacementAsset + "tableur/open-tableur.png"
                                                 , width=90, height=90)
        imgOpenTableurCoputerSoft = aImage(path_light=self.__emplacementAsset + "tableur/open-tableur-coputer-soft.png"
                                                            , width=90, height=90)

        imgSupprValeur = aImage(path_light=self.__emplacementAsset + "tableur/suppr-valeur.png"
                                                 , width=90, height=90)
        imgViewTableur = aImage(path_light=self.__emplacementAsset + "tableur/view-tableur.png"
                                                 , width=90, height=90)

        # Images pour la frame Word
        imgOpenWord = aImage(path_light=self.__emplacementAsset + "word/open-word.png",
                                              width=90, height=90)
        imgOpenWordWithComputer = aImage(path_light=self.__emplacementAsset + "word/open-word-coputer-soft.png",
                                                          width=90, height=90)
        imgCloseWord = aImage(path_light=self.__emplacementAsset + "word/close-word.png",
                                               width=90, height=90)
        imgReadWord = aImage(path_light=self.__emplacementAsset + "word/read-word.png",
                                              width=90, height=90)

        imgWriteWord = aImage(path_light=self.__emplacementAsset + "word/write-word.png",
                                               width=90, height=90)

        # Images pour la frame Projet
        imgCreateFileProjet = aImage(path_light=self.__emplacementAsset + "project/create-file-project.png",
                                                      width=90, height=90)
        imgCreateProject = aImage(path_light=self.__emplacementAsset + "project/create-projet.png",
                                                   width=90, height=90)
        imgOpenFileProjet = aImage(path_light=self.__emplacementAsset + "project/open-file-project.png",
                                                    width=90, height=90)
        imgOpenProjet = aImage(path_light=self.__emplacementAsset + "project/open-project.png",
                                                width=90, height=90)
        imgSetTypeProjet = aImage(path_light=self.__emplacementAsset + "project/setType-project.png",
                                                   width=90, height=90)
        imgTaskSayProjet = aImage(path_light=self.__emplacementAsset + "project/task-say.png",
                                                   width=90, height=90)
        imgTaskViewProjet = aImage(path_light=self.__emplacementAsset + "project/view-task-project.png",
                                                    width=90, height=90)
        imgCloseProjet = aImage(path_light=self.__emplacementAsset + "project/close-project.png",
                                                 width=90, height=90)

        # Frames
        self.__fAcceuil = aFrame(self._screen)
        self.__fDock = aFrame(self._screen,height=70)
        self.__fTableur = aFrame(self._screen)
        self.__fTableurNoOpen = aFrame(self._screen)
        self.__fWord = aFrame(self._screen)
        self.__fWordNoOpen = aFrame(self._screen)
        self.__fProjet = aFrame(self._screen)
        self.__fProjetNoOpen = aFrame(self._screen)

        self.__frameManageTableur = aFrame(self._screen)
        self.__frameAddValeur = aFrame(self.__frameManageTableur)
        self.__frameAddFormule = aFrame(self.__frameManageTableur)
        self.__frameReadTableur = aFrame(self.__frameManageTableur)
        self.__frameDelValeurTableur = aFrame(self.__frameManageTableur)

        self.__frameManageWord = aFrame(self._screen)
        self.__fReadWord = aFrame(self.__frameManageWord)
        self.__fWriteWord = aFrame(self.__frameManageWord)

        # Widgets dans la frame d'accueil
        labelTitleAcceuil = aLabel(self.__fAcceuil, text=self._gestionnaire.getConfigFile().name + " : Arrera Work")
        btnArreraTableurAcceuil = aButton(self.__fAcceuil, width=100,height=100, image=imgTableurAcceuil,
                                                           command=self.__activeTableur,text="")
        btnArreraWordAcceuil = aButton(self.__fAcceuil, width=100,height=100, image=imgWordAcceuil,
                                                        command=self.__activeWord,text="")
        btnArreraProjectAcceuil = aButton(self.__fAcceuil, width=100,height=100, image=imgProjectAcceuil,
                                                           command=self.__activeProjet,text="")

        # Widgets dans la frame dock
        btnArreraTableurDock = aButton(self.__fDock, width=60,height=60, image=imgTableurDock,
                                                        command=self.__activeTableur,text="")
        btnArreraWordDock = aButton(self.__fDock, width=60,height=60, image=imgWordDock,
                                                     command=self.__activeWord,text="")
        btnArreraProjectDock = aButton(self.__fDock, width=60, image=imgProjectDock,
                                                        command=self.__activeProjet,text="")
        btnCloseAcceuilDock = aButton(self.__fDock, width=60,height=60, image =imgAnnulerDock,
                                                       command=self.__closeDock,text="")

        # Widgets du frame Tableur
        labelTitleNoOpenTableur = aLabel(self.__fTableurNoOpen, text="Travail sur un tableur")
        btnOpenTableur = aButton(self.__fTableurNoOpen, width=90, height=90,image=imgOpenTableur,command=self.__openTableur,text="")
        labelTitleTableur = aLabel(self.__fTableur, text="Travail sur un tableur")
        btnOpenTableurWithComputer = aButton(self.__fTableur, width=90, height=90,image=imgOpenTableurCoputerSoft,text="",command=self.__openTableurCoputerSoft)
        btnCloseTableur = aButton(self.__fTableur, width=90, height=90,image=imgCloseTableur,text="", command=self.__closeTableur)

        btnAddValeurTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddValeur,text="", command=self.__viewAddValeurTableur)
        btnAddMoyenneTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddMoyenne,text="", command=self.__viewMoyenneTableur)
        btnAddSommeTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddSomme,text="", command=self.__viewSommeTableur)
        btnAddComptageTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddComptage,text="", command=self.__viewComptageTableur)
        btnAddMinimumTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddMinimum,text="", command=self.__viewMinimumTableur)
        btnAddMaximumTableur = aButton(self.__fTableur, width=90, height=90,image=imgAddMaxmum,text="", command=self.__viewMaximumTableur)
        btnAffichageTableur = aButton(self.__fTableur, width=90, height=90,image=imgViewTableur,text="", command=self.__readTableur)
        btnSupprDataTableur = aButton(self.__fTableur, width=90, height=90,image=imgSupprValeur,text="",command=self.__viewDelValeurTableur)

        # Widgets dans la frame Word
        labelTitleNoOpenWord = aLabel(self.__fWordNoOpen, text="Travail sur un document Word")
        btnOpenWord = aButton(self.__fWordNoOpen, width=90, height=90, image=imgOpenWord,text="",command=self.__openWord)

        labelTitleWord = aLabel(self.__fWord, text="Travail sur un document Word")
        btnOpenWordWithComputer = aButton(self.__fWord, width=90, height=90,image=imgOpenWordWithComputer,text="", command=self.__openWordCoputerSoft)
        btnEditWord = aButton(self.__fWord, width=90, height=90, image=imgWriteWord,text="",command=self.__viewEditWord)
        btnViewReadWord = aButton(self.__fWord, width=90, height=90,image=imgReadWord,text="", command=self.__viewReadWord)

        btnCloseWord = aButton(self.__fWord, width=90, height=90,image=imgCloseWord,text="", command=self.__closeWord)

        # Manage Word
        labelTitleReadWord = aLabel(self.__fReadWord, text="Lecture du document Word")
        self.__textReadWord = aTextScrollable(self.__fReadWord)
        btnQuitReadWord = aButton(self.__fReadWord,text="Quitter",command=self.__quitReadWord)
        btnReadWord = aButton(self.__fReadWord,text="Lire",command=self.__readWord)

        labelEditWord = aLabel(self.__fWriteWord, text="Ecriture dans le document Word")
        self.__textEditWord = aTextScrollable(self.__fWriteWord)
        btnQuitEditWord = aButton(self.__fWriteWord,text="Quitter",command=self.__quitEditWord)
        btnWriteWord = aButton(self.__fWriteWord,text="Ecrire",command=self.__writeWord)



        # Widget dans la frame Projet
        # No OPEN
        labelTitleNoOpenProjet = aLabel(self.__fProjetNoOpen, text="Travail sur un projet")

        btnOpenProjet = aButton(self.__fProjetNoOpen, width=90, height=90,image=imgOpenProjet,text="",command=self.__openProjet)

        btnCreateProjet = aButton(self.__fProjetNoOpen, width=90, height=90,image=imgCreateProject,text="",command=self.__windowsNameNewProjet)

        # OPEN
        labelTitleProjet = aLabel(self.__fProjet, text="Travail sur un projet")
        btnAddTypeProjet = aButton(self.__fProjet, width=90, height=90,image=imgSetTypeProjet,text="", command=self.__windowsTypeFileProjet)
        btnCreateFileProjet = aButton(self.__fProjet, width=90, height=90, image=imgCreateFileProjet,text="",command=self.__windowsCreateFileProjet)
        btnOpenFileProjet = aButton(self.__fProjet, width=90, height=90, image=imgOpenFileProjet,text="",command=self.__openFileProjet)
        btnViewTaskProjet = aButton(self.__fProjet, width=90, height=90, image=imgTaskViewProjet,text="",command=self.openTaskProjet)
        btnSayAllTaskProjet = aButton(self.__fProjet, width=90, height=90,image=imgTaskSayProjet,text="", command=self.__sayTaskProjet)

        btnCloseProjet = aButton(self.__fProjet, width=90, height=90, image=imgCloseProjet,text="",command=self.__closeProjet)

        # frameTableurAdd
        # frameAddValeur
        labelTitleAddValeur = aLabel(self.__frameAddValeur, text="Ajout d'une valeur")
        self.__eCaseAddValeur = aEntryLengend(self.__frameAddValeur,text="Case de la valeur : ",gridUsed=True)
        self.__eValueAddValeur = aEntryLengend(self.__frameAddValeur,text="Valeur : ",gridUsed=True)
        btnAddValeur = aButton(self.__frameAddValeur,text="Ajouter la valeur",command=self.__addValeurTableur)
        btnCancelAddValeur = aButton(self.__frameAddValeur,text="Annuler",command=self.__disableManageTableur)
        # frameAddFormule
        lTitleAddFormule = aLabel(self.__frameAddFormule, text="Ajout d'une formule")
        self.__menuChoixFormule = aOptionMenu(self.__frameAddFormule,value=self.__listFormule)

        self.__eCaseStartFormule = aEntryLengend(self.__frameAddFormule,text="Case de debut : ",gridUsed=True)
        self.__eCaseEndFormule = aEntryLengend(self.__frameAddFormule,text="Case de fin : ",gridUsed=True)
        self.__eCaseDestFormule = aEntryLengend(self.__frameAddFormule,text="Case de destination : ",gridUsed=True)

        btnAddFormule = aButton(self.__frameAddFormule,text="Ajouter la formule",command=self.__addFormuleTableur)
        btnCancelAddFormule = aButton(self.__frameAddFormule,text="Annuler",command=self.__disableManageTableur)
        # frameReadTableur
        labelTitleReadTableur = aLabel(self.__frameReadTableur, text="Lecture du tableur")
        self.__fScrolledRead = aScrollableFrame(self.__frameReadTableur)
        btnQuitReadTableur = aButton(self.__frameReadTableur,text="Quitter",command=self.__disableManageTableur)
        # frameDelValeurTableur
        labelTitleDelTableur = aLabel(self.__frameDelValeurTableur, text="Suppression de valeur")
        self.__eCaseDel = aEntryLengend(self.__frameDelValeurTableur,text="Case a supprimer : ",gridUsed=True)
        btnDelTableur = aButton(self.__frameDelValeurTableur,text="Supprimer la valeur",command=self.__delValeurTableur)
        btnCancelDebTableur = aButton(self.__frameDelValeurTableur,text="Annuler",command=self.__disableManageTableur)

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

        self.__frameManageTableur.grid_rowconfigure(0, weight=1)
        self.__frameManageTableur.grid_columnconfigure(0, weight=1)

        self.__frameAddValeur.columnconfigure(0, weight=1)
        self.__frameAddValeur.columnconfigure(1, weight=1)
        self.__frameAddValeur.rowconfigure(1, minsize=5)
        self.__frameAddValeur.rowconfigure(4, weight=1)

        self.__frameAddFormule.columnconfigure(0, weight=1)
        self.__frameAddFormule.columnconfigure(1, weight=1)
        self.__frameAddFormule.rowconfigure(5, weight=1)

        self.__frameReadTableur.columnconfigure(0, weight=1)
        self.__frameReadTableur.rowconfigure(1, weight=1)

        self.__frameDelValeurTableur.columnconfigure(0, weight=1)
        self.__frameDelValeurTableur.columnconfigure(1, weight=1)
        self.__frameDelValeurTableur.rowconfigure(1, weight=1)
        self.__frameDelValeurTableur.rowconfigure(3, weight=1)

        self.__frameManageWord.grid_rowconfigure(0, weight=1)
        self.__frameManageWord.grid_columnconfigure(0, weight=1)

        self.__fReadWord.grid_columnconfigure(0, weight=1, uniform="buttons")
        self.__fReadWord.grid_columnconfigure(1, weight=1, uniform="buttons")
        self.__fReadWord.grid_rowconfigure(0, weight=0)
        self.__fReadWord.grid_rowconfigure(1, weight=1)
        self.__fReadWord.grid_rowconfigure(2, weight=0)

        self.__fWriteWord.grid_columnconfigure(0, weight=1, uniform="buttons")
        self.__fWriteWord.grid_columnconfigure(1, weight=1, uniform="buttons")
        self.__fWriteWord.grid_rowconfigure(0, weight=0)
        self.__fWriteWord.grid_rowconfigure(1, weight=1)
        self.__fWriteWord.grid_rowconfigure(2, weight=0)


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
        btnViewReadWord.grid(row=1, column=0, padx=20, pady=20)
        btnEditWord.grid(row=1, column=1, padx=20, pady=20)
        btnOpenWordWithComputer.grid(row=1, column=2, padx=20, pady=20)
        btnCloseWord.grid(row=2, column=0, padx=20, pady=20)

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

        labelTitleAddValeur.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 20))
        self.__eCaseAddValeur.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 10))
        self.__eValueAddValeur.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20)
        btnCancelAddValeur.grid(row=5, column=0, sticky="sw", padx=10, pady=10)
        btnAddValeur.grid(row=5, column=1, sticky="se", padx=10, pady=10)

        lTitleAddFormule.grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 6))
        self.__menuChoixFormule.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 10))
        self.__eCaseStartFormule.grid(row=2, column=0, columnspan=2, sticky="ew", padx=12, pady=(0, 6))
        self.__eCaseEndFormule.grid(row=3, column=0, columnspan=2, sticky="ew", padx=12, pady=(0, 6))
        self.__eCaseDestFormule.grid(row=4, column=0, columnspan=2, sticky="ew", padx=12)
        btnCancelAddFormule.grid(row=6, column=0, sticky="sw", padx=10, pady=10)
        btnAddFormule.grid(row=6, column=1, sticky="se", padx=10, pady=10)

        labelTitleReadTableur.grid(row=0, column=0, sticky="new", padx=10, pady=(10, 8))
        self.__fScrolledRead.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
        btnQuitReadTableur.grid(row=2, column=0, sticky="sew", padx=10, pady=10)

        labelTitleDelTableur.grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=(10, 8))
        self.__eCaseDel.grid(row=2, column=0, columnspan=2, padx=12, pady=6)
        btnCancelDebTableur.grid(row=4, column=0, sticky="sw", padx=10, pady=10)
        btnDelTableur.grid(row=4, column=1, sticky="se", padx=10, pady=10)

        labelTitleReadWord.grid(row=0, column=0, columnspan=2, sticky="ew",padx=8, pady=(8, 4))
        self.__textReadWord.grid(row=1, column=0, columnspan=2, sticky="nsew",padx=8, pady=4)
        btnQuitReadWord.grid(row=2, column=0, sticky="ew",padx=(8, 4), pady=(4, 8))
        btnReadWord.grid(row=2, column=1, sticky="ew",padx=(4, 8), pady=(4, 8))

        labelEditWord.grid(row=0, column=0, columnspan=2, sticky="ew",padx=8, pady=(8, 4))
        self.__textEditWord.grid(row=1, column=0, columnspan=2, sticky="nsew",padx=8, pady=4)
        btnQuitEditWord.grid(row=2, column=0, sticky="ew",padx=(8, 4), pady=(4, 8))
        btnWriteWord.grid(row=2, column=1, sticky="ew",padx=(4, 8), pady=(4, 8))


    def activeProjet(self):
        self.active()
        self._mainframe()
        self.__activeProjet()

    def activeTableur(self):
        self.active()
        self._mainframe()
        self.__activeTableur()

    def activeWord(self):
        self.active()
        self._mainframe()
        self.__activeWord()

    def activeAcceuil(self):
        self.active()
        self._mainframe()
        self.__activeAcceuil()

    # Active pour le tableur

    def activeManageTableur(self,mode:int):
        """
        1. Add Valeur
        2. Add Somme
        3. Add Moyenne
        4. Add Comptage
        5. Add Minimum
        6. Add Maximum
        7. Suppr valeur
        """
        self.active()
        self.updateEtat()
        if not self.__tableurOpen:
            return False

        match mode :
            case 1 :
                self.__viewAddValeurTableur()
                return True
            case 2 :
                self.__viewSommeTableur()
                return True
            case 3 :
                self.__viewMoyenneTableur()
                return True
            case 4 :
                self.__viewComptageTableur()
                return True
            case 5 :
                self.__viewMinimumTableur()
                return True
            case 6 :
                self.__viewMaximumTableur()
                return True
            case 7 :
                self.__viewDelValeurTableur()
                return True
            case _ :
                return False

    def activeReadWord(self):
        self.active()
        self.updateEtat()
        if not self.__wordOpen:
            return False
        self.__viewReadWord()
        return True

    def activeWriteWord(self):
        self.active()
        self.updateEtat()
        if not self.__wordOpen:
            return False
        self.__viewEditWord()
        return True

    def activeReadTableur(self):
        self.active()
        self.updateEtat()
        if not self.__tableurOpen:
            return False
        self.__readTableur()
        return True

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
        if self.__projectOpen:
            self.__nameProjet = self._gestionnaire.getGestFNC().getFNCWork().getNameProjet()
            self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                   self.__nameProjet,
                                                   self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())
        else :
            self.__nameProjet = None
            self.__guiTaskProject = None

    # Partie Tableur
    def __openTableur(self):
        """
        Ouvre le tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableur()
        self.updateEtat()
        self.__activeTableur()

    def __openTableurCoputerSoft(self):
        """
        Ouvre le tableur avec un logiciel de tableur.
        """
        self._gestionnaire.getGestFNC().getFNCWork().openTableurOs()

    def __closeTableur(self):
        self.__disableManageTableur()
        self._gestionnaire.getGestFNC().getFNCWork().closeTableur()
        self.updateEtat()
        self.__activeTableur()

    def __viewAddValeurTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameAddValeur.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.__eCaseAddValeur.getEntry().delete(0,ctk.END)
        self.__eValueAddValeur.getEntry().delete(0,ctk.END)
        self._screen.update()

    def __addValeurTableur(self):
        case = self.__eCaseAddValeur.getEntry().get()
        valeur = self.__eValueAddValeur.getEntry().get()
        if not case or not valeur:
            showerror("Erreur", "La case et la valeur ne peuvent pas être vide.")
            return
        if self._gestionnaire.getGestFNC().getFNCWork().addValeurOnTableur(case,valeur):
            showinfo("Succès", f"La valeur {valeur} a été ajoutée à la case {case}.")
            self.__disableManageTableur()
        else:
            showerror("Erreur", "Une erreur est survenue lors de l'ajout de la valeur.")
            self.__disableManageTableur()

    def __viewAddFormuleTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameAddFormule.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.__eCaseDestFormule.getEntry().delete(0,ctk.END)
        self.__eCaseEndFormule.getEntry().delete(0,ctk.END)
        self.__eCaseStartFormule.getEntry().delete(0,ctk.END)

    def __viewMoyenneTableur(self):
        self.__viewAddFormuleTableur()
        self.__menuChoixFormule.set(self.__listFormule[1])
        self._screen.update()

    def __viewSommeTableur(self):
        self.__viewAddFormuleTableur()
        self.__menuChoixFormule.set(self.__listFormule[0])
        self._screen.update()

    def __viewComptageTableur(self):
        self.__viewAddFormuleTableur()
        self.__menuChoixFormule.set(self.__listFormule[2])
        self._screen.update()

    def __viewMinimumTableur(self):
        self.__viewAddFormuleTableur()
        self.__menuChoixFormule.set(self.__listFormule[3])
        self._screen.update()

    def __viewMaximumTableur(self):
        self.__viewAddFormuleTableur()
        self.__menuChoixFormule.set(self.__listFormule[4])
        self._screen.update()

    def __addFormuleTableur(self):
        caseDest = self.__eCaseDestFormule.getEntry().get()
        caseEnd = self.__eCaseEndFormule.getEntry().get()
        caseStart = self.__eCaseStartFormule.getEntry().get()
        formule = self.__menuChoixFormule.get()

        if not caseDest or not caseEnd or not caseStart or not formule:
            showerror("Erreur", "Les cases et la formule ne peuvent pas être vide.")
            return

        if formule == self.__listFormule[0]:
            if self._gestionnaire.getGestFNC().getFNCWork().addSommeOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule SOMME a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout de la somme.")
        elif formule == self.__listFormule[1]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMoyenneOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MOYENNE a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout de la moyenne.")
        elif formule == self.__listFormule[2]:
            if self._gestionnaire.getGestFNC().getFNCWork().addComptageOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule COMPTAGE a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du comptage.")
        elif formule == self.__listFormule[3]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMinimumOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MINIMUM a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du minimum.")
        elif formule == self.__listFormule[4]:
            if self._gestionnaire.getGestFNC().getFNCWork().addMaximumOnTableur(caseStart,caseEnd,caseDest):
                showinfo("Succès", f"La formule MAXIMUM a été ajoutée à la case {caseDest}.")
            else:
                showerror("Erreur", "Une erreur est survenue lors de l'ajout du maximum.")
        else :
            showerror("Erreur", "La formule sélectionnée n'est pas valide.")

        self.__disableManageTableur()


    def __readTableur(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readTableur():
            self.__disabelFrame()
            self.__disableManageTableur()
            self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self.__frameReadTableur.grid(row=0, column=0, sticky="nsew")
            self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

            for w in self.__fScrolledRead.winfo_children():
                w.destroy()

            data = self._gestionnaire.getGestFNC().getFNCWork().getReadTableur()
            if not data:
                lbl = aLabel(self.__fScrolledRead, text="Le tableur est vide.")
                lbl.pack(pady=10)
            else:
                for row in data:
                    lbl = aLabel(self.__fScrolledRead, text=row+"\n")
                    lbl.configure(anchor="w")
                    lbl.pack(side="top", anchor="w", fill="x", padx=5, pady=2)

        else :
            self.__disabelFrame()
            self.__disableManageTableur()




    def __viewDelValeurTableur(self):
        self.__disabelFrame()
        self.__disableManageTableur()
        self.__frameManageTableur.grid(row=0, column=0, columnspan=3, sticky='nsew')
        self.__frameDelValeurTableur.grid(row=0, column=0, sticky="nsew")
        self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.__eCaseDel.delete(0,ctk.END)
        self._screen.update()

    def __delValeurTableur(self):
        case = self.__eCaseDel.get()
        if not case:
            showerror("Erreur", "La case ne peut pas être vide.")
            return
        if self._gestionnaire.getGestFNC().getFNCWork().delValeur(case):
            showinfo("Succès", f"La valeur de la case {case} a été supprimée.")

        self.__disableManageTableur()

    def __disableManageTableur(self):
        self.__frameManageTableur.grid_forget()
        self.__frameAddValeur.grid_forget()
        self.__frameAddFormule.grid_forget()
        self.__frameReadTableur.grid_forget()
        self.__frameDelValeurTableur.grid_forget()
        self.__fDock.grid_forget()
        self.__disabelFrame()
        self.__activeTableur()


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
        self.__disableManageWord()
        self._gestionnaire.getGestFNC().getFNCWork().closeWord()
        self.updateEtat()
        self.__activeWord()

    def __viewEditWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():

            self.__disabelFrame()
            self.__disableManageWord()
            self.__frameManageWord.grid(row=0, column=0, columnspan=3, sticky='nsew')
            self.__fWriteWord.grid(row=0, column=0, sticky="nsew")
            self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
            self.__textEditWord.enableTextBox()

            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self.__textEditWord.getTextBox().delete(1.0, ctk.END)
                self.__textEditWord.getTextBox().insert(ctk.END, text)
        else :
            showinfo("Erreur", "Une erreur est survenue.")

    def __writeWord(self):
        newTexte = self.__textEditWord.getTextBox().get(1.0, ctk.END)
        if self._gestionnaire.getGestFNC().getFNCWork().writeWordEcrase(newTexte):
            showinfo("Succès", "Le document a été mis à jour.")
        else :
            showerror("Erreur", "Une erreur est survenue lors de la mise à jour du document.")
        self.__disableManageWord()

    def __quitEditWord(self):
        self.__disableManageWord()

    def __viewReadWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():
            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self.__disabelFrame()
                self.__disableManageWord()
                self.__frameManageWord.grid(row=0, column=0, columnspan=3, sticky='nsew')
                self.__fReadWord.grid(row=0, column=0, sticky="nsew")
                self.__fDock.grid(row=1, column=0, columnspan=3, sticky='ew')
                self.__textReadWord.enableTextBox()
                self.__textReadWord.getTextBox().delete(1.0, ctk.END)
                self.__textReadWord.getTextBox().insert(ctk.END, text)
                self.__textReadWord.disableTextBox()
            else :
                showinfo("Info", "Le document est vide.")
        else :
            showinfo("Erreur", "Une erreur est survenue lors de la lecture du document.")

    def __quitReadWord(self):
        self.__disableManageWord()

    def __readWord(self):
        if self._gestionnaire.getGestFNC().getFNCWork().readWord():
            text = self._gestionnaire.getGestFNC().getFNCWork().getReadWord()
            if text :
                self._gestionnaire.getArrVoice().say(text)
            else :
                showinfo("Info", "Le document est vide.")
        else :
            showinfo("Erreur", "Une erreur est survenue lors de la lecture du document.")

    def __disableManageWord(self):
        self.__frameManageWord.grid_forget()
        self.__fReadWord.grid_forget()
        self.__fWriteWord.grid_forget()
        self.__fDock.grid_forget()
        self.__disabelFrame()
        self.__activeWord()


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
        self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                  self.__nameProjet,
                                                  self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

    def __windowsTexteProjet(self,title:str, texte:str,fnc:callable):
        screen = self._arrtk.aTopLevel(width=225, height=100,resizable=False,title=title)
        aLabel(screen, text=texte).placeTopCenter()
        self.__entryNameProjet = aEntry(screen)
        self.__entryNameProjet.placeCenter()
        aButton(screen, text="Valider",command= lambda :fnc(screen)).placeBottomCenter()

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
        self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                               self.__nameProjet,
                                               self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

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

        aLabel(screen, text="Creation d'un fichier dans le projet").placeTopCenter()
        self.__entryNameFile = aEntry(screen)
        self.__entryNameFile.placeLeftCenter()
        self._arrtk.placeRightCenter(self._arrtk.createOptionMenu(screen, value=listType, var=self.__var))
        self.__var.set(listType[0])
        aButton(screen, text="Valider",command=lambda: self.__createFileProjet(screen)).placeBottomCenter()

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
            self.__guiTaskProject = GUITaskProject(self._gestionnaire,
                                                   self.__nameProjet,
                                                   self._gestionnaire.getGestFNC().getFNCWork().getFNCTaskProjet())

    def openTaskProjet(self):
        """
        Ouvre une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.active()
            return True
        else :
            return False

    def openTaskProjetAdd(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeAdd()
            return True
        else :
            return False


    def openTaskProjetdel(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeDel()
            return True
        else :
            return False

    def openTaskProjetfinish(self):
        """
        Ouvre une fenêtre pour ajouter une tâche dans le projet.
        """
        self.updateEtat()
        if self.__guiTaskProject is not None :
            self.__guiTaskProject.activeFinish()
            return True
        else :
            return False


    def __closeProjet(self):
        """
        Ferme le projet.
        """
        self._gestionnaire.getGestFNC().getFNCWork().closeProjet()
        self.__activeAcceuil()
        self.__nameProjet = None
        del self.__guiTaskProject
        self.__guiTaskProject = None
        self.updateEtat()