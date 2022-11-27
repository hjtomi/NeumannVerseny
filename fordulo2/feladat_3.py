# az a)-t es a c)-t mar megcsinaltuk tehat csak a b) van hatra

# b) Hány olyan szám szerepel a fájlban, amelyet 612-vel osztva a hányados nem egész szám, de véges
# tizedestört az eredmény?

# adatokban van az osszes szam intigerkent
adatok = []
with open("szamok2.txt", "r", encoding="UTF-8") as bemenet:
  for adat in bemenet.readlines():
    adatok.append(int(adat))

from decimal import *

getcontext().prec = 200

veges_tortek_szama = 0
for szam in adatok:
    if len(str(Decimal(szam) / 612)) < 200:
        veges_tortek_szama += 1

print(veges_tortek_szama)
