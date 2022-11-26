# az a)-t es a c)-t mar megcsinaltuk tehat csak a b) van hatra

# b) Hány olyan szám szerepel a fájlban, amelyet 612-vel osztva a hányados nem egész szám, de véges
# tizedestört az eredmény?

from decimal import Decimal
import math

numbers = []
file = open("szamok2.txt", "r")
for line in file.readlines():
    numbers.append((int(line)))
file.close()

for number in numbers:
    if number % 612 < 1:
        print(number)
