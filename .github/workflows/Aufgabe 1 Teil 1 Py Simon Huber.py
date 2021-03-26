#Benutzer begrüßen
#zahl entgegennehmen
#zweite zahl entgegennehmen
#summe der zahlen berechnen und ausgeben
#differenz der kleineren von der größeren Zahl
#produkt berechnen und ausgeben
#quotient kleinere Zahl durch größere Zahl mit nachkommastellen berechnen und ausgeben

print ("Welcome")
ersteZahl_string = input ("Eingabe erste Zahl:")
ersteZahl = int (ersteZahl_string)
zweiteZahl_string = input ("Eingabe zweite Zahl:")
zweiteZahl = int (zweiteZahl_string)

Summe = (ersteZahl + zweiteZahl)
print ("Summe:", Summe)

result = ersteZahl < zweiteZahl
if result:
    Differenz = (zweiteZahl - ersteZahl)
    print ("Differenz:", Differenz)
else:
    Differenz = (ersteZahl - zweiteZahl)
    print ("Differenz:", Differenz)


Produkt = (ersteZahl * zweiteZahl)
print ("Produkt:", Produkt)

result = ersteZahl < zweiteZahl
if result:
    Quotient = (ersteZahl / zweiteZahl)
    print ("Quotient:", Quotient)
else:
    Quotient = (zweiteZahl - ersteZahl)
    print ("Quotient:", Quotient)
