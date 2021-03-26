print ("Welcome")
ersteZahl  = int(input("Eingabe erste Zahl:"))
zweiteZahl = int(input("Eingabe zweite Zahl:"))

Summe   = (ersteZahl + zweiteZahl)
Produkt = (ersteZahl * zweiteZahl)

Zustand = ersteZahl < zweiteZahl
if Zustand:
    Differenz = (zweiteZahl - ersteZahl)
    Quotient  = (ersteZahl  / zweiteZahl)
else:
    Differenz = (ersteZahl  - zweiteZahl)
    Quotient  = (zweiteZahl / ersteZahl)

print ("Summe:", Summe)
print ("Differenz:", Differenz)
print ("Produkt:", Produkt)
print ("Quotient:", Quotient)

