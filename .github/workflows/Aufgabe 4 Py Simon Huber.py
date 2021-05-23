# Auftrag: Wörterbuch mit folgenden Möglichkeiten:
# Neues Wort hinzufügen, Wort löschen, Wort übersetzen von
# englisch -> deutsch bzw. deutsch -> englisch


dicDE = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
dicEN = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
#print(dicDE)
#print(dicEN)
dicDEgross = [x.upper() for x in dicDE] # Alle Wörter in Grossbuchstaben
dicENgross = [x.upper() for x in dicEN] # Alle Wörter in Grossbuchstaben

running = True #ab hier endlos Schleife

while True:
    ausw = input("Befehl? [E]infügen, [L]öschen, [A]bfragen: ")
    auswahl = ausw.upper()

# auswahl = auswahl.upper()
    #if auswahl == 'E' or 'e':
    if 'E' in auswahl: #Hinzufügen
        neuesWortDE = input("Neues deutsches Wort eingeben:")
        dicDE.append(neuesWortDE) #Neues deutsches Wort wird zur Liste hinzugefügt
        neuesWortEN = input("Jetzt bitte englische Übersetzung zu neuem Wort eingeben:")
        dicEN.append(neuesWortEN) #Neues englisches Wort wird zur Liste hinzugefügt
        print(dicDE)
        print(dicEN)

        
  #  elif auswahl == 'L' or 'l':
    elif 'L' in auswahl: #Löschen
    #elif auswahl == 'B' or auswahl == 'b':
     #   running = False
        WortLoeschen = input("Zu löschendes Wort in Deutsch eingeben:")
        dicDE.remove(WortLoeschen) # Wort aus deutschem Wörterbuch entfernen
        dicEN.remove(index.WortLoeschen) #An Index Stelle von deutschem Wort auch aus EN Wörterbuch entfernen
        print(dicDE)
        print(dicEN)

        
    else: # Standardvorgang -> immer mit dem geringsten Risiko -> Abfrage
        gesuchtesWort = input ("Eingabe:")
        GrossesWort = gesuchtesWort.upper()
        Fehlermeldung = ("Dieses Wort existiert nicht im Woerterbuch.")

        if GrossesWort in dicDEgross:
            IndexGesuchtesWort = dicDEgross.index (GrossesWort)
            print ("Übersetzung ins Englische:")
            print (dicEN [IndexGesuchtesWort])
        elif GrossesWort in dicENgross:
            IndexGesuchtesWort = dicENgross.index (GrossesWort)
            print ("Übersetzung ins Deutsche:")
            print (dicDE [IndexGesuchtesWort])
#    
        else:
            print (Fehlermeldung)

