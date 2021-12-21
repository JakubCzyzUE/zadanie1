from Classes import Developer
from Classes import Nieruchomosc
from Classes.Dom import  Dom
from Classes.Mieszkanie import Mieszkanie





def obliczMetrazWszsytkich():
    tablica = []

    for x in tablica:
        print(x)



class Zamowienie:


    def __init__(self, id_zamowienia: int, imie_kupujacego: str, nazwisko_kupujacego: str, zaliczka: int, nieruchomosci:list):
        self._id_zamowienia = id_zamowienia
        self._imie_kupujacego = imie_kupujacego
        self._nazwisko_kupujacego = nazwisko_kupujacego
        self._zaliczka = zaliczka
        self._nieruchomosci = nieruchomosci

    def __str__(self):
        return f"id zamówienia: {self._id_zamowienia} imie kupującego: {self._imie_kupujacego} " \
               f"nazwisko kupującego: {self._nazwisko_kupujacego} wpłacona zaliczka: {self._zaliczka}"

    @property
    def id_zamowienia(self) -> None:
        return self._id_zamowienia

    @id_zamowienia.setter
    def id_zamowienia(self, value):
        self._id_zamowienia = value

    @property
    def imie_kupujacego(self) -> None:
        return self.imie_kupujacego

    @imie_kupujacego.setter
    def imie_kupujacego(self, value):
        self.imie_kupujacego = value

    @property
    def nazwisko_kupujacego(self) -> None:
        return self.nazwisko_kupujacego

    @nazwisko_kupujacego.setter
    def nazwisko_kupujacego(self, value):
        self.nazwisko_kupujacego = value

    @property
    def zaliczka(self) -> None:
        return self.zaliczka

    @zaliczka.setter
    def zaliczka(self, value):
        self.zaliczka = value

    def LiczMetryKwadratowe(self):

        all_meters = 0
        for nieruchomosc in self._nieruchomosci:
            all_meters += nieruchomosc.powierzchnia
        return all_meters

    def obliczCene(self,m:Mieszkanie ):
        if(m.id_zamowienia == self.id_zamowienia):
            print(m.cena)


    def obliczCene(self,d:Dom):
        if (d.id_zamowienia == self.id_zamowienia):
            print(d.cena)
