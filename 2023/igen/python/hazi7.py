"""Ország:	Állatok (Animalia)
Törzs:	Gerinchúrosok (Chordata)
Altörzs:	Gerincesek (Vertebrata)
Főosztály:	Négylábúak (Tetrapoda)
Osztály:	Emlősök (Mammalia)
Alosztály:	Elevenszülő emlősök (Theria)
Csoport:	Eutheria
Alosztályág:	Méhlepényesek (Placentalia)
Öregrend:	Laurasiatheria
Csoport:	Ferae
Rend:	Ragadozók (Carnivora)
Alrend:	Kutyaalkatúak (Caniformia)
Család:	Kutyafélék (Canidae)
Nemzetség:	Rókák (Vulpini)
Nem:	Róka (Vulpes)
Faj:	V. zerda
Frisch,1775
"""

class orszag():
    def __init__(self,orszag):
        self.orszag=orszag

class torzs(orszag):
    def __init__(self,orszag,torzs):
        super().__init__(orszag)
        self.torzs=torzs
class altorzs(torzs):
    def __init__(self,orszag,torzs,altorzs):
        super().__init__(oszag,torzs)
        self.altorzs=altorzs
class foosztaly():
    def __init__(self,orszag,torzs,altorzs,foosztaly):
        super().__init__(orszag,torzs,altorzs)
        self.foosztaly=foosztaly
class alosztaly():
    def __init__(self,orszag,torzs,altorzs,foosztaly,alosztaly):
        super().__init__(orszag,torzs,altorsz,foosztaly)
        self.alosztaly=alosztaly
