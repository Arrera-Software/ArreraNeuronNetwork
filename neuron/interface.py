from neuron.CNeuronBase import neuronBase,gestionnaire

class interface(neuronBase):
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)

    def neurone(self,requette:str):
        if self._keyword.checkInterface(requette,"noopensoft") :
            self._valeurOut = 1
            self._listSortie = ["noopensoft",""]
