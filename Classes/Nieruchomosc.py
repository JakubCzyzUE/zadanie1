class Nieruchomosc:
    def __init__(self,ulica:str,miasto:str,numer_budynku:str,cena:int):
        self._ulica = ulica
        self._miasto = miasto
        self._numer_budynku = numer_budynku
        self._cena = cena

    @property
    def ulica(self):
        return self._ulica

    @property
    def miasto(self):
        return self._miasto

    @property
    def numer_budynku(self):
        return self._numer_budynku

    @property
    def cena(self):
        return self._cena