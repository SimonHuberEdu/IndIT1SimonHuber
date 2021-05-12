#Eingabe deutscher Suchbegriff -> Ausgabe englischer Lösung oder Fehlermeldung

dicDE = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
dicEN = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

dicDEgross = [x.upper() for x in dicDE]
dicENgross = [x.upper() for x in dicEN]

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
