from gestionnaire.gestion import gestionnaire
from librairy.ArreraIALoad import ArreraIALoad
from librairy.model_downloader import *

class gestIA :
    def __init__(self,gestionnaire:gestionnaire):

        self.__gestionnaire =  gestionnaire

        self.__ia_mode_enabled = False
        self.__ia_loader = None

        self.__reponse_ia = ""
        self.__confidence_ia = 0.0

        self.__model_reponse_ok = False

        self.loadIA()

    def loadIA(self):
        user_conf = self.__gestionnaire.getUserConf()
        model_name = user_conf.get_ia_model()

        if user_conf.get_use_ia() == 1 and model_name !="":
            try :
                self.__ia_loader= ArreraIALoad()
                self.__ia_loader.load_model_gguf(model_name)
                self.__ia_mode_enabled = True
            except Exception as e :
                # print(e)
                self.__ia_mode_enabled = False

            self.__ia_mode_enabled = True
        else :
            self.__ia_mode_enabled = False

    def send_request_ia(self,requette:str):
        if self.__ia_mode_enabled:
            try :
                self.__reponse_ia, self.__confidence_ia = self.__ia_loader.send_request(requette)
                self.__model_reponse_ok = True
                return True
            except Exception as e :
                self.__model_reponse_ok = False
                return False
        else :
            self.__model_reponse_ok = False
            return False

    def __state_ia_reponse(self):
        return self.__model_reponse_ok

    def get_reponse_ia(self):
        return self.__reponse_ia

    def get_confidence_ia(self):
        return self.__confidence_ia