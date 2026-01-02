# Integrating Arrera Neuron into an Assistant Project

## Folder

Move the folders ```asset/```, ```brain/```, ```config/```, ```fnc/```, ```gestionnaire/```, ```gui/```, ```keywork/```, ```librairy/```, ```neuron/```, and ```objet/``` to the root of your assistant project.

Once done, choose a language you want in the ```language/``` folder, either ```tutoiment``` (informal) or ```vouvoiment``` (formal).

## Configuration

In your main.py file

Before trying to launch your assistant, you must configure it with the confNeuron object.

Here is an example of the configuration for the Arrera OPALE development assistant.


```python
config = confNeuron(name="Opale",
                   lang="fr",
                   asset="asset/",
                   icon="asset/icon.png",
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
                   fichierLangue="language/",
                   fichierKeyword="keyword/",
                    voiceAssistant=True)
```
The parameters starting with ```etat``` are parameters to be set to either 1 or 0, which corresponds to whether you want to activate a specific function of the assistant.
The ```asset``` parameter corresponds to the location of the assistant's assets.
```icon``` is the parameter for the assistant's icon.
```assistant_color``` and ```assistant_texte_color``` are the color and text color of the assistant's interface.
```lienDoc``` is the link to the online documentation.
```fichierLangue``` is the location of the folder where all language files are found.
```fichierKeyword``` is the location of the folder where all keyword files are found.

## Integration and usage in a project

Once the configuration is done, we can start the assistant.


### Step 1: Initialization of the brain object

```python
try :
    assistantBrain = ABrain(config=config)
    return True
except Exception as e:
    print(f"Error starting the Brain assistant : {e}")
    return False
```

It is advised to use a try block to avoid complete program crashes.

Requested parameter: config, which is the configuration we made just before.

### Step 2: Startup

```python
try :
    self.__labelAssistantText.configure(text=assistantBrain.boot(), wraplength=200
    ,justify=LEFT)
except Exception as e:
    self.__labelAssistantText.configure(text=f"Error during assistant boot : {e}",wraplength=200
    ,justify=LEFT)
```

The ```boot()``` method of the ```ABrain``` object allows starting the assistant and returns the assistant's greeting formulation.

### Step 3: Sending request to the assistant

```python
def __sendAssistantMessage(self,entry:ctk.CTkEntry,screen:ctk.CTk):
    if not self.__thAssistant.is_alive():
        message = entry.get()
        if message:
            self.__thAssistant = th.Thread(target=self.__assistantBrain.neuron,args=(message,))
            self.__thAssistant.start()
            entry.delete(0, 'end')  # Clear the entry after sending
            self.__updateRequetteAssistant(screen,message)
        else:
            self.__labelAssistantText.configure(text="Please enter a message.", wraplength=200
                                                ,justify=LEFT)

def __updateRequetteAssistant(self,screen:ctk.CTk,message:str):
    if self.__thAssistant.is_alive():
        self.__arrTK.placeBottomRight(self.__labelGeneration)
        screen.after(1000,self.__updateRequetteAssistant,screen,message)
    else :
        del self.__thAssistant
        self.__labelGeneration.place_forget()
        self.__thAssistant = th.Thread()
        nb = self.__assistantBrain.getValeurSortie()
        texte = self.__assistantBrain.getListSortie()
        self.__labelAssistantText.configure(text=texte[0], wraplength=200
                                            ,justify=LEFT)
        self.__labelAssistantNumber.configure(text=str(nb))
        self.__addLog(nb,texte[0],message)
        if nb == 15:
            self.__close()
```

It is advised, if you use an interface, to use a thread to manage requests sent to the assistant, as it may take a little time for the response return due to the use of a local AI.

Once the assistant's reflection is finished, you must use the ```getValeurSortie()``` method to retrieve the output value, here are the possible outputs:

- 0 : No output
- 1 : Normal output
- 3 : News output
- 4 : Weather / temperature / GPS
- 5 : Output with tkinter window
- 6 : News error
- 7 : File opening
- 8 : File closing
- 9 : File reading
- 10 : Project creation
- 11 : News summary error
- 12 : News summary success
- 13 : Spreadsheet reading
- 14 : Project opening
- 15 : Assistant shutdown
- 16 : File creation in a project
- 17 : Help display
- 18 : Task / agenda summary
- 19 : Summary all ok
- 20 : Summary all fail
- 21 : Close project
- 22 : Radio launch
- 23 : GUI Codehelp

And to retrieve the texts generated by the assistant, you must use the ```getListSortie()``` method which returns a Python list, and the text is found at index 0.

### Step 4: Retrieving requests sent by the socket

Assistants developed based on the Arrera Neuron Network can be connected to the Arrera application via a websocket.
To take advantage of this, you must create a method that runs continuously to retrieve requests:
Here is an example

```python
def __updateAssistant(self,screen:ctk.CTk=None):
    if self.__assistantBrain.updateAssistant():
        varOut = self.__assistantBrain.getValeurSortie()
        self.__labelAssistantText.configure(text=self.__assistantBrain.getListSortie()[0], wraplength=200)
        self.__labelAssistantNumber.configure(text=str(varOut))
        if varOut == 15:
            self.__close()

    screen.after(1000,self.__updateAssistant,screen)
```
