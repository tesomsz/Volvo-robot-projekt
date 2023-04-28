class Adat():
    def __init__(self,sor):
        egy = sor.rstrip("\n").split(";")
        self.hegycsucs = egy[0]
        self.hegyseg = egy[1]
        self.magassag = int(egy[2])
        
f = open("hegyek.txt", encoding = "utf-8")
be = f.readlines()
hegyek = []
for x in be[1:]:
    egysor = Adat(x)
    hegyek.append(egysor)

#teszt
"""
for x in hegyek:
    
    print(x.hegyseg)
"""    

#3

hegycsucs = len(hegyek)
print("3.feladat: Hegycsúcsok száma:",hegycsucs)

#4
maga = []
for x in hegyek:
    hegy = x.magassag
    maga.append(hegy)
maga1 = sum(maga)
maga2 = maga1/ hegycsucs
print("4.feladat: Hegycsúcsok átlagos magassága: {:.2f}".format(maga2), "m")
#5
legmagasabb = max(maga)
print("5.feladat: A legmagasabb hegycsúcs adatai:")

for x in hegyek:
    
    if x.magassag == legmagasabb:
        print(f"Név: {x.hegycsucs}")
        print(f"Hegység: {x.hegyseg}")
        print(f"Magassag: {x.magassag}")
#6
borzsony = []

for x in hegyek:
    
    if x.hegyseg == "Börzsöny":
        borzsony.append(x.magassag)

be = int(input("6.feladat: Kérem a magasságot:"))
van = False
for x in borzsony:
    
    if x > be:
        van = True
        
if van:
    print(f"Van {be}m-nél magasabb hegycsúcs a börzsönyben!")
    
else:
    print(f"Nincs {be}m-nél magasabb hegycsúcs a börzsönyben!")
#7
hegycsucsok_szama = 0

for x in hegyek:
    
    if x.magassag > 500:
        hegycsucsok_szama += 1
        
print(f"7.feladat: 500m-nél magasabb hegycsúcsok száma: {hegycsucsok_szama}")
#8.feladat: magassagok.txt -- amiben a méterek egymás alatt!
"""
ki = open("magassagok.txt", "w")

for x in maga:
    
    ki.write(str(x) + "\n")
    
    
ki.close()

print("A kiiratás befejeződött!")
"""
#9.feladat:

ki = open("otszaz.txt", "w")

for x in hegyek:
    if x.magassag > 500:
        
        ki.write(x.hegyseg + "\n")
        
ki.close()

print("A kiiratás befejeződött!")