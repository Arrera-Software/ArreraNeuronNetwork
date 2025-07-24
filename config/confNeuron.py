from dataclasses import dataclass, field
from typing import List

@dataclass
class confNeuron:
    name: str
    lang: str
    icon: str
    assetHorloge: str
    assetCalculatrice: str
    guiColor: str
    textColor: str
    bute: str
    createur: str
    listFonction: List[str] = field(default_factory=list)
    moteurderecherche: str = ""
    etatService: int = 0
    etatSoftware: int = 0
    etatTime: int = 0
    etatOpen: int = 0
    etatSearch: int = 0
    etatChatbot: int = 0
    etatApi: int = 0
    etatCodehelp: int = 0
    etatWork: int = 0
    etatSocket: int = 0
    lienDoc: str = ""

confassistant = confNeuron(
    name= "Opale",
    lang= "fr",
    icon= "assets/icon.png",
    assetHorloge="asset/horloge/",
    assetCalculatrice="asset/calculatrice/",
    guiColor="white",
    textColor="black",
    bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
    createur="Pauchet Baptiste",
    listFonction=["ouvrir une application","aider sur les recherches de internet","donner la meteo","faire un résumer des actualités"],
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
    lienDoc="www.google.com")
