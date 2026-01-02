# ArreraNeuronNetwork Project Architecture

This document describes the file and folder organization of the ArreraNeuronNetwork project.

## Directories

### asset/
Contains static resources (images, sounds).
- `calculatrice/`: Images for calculator keys.
- `calendar/`: Images for the calendar.
- `horloge/`: Images and sounds (bip.mp3) for the clock, stopwatch, and timer.
- `meteo/`: Icons for weather conditions.
- `tache/`: Icons for task management.
- `work/`: Icons for the workspace (projects, spreadsheet, word processing).

### brain/
- `brain.py`: Likely contains the central logic or "brain" of the assistant.

### config/
Configuration files.
- `confNeuron.py`: Neuron configuration.
- `ia_instruction.txt`: Textual instructions for the AI.
- `listFete.json`: Database of holidays/celebrations.

### fnc/ (Functions)
Modules implementing the various functionalities of the assistant.
- `fncBase.py`: Base class for functions.
- `fonctionActu.py`: News management.
- `fonctionArreraDownload.py`: Download management.
- `fonctionArreraWork.py`: Work-related functionalities (office tools).
- `fonctionBreef.py`: Summaries or briefs.
- `fonctionCalculatrice.py`: Calculator logic.
- `fonctionCalendar.py`: Calendar management.
- `fonctionCodeHelp.py`: Coding/development helper.
- `fonctionGPS.py`: Location and GPS.
- `fonctionHorloge.py`: Time management, alarms, timer.
- `fonctionLecture.py`: Text-to-speech or text reading.
- `fonctionMeteo.py`: Weather forecasts.
- `fonctionOPEN.py`: Opening files or programs.
- `fonctionOrthographe.py`: Spelling correction.
- `fonctionRadio.py`: Radio player.
- `fonctionRecherche.py`: Internet search.
- `fonctionTache.py`: Task manager (To-Do).
- `fonctionTraduction.py`: Text translation.

### gestionnaire/ (Managers)
Management modules and coordinators.
- `gestion.py`: Global manager.
- `gestFNC.py`: Function manager.
- `gestGUI.py`: GUI manager.
- `gestHistorique.py`: Interaction history management.
- `gestIA.py`: Artificial Intelligence management.
- `gestKeyword.py`: Keyword management for recognition.
- `gestLangue.py`: Language management.
- `gestNeuron.py`: Neural network management.
- `gestSocket.py`: Network/socket connection management.
- `gestSTR.py`: String processing utilities.
- `gestUserSetting.py`: User settings management.

### gui/ (Graphical User Interface)
Code related to the user interface (windows, widgets).
- `guibase.py`: Base class for windows.
- `GUIAgenda.py`, `GUICalculatrice.py`, `GUIHorloge.py`, `GUIMeteo.py`, etc.: Feature-specific interfaces.
- `GUIArreraDownload.py`, `GUIArreraWork.py`, `GUIBaseTache.py`, `GUIHelp.py`, `GUILecture.py`, `GUITache.py`, `GUITaskProject.py`, `GUITraducteur.py`, `GUIView.py`, `GUIViewBreef.py`, `GUIViewResumer.py`, `GUIorthographe.py`.
- `codehelp/`: Subdirectory containing interfaces for code help (`CCHcolorSelector.py`, `CCHguiBase.py`, `CHGithub.py`, `CHLibrairy.py`, `CHOrgraVarriable.py`).

### keyword/
JSON files defining trigger keywords.
- `api.json`, `codehelp.json`, `interface.json`, `open.json`, `search.json`, `service.json`, `time.json`, `utils.json`, `work.json`.

### language/
Linguistic configuration files (responses, standard phrases).
Divided into two modes:
- `tutoiment/`: Configuration for informal address ("tu").
- `vouvoiment/`: Configuration for formal address ("vous").
Each folder contains JSON files like `chatbot.json`, `formule.json`, `interface.json`, etc.

### librairy/
Utility libraries and support modules.
- `ArreraIALoad.py`: AI model loading.
- `arrera_date.py`: Date utilities.
- `arrera_tk.py`: Extensions or utilities for Tkinter.
- `arrera_voice.py`: Voice management (TTS/STT).
- `dectectionOS.py`: Host OS detection.
- `model_downloader.py`: External model downloader.
- `network.py`: Network utilities.
- `openSoftware.py`: Launching external software.
- `parreraclient.py`: Client for Arrera services.
- `resource_lib.py` : Library qui gère l'emplacement des resources (Pour MAC OS)
- `travailJSON.py`: JSON read/write utilities.

### neuron/
"Neural" logic for request processing.
- `CNeuronBase.py`: Base class.
- `API.py`, `chatBots.py`, `codehelp.py`, `interface.py`, `open.py`, `search.py`, `service.py`, `time.py`, `work.py`: Domain-specific processing modules.

### objet/
Business objects and class definitions.
- `CArreraDownload.py`: Download object.
- `CHsearchDoc.py`: Documentation search.
- `arreradocument.py`: Document management.
- `arreratableur.py`: Spreadsheet management.
