class Developer:
    def __init__(self, nazwa:str, adres:str, nip:str, wlascicel:str):
        self._nazwa = nazwa
        self._adres = adres
        self._nip = nip
        self._wlasciciel = wlascicel

    def __str__(self):
        return f"Nazwa dewelopera: {self._nazwa} adres deweloper: {self._adres} " \
               f"NIP: {self._nip} Właściciel firmy: {self._wlasciciel}"

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def adres(self):
        return self._adres

    @property
    def nip(self):
        return self._nip

    @property
    def wlasciciel(self):
        return self._wlasciciel