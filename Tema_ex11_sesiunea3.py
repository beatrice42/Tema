""" TEMA
11. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
a. Citește de la tastatura un numar intreg, x.
b. Afiseaza string-ul fara ultimele x caractere.

Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
print("---rezolvare ex 11---")

# Varianta 1 (functioneaza doar daca utilizatorul introduce intr-adevar un nr intreg)

s = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("Introdu un numar intreg:\n"))
lungime_s = len(s)
l = lungime_s - x
print(s[0:l])

#Varianta 2
"""Pasii:
1. Declaram si initializam stringul: s (linia 30)
2. Preluam date de la tastatura: x (linia 31)
3. Verificam daca a fost introdus un nr intreg (functia if: 32-50).
   Datele preluate vor fi de tip string. In varianta 1, daca utilizatorul introduce orice altceva decat nr intreg, 
   programul crapa. Pt a preveni eroarea, verificam daca datele preluate sunt numere intregi, le convertim in int 
   daca sunt sau respectiv informam utilizatorul ca nu a introdus un nr intreg daca nu sunt.
4. Aflam lungimea stringului (lungime_s) si lungimea stringului fara ultimele x caractere (l).
5. Afisam portiunea de string ceruta (de la indexul 0 pana la indexul l).
"""

s = 'Coral is either the stupidest animal or the smartest rock'
x = input("Introdu un numar intreg:\n")
if x.isdigit(): #acopera nr intregi pozitive si 0
    x = int(x) #str -> intreg
    lungime_s = len(s)
    l = lungime_s - x
    print(f"Lungimea string-ului este: {lungime_s} caractere")  # nu e obligatoriu, ajuta la verificarea rezultatului
    if l < 0:
        print(f"Numarul introdus ({x}) depaseste lungimea sirului ({lungime_s} caractere).")
        print(s[0:l])
    else:
        print(f"Se for afisa primele {l} caractere.")  # nu e obligatoriu, ajuta la verificarea rezultatului
        print(s[0:l])
elif x.startswith("-") and x[1:].isdigit(): #acopera nr intregi negative
        x = int(x)  # str -> intreg
        lungime_s = len(s)
        l = lungime_s - x
        print(f"Ati introdus un nr intreg negativ ({x}).")
        print(s[0:l])
else:
    print(f"{x} nu este numar intreg.")