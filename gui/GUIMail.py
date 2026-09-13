from arrera_tk import aFrame, aButton, aLabel, aEntry, aText, aEntryLengend, aTextScrollable

from gui.guibase import GuiBase,gestionnaire

class GUIMail(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Generation et correction de mail")
        self.__corrector = self._gestionnaire.getGestFNC().getFNCMail()


    def _mainframe(self):
        self._screen.grid_rowconfigure(0, weight=0)
        self._screen.grid_rowconfigure(1, weight=1)
        self._screen.grid_rowconfigure(2, weight=0)
        self._screen.grid_columnconfigure(0, weight=1)

        # Frame princiaple
        top_frame = aFrame(self._screen)
        center_frame = aFrame(self._screen)
        bottom_frame = aFrame(self._screen)

        # Frame secondaire
        self.__redaction_frame = aFrame(center_frame)
        self.__corrector_frame = aFrame(center_frame)
        self.__reponse_frame = aFrame(center_frame)

        out_frame = aFrame(center_frame,fg_color=center_frame.cget("fg_color"))

        # Configuration des frames
        top_frame.grid_rowconfigure(0, weight=1)
        for i in range(3):
            top_frame.grid_columnconfigure(i, weight=1, uniform="top_btns")

        # Configuration de center_frame : 2 colonnes (gauche dynamique, droite out_frame)
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1, uniform="center_cols")
        center_frame.grid_columnconfigure(1, weight=1, uniform="center_cols")

        # Configuration de redaction_frame
        self.__redaction_frame.grid_columnconfigure(0, weight=1)
        self.__redaction_frame.grid_rowconfigure(0, weight=0)
        self.__redaction_frame.grid_rowconfigure(1, weight=0)
        self.__redaction_frame.grid_rowconfigure(2, weight=0)
        self.__redaction_frame.grid_rowconfigure(3, weight=1)

        # Configuration de corrector_frame
        self.__corrector_frame.grid_columnconfigure(0, weight=1)
        self.__corrector_frame.grid_rowconfigure(0, weight=0)
        self.__corrector_frame.grid_rowconfigure(1, weight=0)
        self.__corrector_frame.grid_rowconfigure(2, weight=0)
        self.__corrector_frame.grid_rowconfigure(3, weight=1)

        # Configuration de out_frame
        out_frame.grid_columnconfigure(0, weight=1)
        out_frame.grid_rowconfigure(0, weight=0)
        out_frame.grid_rowconfigure(1, weight=0)
        out_frame.grid_rowconfigure(2, weight=0)
        out_frame.grid_rowconfigure(3, weight=0)
        out_frame.grid_rowconfigure(4, weight=1)

        bottom_frame.grid_rowconfigure(0, weight=1)
        for i in range(4):
            bottom_frame.grid_columnconfigure(i, weight=1, uniform="bottom_btns")

        # Placement des frames principales
        top_frame.grid(row=0,column=0,sticky="ew",padx=5,pady=(5, 2))
        center_frame.grid(row=1,column=0,sticky="nsew",padx=5,pady=2)
        bottom_frame.grid(row=2,column=0,sticky="ew",padx=5,pady=(2, 5))

        # Placement de out_frame à droite (colonne 1)
        out_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Affichage de la frame par défaut à gauche (colonne 0)
        self.__show_redaction()

        # Declaration des widget
        btn_redaction = aButton(top_frame, text="Rédaction", command=self.__show_redaction)
        btn_corrector = aButton(top_frame, text="Correction", command=self.__show_corrector)
        btn_reponse = aButton(top_frame, text="Réponse", command=self.__show_reponse)

        btn_clear = aButton(bottom_frame, text="Effacer tout")
        btn_generate = aButton(bottom_frame, text="Générer")
        btn_copie_body = aButton(bottom_frame, text="Copier le corps")
        btn_copy_all = aButton(bottom_frame, text="Copier tout")

        # Out
        l_title_out = aLabel(out_frame, text="Sortie", police_size=30)

        l_t_objet = aLabel(out_frame, text="Objet :",police_size=15)
        self.__e_view_objet = aEntry(out_frame)

        l_t_corp = aLabel(out_frame, text="Corps du mail :",police_size=15)
        self.__t_view_copr = aText(out_frame)

        # Redaction
        l_title_redaction = aLabel(self.__redaction_frame, text="Redaction d'un mail", police_size=30)
        self.__e_redaction_objet = aEntryLengend(self.__redaction_frame, text="Objet", police_size=15, gridUsed=True)
        l_t_consigne_redaction = aLabel(self.__redaction_frame, text="Informations clés :", police_size=15)
        self.__t_write_consigne = aTextScrollable(self.__redaction_frame)
        self.__t_write_consigne.enableTextBox()

        #Correction
        l_title_correction = aLabel(self.__corrector_frame, text="Correction", police_size=30)
        self.__e_correction_objet = aEntryLengend(self.__corrector_frame, text="Objet", police_size=15, gridUsed=True)
        l_t_correction_redaction = aLabel(self.__corrector_frame, text="Corp du mail :", police_size=15)
        self.__t_write_correction = aTextScrollable(self.__corrector_frame)
        self.__t_write_correction.enableTextBox()

        # Placement des widget de top et bottom
        btn_redaction.grid(row=0, column=0, sticky="ew", padx=15, pady=5)
        btn_corrector.grid(row=0, column=1, sticky="ew", padx=15, pady=5)
        btn_reponse.grid(row=0, column=2, sticky="ew", padx=15, pady=5)

        btn_clear.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        btn_generate.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        btn_copie_body.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
        btn_copy_all.grid(row=0, column=3, sticky="ew", padx=10, pady=5)

        # Placement des widgets dans redaction_frame
        l_title_redaction.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 10))
        self.__e_redaction_objet.grid(row=1, column=0, sticky="ew", padx=10, pady=(5, 10))
        l_t_consigne_redaction.grid(row=2, column=0, sticky="w", padx=10, pady=(5, 2))
        self.__t_write_consigne.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # Placement des widgets dans corrector_frame
        l_title_correction.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 10))
        self.__e_correction_objet.grid(row=1, column=0, sticky="ew", padx=10, pady=(5, 10))
        l_t_correction_redaction.grid(row=2, column=0, sticky="w", padx=10, pady=(5, 2))
        self.__t_write_correction.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # Placement des widgets dans out_frame
        l_title_out.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 10))
        l_t_objet.grid(row=1, column=0, sticky="w", padx=10, pady=(5, 2))
        self.__e_view_objet.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
        l_t_corp.grid(row=3, column=0, sticky="w", padx=10, pady=(5, 2))
        self.__t_view_copr.grid(row=4, column=0, sticky="nsew", padx=10, pady=(0, 10))

    def __hide_all_left_frames(self):
        self.__redaction_frame.grid_forget()
        self.__corrector_frame.grid_forget()
        self.__reponse_frame.grid_forget()

    def __show_redaction(self):
        self.__hide_all_left_frames()
        self.__redaction_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def __show_corrector(self):
        self.__hide_all_left_frames()
        self.__corrector_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def __show_reponse(self):
        self.__hide_all_left_frames()
        self.__reponse_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
