import datetime

class fncDate :
    def __init__(self):
        self.date= datetime.datetime.now()
    
    def rafraichisement(self):
        self.date= datetime.datetime.now()
        
    def heure(self):
        return str(self.date.time().hour)

    def minute(self):
        return str(self.date.time().minute)
    
    def second(self):
        return str(self.date.time().second)
    
    def jour(self):
        return str(self.date.day)
    
    def nbMois(self):
        return str(self.date.month)
    
    def mois(self):
        mois = int(self.date.month)
        if mois == 1 :
            monthSTR = "Janvier"
        else :
            if mois == 2 :
                monthSTR = "Fevrier"
            else :
                if mois == 3 :
                    monthSTR = "Mars"
                else :
                    if mois == 4 :
                        monthSTR = "Avril"
                    else :
                        if mois == 5 :
                            monthSTR = "Mai"
                        else:
                            if mois == 6 :
                                monthSTR = "Juin"
                            else:
                                if mois == 7 :
                                    monthSTR = "Juillet"
                                else :
                                    if mois == 8 :
                                        monthSTR = "Aout"
                                    else :
                                        if mois == 9 :
                                            monthSTR = "Septembre"
                                        else :
                                            if mois == 10 :
                                                monthSTR = "Octobre"
                                            else:
                                                if mois == 11 :
                                                    monthSTR = "Novembre"
                                                else :
                                                    monthSTR = "Décembre"
        return monthSTR
    
    def annes(self):
        return str(self.date.year)