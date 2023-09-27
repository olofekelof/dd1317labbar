# Kod av Tiago Venhammar
# 2023-09-27

import os # Tillåter oss att använda interager med terminalen!

def clear_terminal():
    """
    Rensar terminalen efter varje input, för att användaren ska få en trevligare upplevelse!
    """
    input("Tryck ENTER för att gå vidare!")
    os.system('cls' if os.name == 'nt' else 'clear')

def aritmetisk_foljd(a, d, n):
    """
    Funktion för ett tal i en aritmetisk följd.
    a = Första siffran i talföljden
    d = Talföljdens differens
    n = Antalet siffror i talföljden
    """
    return a + d * (n - 1)

def aritmetisk_foljd_summa(a, d, n):
    """
    Funktion för summan av en aritmetisk följd.
    """
    slutsiffra = a + d * (n - 1)
    return n * (a + slutsiffra) / 2

def geometrisk_foljd(g, q, n):
    """
    Funktion för ett tal i en geometrisk följd.
    g = Första siffran i talföljden
    q = Talföljdens kvot
    n = Antalet siffror i talföljden
    """
    return g * (q ** (n - 1))

def geometrisk_foljd_summa(g, q, n):
    """
    Funktion för summan av en geometrisk följd.
    """
    return g * ((q ** n - 1) / (q - 1))

while True:
    print("Hej! Du har valt att använda Tiagos program för beräkning av aritmetiska och geometriska talföljder. Vad kul för dig!")
    print("Välj typ av talföljd du vill beräkna:")
    print("1. Aritmetisk talföljd")
    print("2. Geometrisk talföljd")
    print("3. Både aritmetisk och geometrisk talföljd")
    val_talfoljd = int(input("Ange ditt val: (1, 2 eller 3) och tryck ENTER"))
    """
    Här låter vi användaren välja vad hen vill beräkna,
    aritmetiska talföljder eller geometriska. Eller både och!
    """

    if val_talfoljd in [1, 2, 3]:
        while True:
            clear_terminal() # Rensar terminalen efter varje användar-input
            print("Du har valt att beräkna en", "Aritmetisk" if val_talfoljd == 1 else "Geometrisk", "talföljd!")

            print("Vill du beräkna 1: Ett tal i talföljden eller 2: Summan av talföljden?")
            print("3: Återgå tidigare sida")
            val_berakning = int(input("Ange ditt val: (1 eller 2) Återgå med 3:"))

            """
            Här låter vi användaren välja huruvida hen vill beräkna summan av en viss talföljd,
            eller bara ett tal i talföljden.
            """

            if val_berakning in [1, 2]:
                clear_terminal()
                print("Aritmetisk talföljd" if val_talfoljd == 1 else "Geometrisk talföljd")
                startsiffra = int(input("Välj startsiffra för talföljden: ")) # Första siffran i talföljden (a1)
                kvot_eller_diff = int(input("Välj kvoten mellan tal i talföljden: " if val_talfoljd == 2 else "Välj differens mellan tal i talföljden: ")) # Val av kvot eller differans i talföljden, (q och d)
                antal_siffror = int(input("Välj vilket tal i talföljden du vill beräkna: ")) # Hur många siffror finns det i talföljden? (n)
                """
                Här låter vi användaren fylla i värden för sin talföljd.
                """
                if val_talfoljd == 1:
                    tal_foljd = aritmetisk_foljd(startsiffra, kvot_eller_diff, antal_siffror)
                else:
                    tal_foljd = geometrisk_foljd(startsiffra, kvot_eller_diff, antal_siffror)


                print("Det", "aritmetiska" if val_talfoljd == 1 else "geometriska", "talet är:", tal_foljd)

            elif val_berakning == 3:
                break # Ifall Användaren vill gå tillbaka, break i det här fallet går tillbaka till huvudmenyn.

            else:
                print("Felaktigt val, välj 1 eller 2, för att återgå tidigare sida välj 3.") # Om användaren inte fyller i rätt siffra för val, så kommer detta meddelande upp.

    else:
        print("Felaktigt val, välj 1, 2 eller 3.")