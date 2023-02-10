#4.feladat: Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
#hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
"""
szam = int(input("Kérem a számot:"))
if szam %3 == 0 or szam %5 == 0:
    print("A szám osztható 5-tel vagy 3-mal.")
else:
    print("A szám nem osztható 5-tel vagy 3-mal.")
"""   
#1.feladat: Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legkisebb értéket ezek közül!
"""
i = []
for x in range(1,4,1):
    s = int(input("Kérem a számot:"))
    i.append(s)
print("A megadott számok közül a legkisebb:",min(i))
"""
#3.feladat:Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
#érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
"""
i = int(input("Kérem a pont számot:"))
if i < 50:
    print("A kapott érdemjegy 1-es.")
if 50<= i < 60:
    print("A kapott érdemjegy 2-es.")
if 60<= i < 70:
    print("A kapott érdemjegy 3-mas")
if 70<= i < 85:
    print("A kapott érdemjegy 4-es")
if i >=85:
    print("A kapott érdemjegy 5-ös")
"""
#5.feladat:
"""
szam = int(input("Kérem a számot:"))
szam1 = int(input("Kérem a számot:"))
szam2 = int(input("Kérem a számot:"))
if szam + szam1 == szam2 or szam2 + szam == szam1 or szam1 + szam2 == szam:
    print("A két szám összege egyenlő a harmadikkal.")
else:
    print("A két szám összege nem egyenlő a harmadikkal.")
"""
#6.feladat:
"""
szam3 = int(input("Kérem a számot:"))
szam4 = int(input("Kérem a számot:"))
szam5 = int(input("Kérem a számot:"))
if szam3 %2 == 0 and szam4 %2 == 0 and szam5 %2 ==0:
    print("Mind a három szám osztható kettővel.")
else:
    print("Nem osztható mind három szám kettővel.")
"""
#8.feladat:
"""
a = float(input("Kérem a számot:"))
k = int(input("Kérem a számot:"))
hatvany = a**k
print(hatvany)
"""
#27.feladat:
"""
i = [1,2,3,4]
i.sort()
i.reverse()
print(i)
"""
#26.feladat:
"""
o = [1,2,3,4,5]
l = o.copy()
print(l)
"""
#9.feladat:

z = int(input("Kérem adjon meg egy 20-nál kisebb egész számot:"))