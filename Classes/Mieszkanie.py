from Classes.Nieruchomosc import Nieruchomosc

class Mieszkanie(Nieruchomosc):
    def __init__(self,powierzchnia:int,ulica:str,miasto:str,numer_budynku:str,cena:int,id_zamowienia:int):
        super().__init__(ulica,miasto,numer_budynku,cena)
        self._powierzchnia = powierzchnia
        self._id_zamowienia = id_zamowienia
    def __str__(self):
        return f" powierzchnia: {self._powierzchnia} ulica: {self._ulica} " \
               f"miasto: {self._miasto} numer budynku: {self._numer_budynku} cena{self.cena}"
    @property
    def powierzchnia(self):
        return self._powierzchnia

    @property
    def id_zamowienia(self):
        return self._id_zamowienia