from Classes.Zamowienie import Zamowienie
from Classes.Dom import Dom
from Classes.Mieszkanie import Mieszkanie
from Classes.Developer import Developer

d1 = Dom(2000, "Nowa", "Kraków", "23", 12032131,123)
m1 = Mieszkanie(3, "Kosowska", "Katowice", "23", 1232131,1234)
dev1 = Developer("DeVabc","Katowice ul.klonowa 13","123452","MAREK KOWALSKI")
z1 = Zamowienie(123,"Alan","Kowalski",200000,[d1,m1])
print(z1)
print(dev1)
print(m1)
print(d1)

print(z1.LiczMetryKwadratowe())

print(z1.obliczCene(m1))

