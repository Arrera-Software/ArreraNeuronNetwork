from playsound3 import playsound as pl
from pyttslib import TextToSpeech
from gestionnaire.gestion import gestionnaire
import speech_recognition as sr


class CArreraVoice:
    def __init__(self,gestionnaire:gestionnaire):
        self.__gestionnaire = gestionnaire
        self.__emplacementSoundMicro = self.__gestionnaire.getConfigFile().assetMicro
        self.__soundMicro = True
        self.__listWord = []
        self.__nbWord = 0
        self.__outPutText = ""
        self.loadConfig()

        if self.__gestionnaire.getNetworkObjet().getEtatInternet():
            self.__tts = TextToSpeech(engine="google")
            self.__tts.set_voice("fr")
        else:
            self.__tts = TextToSpeech(engine="pyttsx3",engine_config={
                "rate": 150,    # Words per minute
                "volume": 0.8,  # Volume level (0.0 to 1.0)
            })
            self.__tts.set_voice("French (France)")



    def loadConfig(self):
        if self.__gestionnaire.getValeurfichierUtilisateur("soundMicro") == "1":
            self.__soundMicro = True
        else:
            self.__soundMicro = False
        self.__listWord = self.__gestionnaire.getValeurfichierUtilisateur("listWord")
        self.__nbWord = len(self.__listWord)

    def say(self,text:str):
        self.__tts.speak(text)

    def playFile(self,file:str):
        pl(file)

    def listen(self):
        if self.__soundMicro:
            pl(self.__emplacementSoundMicro)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            self.__outPutText = text
            return 0
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2

    def getTextMicro(self):
        return self.__outPutText

    def getNbWord(self):
        return self.__nbWord

    def trigerWord(self):
        if self.__nbWord == 0:
            return -3
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            for word in self.__listWord:
                if word in text:
                    return 1
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2
        return 0