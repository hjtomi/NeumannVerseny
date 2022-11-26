#1.feladat #!!!11!!!
szam = int(input('Adj meg egy számot!'))
szam2 = int(input('Adj meg egy nagyobb számot!'))
lista = []
osztok = []
db = 2
szamok = []
primek = []
best = []
str_egyed = []
num_egyed = []
prim = []
#1,
#Bekért számok között feltölt egy listát "szamok"
while szam2 > szam - 1:
    szamok.append(szam)
    szam += 1
#Listában megkeresi a prímeket és a "prímek" listában tárolja
for z in szamok:
    while len(lista) != z - 1:
        lista.append(db)
        db += 1
    for x in lista:
        if z % x == 0:
            osztok.append(x)
    if len(osztok) == 1:
        primek.append(z)
    db = 2
    lista.clear()
    osztok.clear()
#Prímszámok közül kikeresi azt amiből balról elvéve egy számot egy másik prímet kapunk
for y in primek:
    #Prímszám első számának elvétele
    y_num = str(y)
    csonk = list(y_num)
    csonk.pop(0)
    a = ''.join(csonk)
    w = int(a)
    #A már csonkított primet vizsgája hogy prim-e, ha igen "best" listába tárolja
    while len(lista) != w - 1:
        lista.append(db)
        db += 1
    for q in lista:
        if w % q == 0:
            osztok.append(q)
    if len(osztok) == 1:
        best.append(y)
    db = 2
    lista.clear()
    osztok.clear()
    csonk.clear()
#print(len(best))


#2,#!!!megoldás!!!
#szam = 100000
#szam1 = 300000
#print(max(best))


#3,#!!!megoldás!!!
#szam = 10000
#szam1 = 99999
#Primek listól kiveszi, felbontja és egy másik listába "num_egyed" teszi őket számként!!
for v in primek:
    v_num = str(v)
    k = list(v_num)
    str_egyed.extend(k)
for h in str_egyed:
    h = int(h)
    num_egyed.append(h)
#num_egyed listában megkeresei a prímeket és "prim" listába teszi őket
for p in num_egyed:
    while len(lista) != p - 1:
        lista.append(db)
        db += 1
    for l in lista:
        if p % l == 0:
            osztok.append(l)
    if len(osztok) == 1:
        prim.append(p)
    db = 2
    lista.clear()
    osztok.clear()
print(len(prim))