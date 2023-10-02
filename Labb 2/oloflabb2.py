"""
Det här är Olofs labb 2 dd1317
"""

import sys
def aritmetisk_talfoljdsberaknare(n, a1, d):
    """
    Beräknar den aritmetiska talföljden med
    INPUT: flyttal
    n = antalet tal
    A1 - första talet i talföljden
    d - differesen
    OUTPUT: flyttal
    """
    sista_talet = a1 + d * (n - 1)
    aritmetisk_talsumma = n * (a1 + sista_talet) / 2
    return aritmetisk_talsumma

def geometrisk_talfoljdsberaknare(n, g1, q):
   """
   Beräknar den geometriska talföljden med
   INPUT: flyttal
   n - antalet tal
   g1 - första talet i talföljden
   q - kvot mellan talen
   OUTPUT: flyttal
   """
   try:
        geometrisk_talsumma = g1 * ((q ** n) - 1)/(q - 1)
   except ZeroDivisionError:
        sys.exit("Division med noll är inte tilllåtet, försök igen med ett kvotvärde (q) skiljt från 1")

   return geometrisk_talsumma

def flyttalstestare(indata):
    """
    Funktionen testar om datan från användaren är i rätt format. 
    Returnerar antingen värdet eller ett felmeddelande som ber användaren att starta om
    """
    while True:
        try:
            return float((indata))
        except ValueError:
            sys.exit("Det där var inget flyttal, vänligen starta om programmet och försök igen")

#Följande block hanterar indata från användaren
print("Data för den aritmetiska summan:")

forsta_talet_aritmetisk = flyttalstestare((input("Skriv in startvärdet (a1): ")))  #första talet i din aritmetiska talföljd
differens = flyttalstestare((input("Skriv in differensen (d): "))) #differensen mellan talen i din talföljd
print()

print("Data för den geometriska summan:")
forsta_talet_geometrisk = flyttalstestare(input("Skriv in startvärdet (g1): ")) #första talet i din geometriska talföljd
quota = flyttalstestare(input("Skriv in kvotvärde (q). obs: q skiljt från 1: ")) #kvoten av två på varandra följande tal i talföljden


print()
print("Antal termer i summorna:")
try:
    antalet_tal = int(input("Skriv in antalet element i föjden (n): ")) #antalet tal i din talföljd
except ValueError:
    sys.exit("Det där var inte ett heltal, starta om programmet och försök igen")

aritmetisk_summa = aritmetisk_talfoljdsberaknare(antalet_tal, forsta_talet_aritmetisk, differens)
geometrisk_summa = geometrisk_talfoljdsberaknare(antalet_tal, forsta_talet_geometrisk, quota)


#jämför den aritmetiska och geometriska talsummans värde

if aritmetisk_summa > geometrisk_summa:
    """
    Jämför de olika värden som ges av funktionerna och formulerar ett uttalande
    """
    print("Den aritmetiska talsumman är större än den geometriska")
elif aritmetisk_summa < geometrisk_summa:
    print("Den geometriska talsumman är större än den aritmetiska")
elif aritmetisk_summa == geometrisk_summa:
    print("Den aritmetiska talsumman är lika med den geometriska talsumman")
else: 
    print("ett oväntat fel uppstod, vänligen kontakta skaparen")

print(f"den artimetiska talsumman är {aritmetisk_summa}")
print(f"den geometriska talsumman är {geometrisk_summa}")
