# benutzer möglichkeit geben bestimmte anzahl von iterationen zu machen
# mittels schleife Pi berechnen
# k ist schleifenvariable
# weitere variable zum summieren

# summe(von 0 bis unendlich) ((-1)^k)/(2k+1))

i = int(input("Eingabe Iterationen:"))
k = -1
s = 0
while k < i:
    u = (-1)**k / (2*k+1)
    s = s + u
    k = k + 1
    # Möchten Sie die Iterationsschritte angezeigt bekommen, bitte # entfernen
  # print ("Iterationsschritt:", k)
  # print ("Annäherung:", s)
    
print ("Pi/4:", s)
