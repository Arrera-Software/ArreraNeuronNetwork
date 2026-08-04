import threading as th
from gestionnaire.gestion import *
from datetime import datetime, time


class ABrain :
    def __init__(self,config:confNeuron):
        # Declaration des diferente var
        self.__listOut =  [] 
        self.__valeurOut = 0
        self.__networkRunning = True
        self.__update = False
        self.__neuronUsed = str
        self.__listNeuron = ["chatBot","service","api",
                             "software","open","search",
                             "time","codehelp","word"]
        # Gestionnaire
        self.__gestionnaire = gestionnaire(config)
        self.__gestIA = self.__gestionnaire.getGestIA()
        if self.__gestionnaire.getUserConf().get_ia_model() != "":
            if not self.__gestIA.loadIA():
                raise Exception("Erreur critique : Impossible de charger le modèle IA.")
        self.__gestNeuron = self.__gestionnaire.getGestNeuron()
        # Partie serveur
        self.__gestSocket = self.__gestionnaire.getSocketObjet()
        #initilisation du gestionnaire du reseau de neuron
        self.__gestLangue = self.__gestionnaire.getLanguageObjet()
        #recuperation etat du reseau
        self.__etatReseau = self.__gestionnaire.getNetworkObjet().getEtatInternet()
        # Theard recevied message socket
        if self.__gestSocket is not None and self.__gestSocket.get_client_is_on():
            self.__threadSocket = th.Thread(target=self.__gestSocket.received_message_client)
            self.__threadSocket.daemon = True
            self.__threadSocket.start()


    def getGestionnaire(self):
        return self.__gestionnaire

    def getNeuronRunning(self):
        return self.__networkRunning

    def boot(self):
        return self.__gestionnaire.boot()
    
    def shutdown(self):
        hour = datetime.now().hour
        text = self.__gestLangue.aurevoir(hour)
        if self.__gestionnaire.getGestNeuron().getSocket():
            if self.__gestSocket.get_client_is_on():
                self.__gestSocket.stop_socket_client()

            if self.__gestSocket.get_server_is_on():
                self.__gestSocket.broadcast_data_with_server("closed")
                self.__gestSocket.stop_socket_server()
        self.__gestionnaire.getGestHist().saveHist()
        return str(text)
    
    def getListSortie(self)->list :
        if self.__valeurOut == 5 or self.__valeurOut == 12 or self.__valeurOut == 18 or self.__valeurOut == 19:
            if not self.__valeurOut == 12 or not self.__valeurOut == 18 or not self.__valeurOut == 19:
                texte = self.__getTextWithTkinterWindows()
                if texte is not None:
                    self.__listOut = texte

        if self.__valeurOut == 23 :
            self.__gestionnaire.getGestFNC().getFNCCodeHelp().launchGui()

        if self.__listOut == ["",""]:
            self.__listOut = [self.__gestLangue.nocomprehension(), ""]

        return self.__listOut

    def getNeuronUsed(self)-> type[str]:
        return self.__neuronUsed

    def getValeurSortie(self)->int :
        """
        0 : Aucun sortie
        1 : Sortie normale
        3 : Sortie actu
        4 : Meteo / temperature / GPS
        5 : Sortie avec fenetre tkinter
        6 : Erreur actu
        7 : Ouverture de fichier
        8 : Fermeture de fichier
        9 : Lecture fichier
        10 : Creation d'un projet
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        13 : Lecture tableur
        14 : Ouverture d'un projet
        15 : Arret de l'assistant
        16 : Creation d'un fichier dans un projet
        17 : Affichage aide
        18 : Resumer tache / agenda
        19 : Resumer all ok 
        20 : Resumer all fail
        21 : Close projet
        22 : Lancement de radio
        23 : GUI Codehelp
        """
        return self.__valeurOut

    def __getTextWithTkinterWindows(self):
        if self.__gestionnaire.getGestGUI().launch_gui():
            return [self.__gestionnaire.getGestGUI().textOut(),""]
        else :
            return None
    
    def getTableur(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatTableur()
    
    def getWord(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatWord()

    def getProject(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatProject()

    def getUserData(self):
        return self.__gestionnaire.getLanguageObjet().getDataUser()

    def neuron(self,var:str) :
        # Var local
        requette = self.__gestionnaire.netoyageChaine(str(var).lower())
        # Var de l'objet
        self.__valeurOut = 0
        self.__listOut =  []
        self.__neuronUsed = "none"

        intent = self.__gestionnaire.getGestIA().classify_intent(requette)
        mots_intent = intent.split(" ")

        # 1. Check pour arrêt complet
        if mots_intent[0] == "ARRET":
            self.__listOut = [self.shutdown(),""]
            self.__valeurOut = 15
            self.__neuronUsed = "core"
        elif mots_intent[0] != "COMPLEXE":
            # 2. Utilisation du core neuron (les intents rapides)
            self.__gestNeuron.ncore.neuron(intent, requette)
            self.__valeurOut = self.__gestNeuron.ncore.getValeurSortie()
            self.__listOut = self.__gestNeuron.ncore.getListSortie()
            self.__neuronUsed = "core"
        else:
            # 3. Utilisation du routeur IA complexe
            success = self.__gestNeuron.iarouter.route(requette)
            
            if success and self.__gestNeuron.iarouter.getValeurSortie() != 0:
                self.__valeurOut = self.__gestNeuron.iarouter.getValeurSortie()
                self.__listOut = self.__gestNeuron.iarouter.getListSortie()
                self.__neuronUsed = "IA"
            else:
                self.__valeurOut = 0
                self.__listOut = [self.__gestLangue.nocomprehension(), ""]


        #Sauvegarde de la sortie et de l'entrée
        if (self.__valeurOut == 3) or (self.__valeurOut == 12) or (self.__valeurOut == 11):
            self.__gestionnaire.setOld("requette api",requette)
        else :
            self.__gestionnaire.setOld(self.__listOut[0],requette)

    def updateAssistant(self):
        # print("updateAssistant")
        # Ajouter la partie mise a jour du socket
        self.__gestionnaire.updateDate()
        if (time(0,0) <= datetime.now().time() < time(11,0) and not
        self.__gestionnaire.get_state_morning_brief()):
            self.__gestionnaire.set_state_morning_brief()
            try:
                response = self.__gestIA.generate_final_response("","Annonce-lui que son brief du matin est prêt.")
                self.__listOut = [response if response else "Brief du matin prêt.",""]
            except Exception as e:
                print(f"Erreur generate_final_response morning: {e}")
                self.__listOut = ["Brief du matin prêt.",""]
            self.__gestionnaire.getGestGUI().active_morning_brief()
            self.__listOut = [self.__gestIA.generate_final_response("","Salue l'utilisateur et annonce-lui que son brief du matin est prêt."),""]
            self.__valeurOut = 5
            return True
        elif (time(11,0) <= datetime.now().time() < time(16,0) and not
        self.__gestionnaire.get_state_afternoon_brief()):
            self.__gestionnaire.set_state_afternoon_brief()
            self.__gestionnaire.getGestGUI().active_afternoon_brief()
            self.__listOut = [self.__gestIA.generate_final_response("","Salue l'utilisateur et annonce-lui que son brief de l'après-midi est prêt."),""]
            self.__valeurOut = 5
            return True
        elif (time(16,0) <= datetime.now().time() and not
        self.__gestionnaire.get_state_evening_brief()):
            self.__gestionnaire.set_state_evening_brief()
            self.__gestionnaire.getGestGUI().active_evening_brief()
            self.__listOut = [self.__gestIA.generate_final_response("","Salue l'utilisateur et annonce-lui que son brief de la soirée est prêt."),""]
            self.__valeurOut = 5
            return True
        elif self.__gestSocket is not None:
            if self.__gestSocket.get_new_client_is_connected():
                self.__listOut = ["soft connected",""]
                self.__valeurOut = 1
                return True
            elif self.__gestSocket.get_message_is_received_from_server():
                out = self.__gestSocket.get_message_from_server()
                client = out["client"]
                message = out["message"]
                if message != "Message Received" :
                    if client == "arrera_markdown":
                        self.__gestNeuron.nmarkdown.neurone(message)
                        self.__listOut = self.__gestNeuron.nmarkdown.getListSortie()
                        self.__valeurOut = self.__gestNeuron.nmarkdown.getValeurSortie()
                        return True
                    else :
                        return False
                else :
                    return False
            elif self.__gestSocket.get_message_is_received_form_client():
                if self.__gestionnaire.getKeywordObjet().checkInterface(
                        self.__gestSocket.get_message_form_client(), "requette"):
                    mots = self.__gestionnaire.getKeywordObjet().getListKeyword("interface","requette")
                    message = self.__gestSocket.get_message_form_client().replace(mots[0], "").strip()
                    self.neuron(message)
                    return True
                elif self.__gestionnaire.getKeywordObjet().checkInterface(self.__gestSocket.get_message_form_client(), "namemode"):
                    self.__gestionnaire.setNameMode(self.__gestSocket.get_message_form_client())
                    return False
                else:
                    message = self.__gestSocket.get_message_form_client()
                    self.__gestNeuron.ninterface.neurone(message)
                    self.__listOut = self.__gestNeuron.ninterface.getListSortie()
                    self.__valeurOut = self.__gestNeuron.ninterface.getValeurSortie()
                    return  True
            else :
                return False
        else :
            return False
