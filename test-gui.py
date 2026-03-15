import tkinter as tk
from gestionnaire.gestion import gestionnaire
from config.confNeuron import confNeuron

# Configuration de l'assistant
conf = confNeuron(name="Opale",
                  lang="fr",
                  icon="asset/icon.png",
                  asset="asset/",
                  assistant_color="white",
                  assistant_texte_color="black",
                  bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
                  createur="Pauchet Baptiste",
                  listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                          "faire un résumer des actualités"],
                  moteurderecherche="google",
                  etatService=1,
                  etatTime=1,
                  etatOpen=1,
                  etatSearch=1,
                  etatChatbot=1,
                  etatApi=1,
                  etatCodehelp=1,
                  etatWork=1,
                  etatSocket=1,
                  lienDoc="www.google.com",
                  fichierLangue="language/vouvoiment/",
                  fichierKeyword="keyword/",
                  voiceAssistant=True)

# Initialisation du gestionnaire principal
gest = gestionnaire(conf)
# Récupération du gestionnaire de GUI
gest_gui = gest.getGestGUI()

# Créer la fenêtre principale
window = tk.Tk()
window.title("Test des interfaces graphiques")
window.geometry("800x600")

# Créer un cadre pour les boutons
button_frame = tk.Frame(window)
button_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Dictionnaire des interfaces à tester et de leurs fonctions de lancement
# Nous utilisons les méthodes directes exposées à la fin de gestGUI.py
gui_to_test = {
    "Agenda": gest_gui.activeAgenda,
    "Tâches": gest_gui.activeTache,
    "Aide": lambda: gest_gui.activeHelp("Texte d'aide de test"),
    "Breef": gest_gui.activeBreef,
    "Calculatrice": lambda: gest_gui.setGUIActive("calculatrice_normal") and gest_gui.launch_gui(),
    "Orthographe": lambda: gest_gui.setGUIActive("orthographe", "Ceci est un texte de test.") and gest_gui.launch_gui(),
    "Arrera Download": lambda: gest_gui.setGUIActive("arrera_download") and gest_gui.launch_gui(),
    "Horloge": lambda: gest_gui.setGUIActive("horloge") and gest_gui.launch_gui(),
    "Lecture": lambda: gest_gui.setGUIActive("lecture") and gest_gui.launch_gui(),
    "Arrera Work": lambda: gest_gui.setGUIActive("work") and gest_gui.launch_gui(),
    "Traducteur": lambda: gest_gui.setGUIActive("traducteur") and gest_gui.launch_gui(),
    "Resumer": lambda: gest_gui.activeViewResumer(dict={}, list=[], intIn=0)
}


# Créer un bouton pour chaque interface
# Organiser les boutons sur une grille pour une meilleure lisibilité
rows = 4
cols = 3
i = 0
for name, action in gui_to_test.items():
    row = i // cols
    col = i % cols
    btn = tk.Button(button_frame, text=name, command=action, height=4, width=15)
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    i += 1

# Configurer la grille pour qu'elle s'étende avec la fenêtre
for i in range(rows):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(cols):
    button_frame.grid_columnconfigure(i, weight=1)


# Lancer la boucle principale de l'interface graphique
window.mainloop()
