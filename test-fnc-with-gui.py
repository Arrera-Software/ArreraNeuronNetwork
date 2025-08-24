from librairy.arrera_tk import *
from gestionnaire.gestion import gestionnaire
from config.confNeuron import confNeuron

conf = confNeuron(name="Opale",
                  lang="fr",
                  icon="asset/icon.png",
                  asset="asset/",
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
                  etatService=1,
                  etatSoftware=1,
                  etatTime=1,
                  etatOpen=1,
                  etatSearch=1,
                  etatChatbot=1,
                  etatApi=1,
                  etatCodehelp=1,
                  etatWork=1,
                  etatSocket=1,
                  lienDoc="www.google.com",
                  fichierLangue="language/vouvoiment/")

gest = gestionnaire(conf)
fnc = gest.getGestFNC()
gui = gest.getGestGUI()
arrtk = CArreraTK()

def partCodeHelp(w:ctk.CTk):
    arrtk.createButton(w, text="Github", command=lambda : fnc.getFNCCodeHelp().openGUIGithubGestion()).pack()
    arrtk.createButton(w, text="Lib", command=lambda: fnc.getFNCCodeHelp().openGUILibrairy()).pack()
    arrtk.createButton(w, text="Orga Var", command=lambda: fnc.getFNCCodeHelp().openGUIOrgaVar()).pack()
    arrtk.createButton(w, text="Color", command=lambda: fnc.getFNCCodeHelp().openGUIColorSelector()).pack()

def partCalculatrice(w:ctk.CTk):
    arrtk.createButton(w, text="calculatrice", command=lambda: gui.activeCalculatriceNormal()).pack()
    arrtk.createButton(w, text="calculatrice Pythagore", command=lambda: gui.activeCalculatricePythagore()).pack()
    arrtk.createButton(w, text="calculatrice Complex", command=lambda: gui.activeCalculatriceComplex()).pack()

def partOrthographe(w:ctk.CTk):
    arrtk.createButton(w, text="Correcteur d'orthographe", command=lambda: gui.activeOrthographe("Je n sais pas lure est ecrore")).pack()

def main():
    screen = arrtk.aTK()
    partCodeHelp(screen)
    partCalculatrice(screen)
    partOrthographe(screen)
    arrtk.view()

if __name__ == "__main__":
    main()