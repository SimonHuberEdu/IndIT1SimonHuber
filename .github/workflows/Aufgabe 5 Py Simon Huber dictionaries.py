# Dictionaries
woerterbuch = {"Apfel": "apple",
               "Birne": "pear",
               "apple": "Apfel",
               "pear": "Birne"
               }

running = True
while running:
    
    try:
        print(woerterbuch[input("Begriff eingeben: ")])
    except:
        print("Wort existiert nicht")
