# Annäherung Pi/4 mit Leibniz-Reihe von Simon Huber:
# Leibniz: Summe(von 0 bis unendlich) ((-1)^k)/(2k+1))

i = int(input("Eingabe Iterationen:")) # Wie viele Iterationen eingeben
k = 0                                  # 'k': Laufvariable
a = 0                                  # Wir fangen von 0 an zu addieren

while k < i:                           # Solange Wert(Laufvariable 'k') < Wert(Gewünschte Iterationen 'i') soll Schleife laufen
    a = a + ((-1)**k / (2*k+1))        # 'a': Funktionswert vorherige Schleife + Funktionswert aktuelle Schleife (bei 1. Iteration: 0 + Funktionswert aktuelle Schleife)
    k = k + 1                          # 'k': Erhöhe Laufvariable um eins
    
# Möchten Sie die Iterationsschritte angezeigt bekommen, bitte # entfernen:
    #print ("Iterationsschritt:", k)
    #print ("Annäherung Pi/4:", a)
    #print ("_________________________________________") #Für bessere Lesbarkeit/Unterscheidung der einzelnen Iterationen

print ("Ergebnis Pi/4:", a)
p = 4*a
print ("Ergebnis Pi:", p)
