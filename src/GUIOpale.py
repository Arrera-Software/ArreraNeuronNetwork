import tkinter
from tkinter.messagebox import showerror, askyesno
from librairy.dectectionOS import OS
from librairy.arrera_tk import *
from config.confNeuron import confNeuron
from brain.brain import ABrain
import signal
from datetime import datetime
import threading as th

class GUIOpale:
    def __init__(self):
        self.__arrTK = CArreraTK()
        self.__emplacementLangue = "language/vouvoiment/"
        self.__objOS = OS()
        self.__logContent = ""


    def active(self):
        self.__guiConf()
        self.__arrTK.view()

    def __guiConf(self):
        screen = self.__arrTK.aTK(width=500,height=500,
                                  title = "Opale",resizable=False,
                                  icon="asset/icon.png")
        self.__varService = tkinter.BooleanVar(value=True)
        self.__varTime = tkinter.BooleanVar(value=True)
        self.__varOpen = tkinter.BooleanVar(value=True)
        self.__varRecherche = tkinter.BooleanVar(value=True)
        self.__varChatbot = tkinter.BooleanVar(value=True)
        self.__varAPI = tkinter.BooleanVar(value=True)
        self.__varCodeHelp = tkinter.BooleanVar(value=True)
        self.__varWork = tkinter.BooleanVar(value=True)
        self.__varSocket = tkinter.BooleanVar(value=False)

        frameNeuron = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameLangue = self.__arrTK.createFrame(screen,width=500,height=225,wightBoder=True)
        frameValidate = self.__arrTK.createFrame(screen,width=500,height=50,wightBoder=True)
        # Widget FrameNeuron
        labelTitleNeuron = self.__arrTK.createLabel(screen,text="Gestion de neurone",ptaille=25)
        self.__checkService = ctk.CTkCheckBox(frameNeuron,text="Neuron\nservice",variable=self.__varService)
        self.__checkTime = ctk.CTkCheckBox(frameNeuron, text="Neuron\nTemps",variable=self.__varTime)
        self.__checkOpen = ctk.CTkCheckBox(frameNeuron, text="Neuron\nOpen",variable=self.__varOpen)
        self.__checkRecherche = ctk.CTkCheckBox(frameNeuron, text="Neuron\nRecherche",variable=self.__varRecherche)
        self.__checkChatbot = ctk.CTkCheckBox(frameNeuron, text="Neuron\nChatbots",variable=self.__varChatbot)
        self.__checkAPI = ctk.CTkCheckBox(frameNeuron, text="Neuron\nAPI",variable=self.__varAPI)
        self.__checkCodeHelp = ctk.CTkCheckBox(frameNeuron, text="Neuron\nCodeHelp",variable=self.__varCodeHelp)
        self.__checkWork = ctk.CTkCheckBox(frameNeuron, text="Neuron\nWork",variable=self.__varWork)
        self.__checkSocket = ctk.CTkCheckBox(frameNeuron, text="Utilisation des socket",variable=self.__varSocket)
        # Widget FrameLangue
        labelTitleLangue = self.__arrTK.createLabel(frameLangue,text="Gestion de la langue",ptaille=25)
        self.__langSet = self.__arrTK.createLabel(frameLangue,text="",ptaille=25)
        self.__btnVous = self.__arrTK.createButton(frameLangue,text="Vouvoiment",ptaille=20,command=lambda: self.__setLangue(1))
        self.__btnTutoiement = self.__arrTK.createButton(frameLangue,text="Tutoiement",ptaille=20,command=lambda: self.__setLangue(2))
        # Widget FrameValidate
        btnValidate = self.__arrTK.createButton(frameValidate, text="Valider", ptaille=25,
                                                command=lambda : self.__activateAssistantGUI(screen))
        # Affichage
        # FrameNeuron
        self.__arrTK.placeTopCenter(labelTitleNeuron)
        self.__checkService.place(x=10,  y=30,anchor="nw")
        self.__checkTime.place(x=130, y=30,anchor="nw")
        self.__checkOpen.place(x=260, y=30,anchor="nw")
        self.__checkRecherche.place(x=380, y=30,anchor="nw")
        self.__checkChatbot.place(x=10,  y=85,anchor="nw")
        self.__checkAPI.place(x=130, y=85,anchor="nw")
        self.__checkCodeHelp.place(x=260, y=85,anchor="nw")
        self.__checkWork.place(x=380, y=85,anchor="nw")
        self.__checkSocket.place(x=130, y=160,anchor="nw")
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
        # Thead Assistant
        self.__thAssistant = th.Thread()

    def __setLangue(self,mode:int):
        """
        1. Vouvoiement
        2. Tutoiement
        """
        match mode:
            case 1 :
                self.__emplacementLangue = "language/vouvoiment/"
                self.__langSet.configure(text="Vouvoiment")
            case 2 :
                self.__emplacementLangue = "language/tutoiment/"
                self.__langSet.configure(text="Tutoiement")
            case _ :
                self.__emplacementLangue = "language/vouvoiment/"
                self.__langSet.configure(text="Vouvoiment")
        self.__btnVous.place_forget()
        self.__btnTutoiement.place_forget()
        self.__arrTK.placeCenter(self.__langSet)

    def __setConfig(self):
        try :
            if (not self.__varService.get() and
                    not self.__varTime.get() and
                    not self.__varOpen.get() and
                    not self.__varRecherche.get() and
                    not self.__varChatbot.get() and
                    not self.__varAPI.get() and
                    not self.__varCodeHelp.get() and
                    not self.__varWork.get()):
                showerror("Assistant"," Vous devez activer au moins un neurone.")
                return False

            self.__config = confNeuron(name="Opale",
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
                                       etatService=int(self.__checkService.get()),
                                       etatTime=int(self.__checkTime.get()),
                                       etatOpen=int(self.__checkOpen.get()),
                                       etatSearch=int(self.__checkRecherche.get()),
                                       etatChatbot=int(self.__checkChatbot.get()),
                                       etatApi=int(self.__checkAPI.get()),
                                       etatCodehelp=int(self.__checkCodeHelp.get()),
                                       etatWork=int(self.__checkWork.get()),
                                       etatSocket=int(self.__checkSocket.get()),
                                       lienDoc="www.google.com",
                                       fichierLangue=str(self.__emplacementLangue),
                                       fichierKeyword="keyword/",
                                        voiceAssistant=True)
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
            if self.__startAssistantBrain():
                self.__GUIAssistant()
                self.__bootAssistant()
        else:
            print("Erreur lors de la création de la configuration de l'assistant.")


    def __GUIAssistant(self):
        screen = self.__arrTK.aTK(width=500, height=500,
                                  title="Opale Assistant", resizable=False,
                                  icon="asset/icon.png")

        screen.protocol("WM_DELETE_WINDOW", self.__close)

        # Frame
        frameAssistant = self.__arrTK.createFrame(screen, width=500, height=225)
        frameUser = self.__arrTK.createFrame(screen, width=350, height=50)

        # Widget
        labelTitle = self.__arrTK.createLabel(screen, text="Assistant Opale", ptaille=25)

        self.__labelAssistantText = self.__arrTK.createLabel(frameAssistant, text="TEXTE", ptaille=20)
        self.__labelAssistantNumber = self.__arrTK.createLabel(frameAssistant, text="NUMBER", ptaille=20)

        entryUser = self.__arrTK.createEntry(frameUser, width=200)
        btnSend = self.__arrTK.createButton(frameUser, text="Envoyer",ptaille=25,
                                            command= lambda : self.__sendAssistantMessage(entryUser,screen))
        btnOpen = self.__arrTK.createButton(screen, text="OPEN",width=10,command=self.__viewOpen)
        self.__labelGeneration = self.__arrTK.createLabel(screen,text="Generation...",ptaille=15)

        # Affichage

        self.__arrTK.placeTopCenter(labelTitle)
        self.__arrTK.placeCenter(frameAssistant)
        self.__arrTK.placeBottomCenterNoStick(frameUser)

        self.__arrTK.placeTopCenter(self.__labelAssistantText)
        self.__arrTK.placeBottomCenter(self.__labelAssistantNumber)

        self.__arrTK.placeLeftCenter(entryUser)
        self.__arrTK.placeRightCenter(btnSend)

        self.__arrTK.placeBottomLeft(btnOpen)

        self.__keyboard(screen,entryUser)

        screen.after(200, self.__updateAssistant,screen)

    def __viewOpen(self):
        w = self.__arrTK.aTopLevel(title="Ouvert par l'assistant",width=300, height=100)

        word = self.__arrTK.createLabel(w,text="WORD",ptaille=15)
        project = self.__arrTK.createLabel(w,text="PROJECT",ptaille=15)
        tableur = self.__arrTK.createLabel(w,text="TABLEUR",ptaille=15)

        self.__arrTK.placeCenterLeft(word)
        self.__arrTK.placeCenterRight(project)
        self.__arrTK.placeCenter(tableur)

        if self.__assistantBrain.getWord():
            word.configure(fg_color="green")
        else:
            word.configure(fg_color="red")

        if self.__assistantBrain.getProject():
            project.configure(fg_color="green")
        else:
            project.configure(fg_color="red")

        if self.__assistantBrain.getTableur():
            tableur.configure(fg_color="green")
        else:
            tableur.configure(fg_color="red")


    def __startAssistantBrain(self):
        try :
            self.__assistantBrain = ABrain(config=self.__config)
            return True
        except Exception as e:
            print(f"Erreur lors du démarrage de l'assistant Brain : {e}")
            return False

    def __bootAssistant(self):
        """
        Fonction qui permet de lancer l'assistant
        """

        try :
            self.__labelAssistantText.configure(text=self.__assistantBrain.boot(), wraplength=200
                                                ,justify=LEFT)
        except Exception as e:
            self.__labelAssistantText.configure(text=f"Erreur lors du boot de l'assistant : {e}",wraplength=200
                                                ,justify=LEFT)

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

    def __keyboard(self,win:ctk.CTk,entry:ctk.CTkEntry):
        def anychar(event):
            if self.__objOS.osWindows():
                if event.keycode == 13:
                    self.__sendAssistantMessage(entry,win)
            elif self.__objOS.osLinux():
                if event.keycode == 36:
                    self.__sendAssistantMessage(entry,win)
            elif self.__objOS.osMac():
                if event.keycode == 603979789:
                    self.__sendAssistantMessage(entry,win)
        win.bind("<Key>", anychar)

    def __close(self):
        out = askyesno("Fermeture","Enregistrer le log avant de quitter ?")
        self.__assistantBrain.shutdown()
        if out:
            if self.__saveLog():
                print("Log sauvegardé avec succès.")
            else:
                print("Erreur lors de la sauvegarde du log.")

        if self.__objOS.osWindows():
            os.kill(os.getpid(), signal.SIGINT)
        elif self.__objOS.osLinux() or self.__objOS.osMac() :
            os.kill(os.getpid(), signal.SIGKILL)

    def __addLog(self,nbOut:int,outTexte:str,inTexte:str):
        self.__logContent += inTexte + " -> " + str(nbOut) + " : " + outTexte + "\n"

    def __saveLog(self):
        date = datetime.now().strftime("%d-%m-%Y-%H-%M")
        file = "log/log_" + date + ".txt"
        try :
            with open(file,"w",encoding="utf-8") as f:
                f.write(self.__logContent)
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du log : {e}")
            return False


    def __updateAssistant(self,screen:ctk.CTk=None):

        if self.__assistantBrain.updateAssistant():
            varOut = self.__assistantBrain.getValeurSortie()
            self.__labelAssistantText.configure(text=self.__assistantBrain.getListSortie()[0], wraplength=200)
            self.__labelAssistantNumber.configure(text=str(varOut))
            if varOut == 15:
                self.__close()

        screen.after(1000,self.__updateAssistant,screen)