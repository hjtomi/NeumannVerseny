from feladat_2 import lepes_sorozatok_int

mezok = [
    11, 12, 13, 14, 15, 16,
    21, 22, 23, 24, 25, 26,
    31, 32, 33, 34, 35, 36,
    41, 42, 43, 44, 45, 46,
    51, 52, 53, 54, 55, 56,
    61, 62, 63, 64, 65, 66
]


# Magyarázat a füzetben!
def sor_helyes(sor):
    '''Megviszgálja, hogy helyes-e a sor, True amikor helyes, False amikor nem'''
    for mezo_szam in mezok:
        if mezo_szam not in sor:
            # print("Nem lép minden mezőre!", mezo_szam)
            return False

    sor_set = set(sor)
    if len(sor) != len(sor_set):
        # print("Egy mezőre többször is lép!")
        return False

    for i, szam in enumerate(sor[:-1]):
        kulonbseg = abs(sor[i] - sor[i+1])
        if kulonbseg != 8 and kulonbseg != 12 and kulonbseg != 19 and kulonbseg != 21:
            # print("Nem minden lépés lehetséges lólépés!", i, sor[i], sor[i+1])
            return False

    return True

egyesek_nullasok = []

for lepes_sor in lepes_sorozatok_int:
    if sor_helyes(lepes_sor):
        egyesek_nullasok.append(1)
    else:
        egyesek_nullasok.append(0)

print(f"A c) megoldása: {egyesek_nullasok}")
