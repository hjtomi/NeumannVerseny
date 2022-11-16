# 1.feladat
# szamok.txt

file = open('szamok.txt', 'r')
nums = file.read()
file.close()
print(nums)

# a)	Hány darab 0 számjegyet tartalmaz a fájl?
nullasok = nums.count("0")
print(f"A szamok.txt fileban {nullasok}db 0-s szamjegy van")


# b)	Hány darab különböző négyjegyű szám szerepel a fájlban?
# (A fájlban tárolt számjegyek csak az előfordulásuk sorrendjében és egymást követő módon vehetők figyelembe.)
nums_in_list = list(nums)

negyjegyu_list = []
start_index = 0
end_index = 4
for _ in range(len(nums_in_list)-3):
    negyjegyu_list.append(''.join(nums_in_list[start_index:end_index]))
    start_index += 1
    end_index += 1

negyjegyu_list = list(dict.fromkeys(negyjegyu_list))

rossz_szamok = []
for num in negyjegyu_list:
    if num[0] == "0":
        rossz_szamok.append(num)


for num in rossz_szamok:
    negyjegyu_list.remove(num)

print(f"A szamok.txt fileban {len(negyjegyu_list)}db kulonbozo 4 jegyu szam van")


# c)	A fájlban szereplő négyjegyű számok között (lásd előző feladat) hány darab különböző prímszám van?
removable_nums = []
for num_str in negyjegyu_list:
    num = int(num_str)
    for i in range(2, num):
        if num % i == 0:
            removable_nums.append(num)
            break

for num in removable_nums:
    negyjegyu_list.remove(str(num))

print(f"A szamok.txt fileban {len(negyjegyu_list)}db prim szam van")
