from tkinter import*
import webbrowser as w
from github import Github
import requests
from gui.codehelp.CCHguiBase import CCHguiBase,gestionnaire
from librairy.arrera_tk import *

class CHGithub(CCHguiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Github")
        self.__tokenGithub = self._gestionnaire.getUserConf().getTokenGithub()
        self.__listDepo = []

    def _mainframe(self):
        #Frame
        self.__frameWelcome = aFrame(self._screen, width=500, height=500)
        self.__frameSearch = aFrame(self._screen, width=500, height=500)
        self.__frameError = aFrame(self._screen, width=500, height=500)
        self.__frameList = aFrame(self._screen, width=500, height=500)
        # Label
        labelWelcome = aLabel(self.__frameWelcome, text="GitHub")
        labelError = aLabel(self.__frameError,text="Aucun token enregistrer\nRendez-vous\ndans les parametre pour\nl'enregistrer")
        labelSearch = aLabel(self.__frameSearch, text="Recherche sur Github")
        # BTN
        btnWelcomeDirectory = aButton(self.__frameWelcome, text="Vos depot",command=self.__GUIListDepos)
        btnWelcomeSearch = aButton(self.__frameWelcome, text="Recherche",command=self.__GUISearch)
        btnValidateSearch = aButton(self.__frameSearch, text="Valider", command=self.__search)
        btnBackSearch = aButton(self.__frameSearch, text="Retour",command=self.__backMain)
        btnErrorDirectory = aButton(self.__frameError, text="Quitter", command=self.__backMain)
        btnListQuit = aButton(self.__frameList, text="Quitter",command=self.__backMain)
        #scrollbar
        self.__scroll = Scrollbar(self.__frameList,orient="vertical")
        #Entry
        self.__entrySearch = aEntry(self.__frameSearch,width=400)
        # Listbox
        self.__boxlistDepot = Listbox(self.__frameList, width=500, height=500)
        #Affichage
        self._arrtk.placeTopCenter(labelWelcome)
        self._arrtk.placeLeftCenter(btnWelcomeDirectory)
        self._arrtk.placeRightCenter(btnWelcomeSearch)
        self._arrtk.placeTopCenter(labelSearch)
        self._arrtk.placeCenter(self.__entrySearch)
        self._arrtk.placeBottomRight(btnValidateSearch)
        self._arrtk.placeBottomLeft(btnBackSearch)
        self._arrtk.placeCenter(labelError)
        self._arrtk.placeBottomCenter(btnErrorDirectory)
        self._arrtk.placeBottomCenter(btnListQuit)
        self.__boxlistDepot.place(relx=0, rely=0, relwidth=0.95, relheight=1)
        self.__scroll.place(relx=0.95, rely=0, relwidth=0.05, relheight=1)
        self._arrtk.placeCenter(self.__frameWelcome)

    def search(self,requette:str):
        urllink = requests.get("https://github.com/search?q="+requette)
        urllink = urllink.url
        w.open(urllink)
    
    def __GUISearch(self):
        self.__frameWelcome.place_forget()
        self.__frameSearch.place(relx=0.5,rely=0.5,anchor="center")
    
    def __search(self):
        self.__frameWelcome.place(relx=0.5, rely=0.5, anchor="center")
        self.__frameSearch.place_forget()
        self.search(str(self.__entrySearch.get()))
        self.__entrySearch.delete("0", END)

    def __setListDepos(self)->bool:
        if self.__tokenGithub :
            access = Github(self.__tokenGithub)
            for repo in access.get_user().get_repos():
                self.__listDepo.append(str(repo.name))
            return True
        else :
            return False
    
    def __backMain(self):
        self.__frameList.place_forget()
        self.__frameError.place_forget()
        self.__frameSearch.place_forget()
        self._arrtk.placeCenter(self.__frameWelcome)
        
    def __GUIListDepos(self):
        self.__frameWelcome.place_forget()
        if not self.__setListDepos():
            self.__frameError.place(relx=0.5,rely=0.5,anchor="center")
        else :
            self.__frameList.place(relx=0.5,rely=0.5,anchor="center")
            for i in range(0,(len(self.__listDepo)-1)) :
                self.__boxlistDepot.insert(END, self.__listDepo[i])
            self.__scroll.configure(command=self.__boxlistDepot.yview)