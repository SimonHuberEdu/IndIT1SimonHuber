#Python 6 Simon Huber
#Ändern Sie das Wörterbuch-Beispiel so, dass Sie den Code unter Verwendung von Funktionen
#(Unterprogrammen) strukturieren.
#Beispielsweise könnten Sie jeweils ein Unterprogramm für die jeweiligen Funktionalitäten erstellen:
#
#Funktion zur Eingabe des Befehls
#Funktion zur Eingabe des Suchbegriffs bzw. Wortes
#Funktion zur Suche
#Funktion zur Ausgabe
#Laden Sie den Programmcode in das Github-Repository aus Teil 1, Aufgabe 2.
#Deadline: Mo, 21.6.2021, Mitternacht


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

def WortHinzufügen(deutschesWort, englischesWort):
    try:
        searchWord(deutschesWort)
        print("Dieses Wort existiert bereits")
    except:
        woerterbuch_deutsch.append(deutschesWort)
        woerterbuch_englisch.append(englischesWort)
    
def WortSuchen(wordInput):
    index = 0
    for wort in woerterbuch_deutsch:  
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:     
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            raise Exception("Dieses Wort existiert nicht")
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)

def WortLöschen():
    try:
        output = WortSuchen(input("Zu löschendes Wort eingeben: "))
        woerterbuch_deutsch.remove(output[0])
        woerterbuch_englisch.remove(output[1])
    except Exception as e:
        print(e)
        
def WortAusgabe():
    try:
        output = WortSuchen(input("Zu übersetzendes Wort: "))
        print(output[0] + "[DE]")
        print(output[1]+ "[EN]")
    except Exception as e:
        print(e)
        
def eingabeBefehl():
    while True:
        auswahl = input("Befehl? \n[E]infügen \n[L]öschen \n[A]bfrage \n[Q]uit: ")
        if auswahl.lower() == "e" or  auswahl.lower() =="l" or auswahl.lower() =="a" or auswahl.lower() =="q":
            return auswahl.lower()
        else:
            print("Falsche Eingabe!")

while True:
    auswahl = eingabeBefehl()
    if auswahl == "e":
        WortHinzufügen(input("Deutsches Wort eingeben: "), input("Englisches Wort eingeben: "))
        
    elif auswahl == "l":
        WortLöschen()
    elif auswahl == "q":
        break   
    else:
        WortAusgabe()

