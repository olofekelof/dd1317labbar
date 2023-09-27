
# Kod av Tiago Venhammar
# 2023-09-27
"""
Hej och välkommen!
Mitt program om man kan kalla det så består av att låta användaren välja om hen
vill räkna ut tal i talföljder eller summor av talföljder, aritmetiska eller geometriska.
Jag skrev koden för att programmet skulla vara så interaktivt som möjligt i terminalen. 
Ibland dyker det upp errors när man kör koden? 
Men då är det bara att köra den igen så borde det lösa sig.
"""
import os

def clear_terminal():
    input("Tryck ENTER för att gå vidare!")
    os.system('cls' if os.name == 'nt' else 'clear')
    #Rensar terminalen inför varje input, för en mer "user friendly" experience

def aritmetisk_foljd(a, d, n):
    foljd = a + d * (n - 1)
    return foljd
    # Funktionen för ett tal i en ARITMETISK talföljd

def aritmetisk_foljd_summa(a, d, n):
    slutsiffra = a + d * (n - 1) 
    foljdsumma = n * (a + slutsiffra)/2
    return foljdsumma
    # Funktionen för summan av en ARITMETISK talföljd

def geometrisk_foljd(g, q, n):
    foljd = g * (q ** (n - 1))
    return foljd
    # Funktionen för ett tal i en GEOMETRISK talföljd

def geometrisk_foljd_summa(g, q, n):
    foljdsumma = g * ((q ** n - 1) / (q - 1))
    return foljdsumma
    # Funktionen för summan av en GEOMETRISK talföljd

while True:
    # Låt användaren välja ifall han vill räkna med aritmetisk talföljd, geometrisk talföljd eller både och.
    print("Hej! Du har valt att använda Tiagos program för beräkning av aritmetiska och geometriska talföljder. Vad kul för dig!")
    print("Välj typ av talföljd du vill beräkna!")
    print("1. Aritmetisk talföljd")
    print("2. Geometrisk talföljd")
    print("3. Både aritmetisk och geometrisk talföljd")
    val_talfoljd = int(input("Ange ditt val: (1, 2 eller 3) och tryck ENTER"))

    if val_talfoljd == 1: # Aritmetisk Talföljd
        while True:
            print("Du har valt att beräkna en Aritmetisk talföljd!")
            clear_terminal()
            print("Vill du beräkna 1: Ett tal i talföljden eller 2: Summan av talföljden?")
            print("3: Återgå tidigare sida")
            # Låt användaren välja ifall hen vill beräkna ett tal eller summan, eller återgå startsidan
            val_berakning = int(input("Ange ditt val: (1 eller 2) Återgå med 3:"))

            if val_berakning == 1:
                # Användaren har valt att beräkna ett tal i talföljden

                print("Du har valt att beräkna ett tal i en aritmetisk talföljd! Grattis!")
                clear_terminal()
                print("Aritmetisk talföljd")
                # Användaren anger sin talföljd
                startsiffra_ari = int(input("Välj startsiffra för talföljden:"))
                differens = int(input("Välj differens mellan tal i talföljden:"))
                antal_siffror_ari = int(input("Välj vilket tal i talföljden du vill beräkna:"))

                tal_aritmetisk_foljd = aritmetisk_foljd(startsiffra_ari, differens, antal_siffror_ari)
                print("Det aritmetiska talet är:", tal_aritmetisk_foljd)
                clear_terminal()


            elif val_berakning == 2:
                # Användaren har valt att beräkna summan av talföljden
                print("Du har valt att beräkna summan av en aritmetisk talföljd! Grattis!")
                clear_terminal()
                print("Aritmetisk talföljd")
                # Användaren anger sin talföljd
                startsiffra_ari = int(input("Välj startsiffra för talföljden:"))
                differens = int(input("Välj differensen för talföljden:"))
                antal_siffror_ari = int(input("Välj antalet tal i talföljden du vill beräkna:"))

                summa_aritmetisk_foljd = aritmetisk_foljd_summa(startsiffra_ari, differens, antal_siffror_ari)
                print("Den aritmetiska summan är:", summa_aritmetisk_foljd)
                clear_terminal()


            elif val_berakning == 3:
                #Användaren har valt att återgå tidigare sida
                break


            else:
                print("Felaktigt val, välj 1 eller 2, för att återgå tidigare sida välj 3.")


    elif val_talfoljd == 2: # Geometrisk Talföljd
        while True:
            # Användaren har valt Geometrisk talföljd
            print("Du har valt att beräkna en Geometrisk talföljd!")
            clear_terminal()
            print("Vill du beräkna 1: Ett tal i talföljden eller 2: Summan av talföljden?")
            print("3: Återgå tidigare sida")
            # Låt användaren välja ifall hen vill beräkna ett tal eller summan, eller återgå startsidan

            val_berakning = int(input("Ange ditt val: (1 eller 2) Återgå med 3:"))

            if val_berakning == 1:
                # Användaren har valt att beräkna ett tal i talföljden

                print("Du har valt att beräkna ett tal i en geometrisk talföljd! Grattis!")
                clear_terminal()
                print("Geometrisk talföljd")
                #Användaren anger sin talföljd
                startsiffra_geo = int(input("Välj startsiffra för talföljden:"))
                kvot = int(input("Välj kvoten mellan tal i talföljden:"))
                antal_siffror_geo = int(input("Välj vilket tal i talföljden du vill beräkna:"))
                tal_geometrisk_foljd = geometrisk_foljd(startsiffra_geo, kvot, antal_siffror_geo)
                print("Det geometriska talet är:", tal_geometrisk_foljd)
                clear_terminal()


            elif val_berakning == 2:
                # Användaren har valt att beräkna summan av talföljden

                print("Du har valt att beräkna summan av en geometrisk talföljd! Grattis!")
                clear_terminal()
                print("Geometrisk talföljd")

                #Användaren anger sin talföljd
                startsiffra_geo = int(input("Välj startsiffra för talföljden:"))
                kvot = int(input("Välj kvoten mellan tal i talföljden:"))
                antal_siffror_geo = int(input("Välj antalet tal i talföljden du vill beräkna:"))

                summa_geometrisk_foljd = geometrisk_foljd_summa(startsiffra_geo, kvot, antal_siffror_geo)
                print("Det geometriska talet är:", summa_geometrisk_foljd)
                clear_terminal()


            elif val_berakning == 3:
                #Användaren har valt att återgå tidigare sida
                break

            else:
                print("Felaktigt val, välj 1 eller 2, för att återgå tidigare sida välj 3.")

    elif val_talfoljd == 3: # Både Aritmetisk och Geometrisk Talföljd
        while True:
            # Användaren har valt Geometrisk talföljd
            print("Du har valt att beräkna både en geometrisk talföljd och en aritmetisk talföljd simultant. Kaxigt!")
            clear_terminal()
            print("Vill du beräkna 1: Tal i talföljderna eller 2: Talföljdernas summor?")
            print("3: Återgå tidigare sida")
            # Låt användaren välja ifall hen vill beräkna ett tal eller summan, eller återgå startsidan

            val_berakning = int(input("Ange ditt val: (1 eller 2) Återgå med 3:"))

            if val_berakning == 1:
                # Användaren har valt att beräkna ett tal i talföljden

                print("Du har valt att beräkna tal i en Aritmetisk och Geometrisk talföljd! Kul!")
                clear_terminal()
                print("Aritmetisk och Geometrisk talföljd")

                # Användaren anger sina värden för talföljderna
                startsiffra = int(input("Välj startsiffra för talföljderna:"))
                differens = int(input("Välj differens mellan talen i den aritmetiska talföljden:"))
                kvot = int(input("Välj kvoten mellan talen i den geometriska talföljden:"))
                antal_siffror = int(input("Välj vilket tal i talföljderna du vill beräkna:"))

                tal_geometrisk_foljd = geometrisk_foljd(startsiffra, kvot, antal_siffror)
                print("Det geometriska talet är:", tal_geometrisk_foljd)
                tal_aritmetisk_foljd = aritmetisk_foljd(startsiffra, differens, antal_siffror)
                print("Det aritmetiska talet är:", tal_aritmetisk_foljd)
                clear_terminal()


            elif val_berakning == 2:
                # Användaren har valt att beräkna summan av talföljderna

                print("Du har valt att beräkna en aritmetisk och en geometrisk talföljds summor. Häftigt!")
                clear_terminal()
                print("Aritmetisk och Geometrisk talföljd")

                # Användaren anger sin talföljd
                startsiffra = int(input("Välj startsiffra för talföljderna:"))
                differens = int(input("Välj differens mellan talen i den aritmetiska talföljden:"))
                kvot = int(input("Välj kvoten mellan talen i den geometriska talföljden:"))
                antal_siffror = int(input("Välj vilket tal i talföljderna du vill beräkna:"))

                summa_geometrisk_foljd = geometrisk_foljd_summa(startsiffra, kvot, antal_siffror)
                print("Den geometriska summan är:", summa_geometrisk_foljd)
                summa_aritmetisk_foljd = aritmetisk_foljd_summa(startsiffra, differens, antal_siffror)
                print("Den aritmetiska summan är:", summa_aritmetisk_foljd)
                clear_terminal()
            

            elif val_berakning == 3:
                # Användaren har valt att återgå tidigare sida
                break

            else:
                print("Felaktigt val, välj 1 eller 2, för att återgå tidigare sida välj 3.")


    else: # Användaren har skrivit fel
        print("Felaktigt val, välj 1, 2 eller 3.")
