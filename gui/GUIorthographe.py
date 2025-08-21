from tkinter import END
import customtkinter as ctk
from tkinter.messagebox import showerror
from gui.guibase import GuiBase,gestionnaire
import math

class GUIOrthographe(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Calculatrice")