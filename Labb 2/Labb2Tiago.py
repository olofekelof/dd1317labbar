# Tiago Venhammar
#2023-10-01

import os

a1 = 0
a2 = 0
d = 0
d2 = 0
g1 = 0
g2 = 0
q = 0
q2 = 0
n = 0
def clear_terminal():
    input("Tryck ENTER för att gå vidare!")
    os.system('cls' if os.name == 'nt' else 'clear')
    # Rensar terminalen inför varje input, för en mer "user friendly" experience

def aritmetrisk_summa(a1, d, n):
    """
    Räknar ut aritmetrisk summa
    a1 = startvärde
    d = Differens
    n = antal tal
    """
    slutsiffra = a1 + d * (n - 1)
    return n * (a1 + slutsiffra)/2
def aritmetrisk_summa2(a2, d2, n):
    """
    Räknar ut aritmetrisk summa
    a1 = startvärde
    d = Differens
    n = antal tal
    """
    slutsiffra = a2 + d2 * (n - 1)
    return n * (a2 + slutsiffra)/2

def geometrisk_summa(g1, q, n):
    """
    Räknar ut geometrisk summa
    g1 = startvärde
    q = kvot
    n = antal tal
    """
    return g1 * ((q ** n - 1) / (q - 1))

def geometrisk_summa2(g2, q2, n):
    """
    Räknar ut geometrisk summa
    g1 = startvärde
    q = kvot
    n = antal tal
    """
    return g2 * ((q2 ** n - 1) / (q2 - 1))



#Huvudmenyn
while True: # Skapar en loop för att kunna upprepa input vid felinmatning
    print("Hej och välkommen till Tiagos summe-jämförare! Jämför olika summor av aritmetiska och/eller geometriska talföljder")
    print("Ange dina värden för aritmetiska och/eller geometriska summor!")
    """
    Nedan fyller användaren in samtliga värden för talföljderna:
    """
    while True:
        val_summor1 = (input("Är den första summan (a)ritmetisk eller (g)eometrisk?:")) # Väljer typen för talföljd nr1
        if val_summor1 == 'a':
            print("Datavärde för aritmetisk summa:")
            try:
                a1 = int(input("Skriv in startvärdet (a1):"))
                d = int(input("Skriv in differensen (d):"))
                break # Bryter loopen för "val_summor1" om inmatningen är korrekt skriven
            except ValueError: # Tillser att programmet inte stängs av vid felinmatning
                print("Felaktigt värde, värdet måste bestå av siffror. Försök igen!:")
        elif val_summor1 == 'g':
            print("Datavärde för geometrisk summa:")
            try:
                g1 = int(input("Skriv in startvärdet (g1):"))
                q = int(input("Skriv in kvoten (q):"))
                if q == 1: # Felhantering ifall användaren väljer kvoten 1, då detta skulle leda till division med 0 i den geometriska summan
                    print("Kvoten kan inte vara 1 i en geometrisk summa!")
                else:
                    break
            except ValueError:
                print("Felaktigt värde, värdet måste bestå av siffror. Försök igen!")
        else:
            print("Felaktigt svar, välj (a) eller (g):")
    while True:
        val_summor2 = (input("Är den andra summan (a)ritmetisk eller (g)eometrisk?:")) # Väljer typen för talföljd nr2
        if val_summor2 == 'a':
            print("Datavärde för aritmetisk summa:")
            try:
                a2 = int(input("Skriv in startvärdet (a1):"))
                d2 = int(input("Skriv in differensen (d):"))
                break
            except ValueError:
                print("Felaktigt värde, värdet måste bestå av siffror. Försök igen!:")
        elif val_summor2 == 'g':
            print("Datavärde för geometrisk summa:")
            try:
                g2 = int(input("Skriv in startvärdet (g1):"))
                q2 = int(input("Skriv in kvoten (q):"))
                if q2 == 1:
                     print("Kvoten kan inte vara 1 i en geometrisk summa!")
                else:
                    break
            except ValueError:
                print("Felaktigt värde, värdet måste bestå av siffror. Försök igen!:")
        else:
            print("Felaktigt svar, välj (a) eller (g):")
    n = int(input("Skriv in antal element i följden (n):"))
    ari_summa = aritmetrisk_summa(a1, d, n)
    ari_summa2 = aritmetrisk_summa2(a2, d2, n)
    ari = ari_summa + ari_summa2
    geo_summa = geometrisk_summa(g1, q, n)
    geo_summa2 = geometrisk_summa2(g2, q2, n)
    geo = geo_summa + geo_summa2
    if ari > geo and geo != 0:
        print("Den aritmetiska summan är störst")
        clear_terminal()
    elif ari < geo and ari != 0:
        print("Den geometriska summan är störst")
        clear_terminal()
    elif ari == geo:
        print("Den aritmetiska och geometriska summan är lika stor")
        clear_terminal()
    elif ari_summa == ari_summa2 and ari != 0:
        print("De aritmetiska summorna är lika stora", )
        clear_terminal()
    elif ari_summa > ari_summa2:
        print("Den första aritmetiska summan är större än den andra", )
        clear_terminal()
    elif ari_summa < ari_summa2:
        print("Den andra aritmetiska summan är större än den första", )
        clear_terminal()
    elif geo_summa == geo_summa2 and geo != 0:
        print("De geometriska summorna är lika stora", )
        clear_terminal()
    elif geo_summa > geo_summa2:
        print("Den första geometriska summan är större än den andra", )
        clear_terminal()
    elif geo_summa < geo_summa2:
        print("Den andra geometriska summan är större än den första", )
        clear_terminal()
    else:
        print("ERROR")
        clear_terminal()