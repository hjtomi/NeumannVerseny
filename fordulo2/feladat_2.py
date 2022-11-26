from copy import deepcopy


lepes_sorozatok_kordinatak = []  # tele van nested listekkel amikben
                      # kordinatak vannak, azaz tuplek
lepes_sorozatok_szamok = []     # ugyanay mint a fenti csak stringekkel

lepes_sorozatok_int = []

file = open("lepesek.txt", "r")
for raw_line in file.readlines():
    line = raw_line.split(" ")
    line[-1] = line[-1].rstrip()

    lepes_sorozatok_szamok.append(line)

    sor_lepesei = []
    sor_int_lepesei = []
    for str_szam in line:
        int_szam = int(str_szam)
        sor_int_lepesei.append(int_szam)

        kordinata = (int(str_szam[0]), int(str_szam[1]))
        sor_lepesei.append(kordinata)

    lepes_sorozatok_kordinatak.append(sor_lepesei)

    lepes_sorozatok_int.append(sor_int_lepesei)

file.close()


def main():
    # first is row, then column
    tabla_start = [
        [11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46],
        [51, 52, 53, 54, 55, 56],
        [61, 62, 63, 64, 65, 66]
    ]


    tabla = deepcopy(tabla_start)


    # a) 88
    kozepso_negy_mezo = [(3, 3), (3, 4), (4, 3), (4, 4)]
    elso_tiz_lepesben_kozepso_mezore_lepett_kodsorok_szama = 0

    for lepes_sorozat in lepes_sorozatok_kordinatak:
        for kordinata in lepes_sorozat[:10]:
            if kordinata in kozepso_negy_mezo:
                elso_tiz_lepesben_kozepso_mezore_lepett_kodsorok_szama += 1
                break
        tabla = deepcopy(tabla_start)

    print(f"a) megoldasa: {elso_tiz_lepesben_kozepso_mezore_lepett_kodsorok_szama}")

    # b) 6
    # Ahhoz hogy egy lepes ervenyes legyen a kordinajuk kulonbsegenek
    # 12, 8, 21 vagy 19-nek kell lennie

    # Csináljunk kettő listát
    # Az első listába a sor végi kordinátákat rakjuk
    # A második listába a sor eleji kordinátákat rakjuk
    # Ugye a kivétel lesz az első sor kezdete és az utolsó sor vége

    # ezután indexenként haladva menjunk végig a két listán
    # és ha a különbségük a fenti, akkor adjunk hozzá egyet egy változóhoz

    utolso_szamok = []
    elso_szamok = []
    for i, szamsor in enumerate(lepes_sorozatok_szamok):
        if i != 99:
            utolso_szamok.append(int(szamsor[-1]))

        if i != 0:
            elso_szamok.append(int(szamsor[0]))


    elerhetoek_szama = 0
    for (utolso_szam, elso_szam) in zip(utolso_szamok, elso_szamok):
        if abs(utolso_szam - elso_szam) == 12:
            elerhetoek_szama += 1
        elif abs(utolso_szam - elso_szam) == 8:
            elerhetoek_szama += 1
        elif abs(utolso_szam - elso_szam) == 21:
            elerhetoek_szama += 1
        elif abs(utolso_szam - elso_szam) == 19:
            elerhetoek_szama += 1

    print(f"b) megoldasa: {elerhetoek_szama}")

    # c) [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # csináljunk egy listát amibe a nullások és egyesek fognak menni

    # 1 Csekkoljuk hogy helyesek-e a lépések
    # 2 Csekkoljuk közben hogy olyan mezőre lépünk-e ahova már egyszer léptünk
    # 3 Csekkoljuk még azt is hogy az összes mezőre léptünk-e
    # 4 Ha mindegyik teszten átmegy akkor jó a lépéssor azaz 1 különben 0

    nullasok_egyesek = []

    # 1
    # minden számot kivéve az utolsót vessük össze az azt követővel és
    # nézzük meg hogy a különbségük 12, 8, 21 vagy 19-e

    fault = False
    # minden sor
    for szamsorozat in lepes_sorozatok_szamok:
        fault = False
        for i, szam in enumerate(szamsorozat[:-1]):
            # intigerre alakitas
            szam = int(szam)
            kovetkezo_szam = int(szamsorozat[i+1])

            # 1
            if abs(szam - kovetkezo_szam) == 12:
                pass
            elif abs(szam - kovetkezo_szam) == 8:
                pass
            elif abs(szam - kovetkezo_szam) == 21:
                pass
            elif abs(szam - kovetkezo_szam) == 19:
                pass
            else:
                nullasok_egyesek.append(0)
                fault = True
                break

        if not fault:
            # 2
            for szam in szamsorozat:
                if szamsorozat.count(szam) > 1:
                    nullasok_egyesek.append(0)
                    fault = True
                    break

            if not fault:
                # 3
                # meg kell nezni hogy az osszes alabbi szam benne van-e a sorban
                szamok = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36,41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66]
                for szam in szamok:
                    if str(szam) in szamsorozat:
                        szamsorozat.remove(str(szam))

                if szamsorozat != []:
                    nullasok_egyesek.append(0)
                    fault = True
                    break

        if not fault:
            nullasok_egyesek.append(1)

    print(f"c) megoldasa: {nullasok_egyesek}")


if __name__ == "__main__":
    main()
