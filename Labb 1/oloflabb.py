"""
Det här är olof labb 1
"""
def aritmetisk_talfoljdsberaknare(n, A1, d):
    """
    Beräknar den aritmetiska talföljden med
    INPUT: heltal
    n = antalet tal
    A1 - första talet i talföljden
    d - differesen
    OUTPUT: heltal
    """
    sista_talet = A1 + d * (n - 1)
    aritmetisk_talsumma = n * (A1 + sista_talet) / 2
    return aritmetisk_talsumma

def geometrisk_talfoljdsberaknare(n, A1, q):
   """
   Beräknar den geometriska talföljden med
   INPUT: Heltal
   n - antalet tal
   A1 - första talet i talföljden
   q - kvot mellan talen
   OUTPUT: heltal
   """
   sista_talet = A1 * q ** (n - 1)
   geometrisk_talsumma = A1 * ((q ** n) - 1)/(q - 1)
   return geometrisk_talsumma

FIRST_ELEMENT = 1 #första talet i din talföljd
DIFFERENS = 1 #differensen mellan talen i din talföljd
NUMBER_OF_ELEMENTS = 7 #antalet tal i din talföljd
QUOTA = 2 #kvoten av två på varandra följande tal i talföljden

print(f"Den aritmetiska talföljden är {aritmetisk_talfoljdsberaknare(NUMBER_OF_ELEMENTS, FIRST_ELEMENT, DIFFERENS)}") #skriver ut summan av den aritmetiska talföljden
print(f"Den geometriska talföljden är {geometrisk_talfoljdsberaknare(NUMBER_OF_ELEMENTS, FIRST_ELEMENT, QUOTA)}") #skriver ut summan av den geometriska talföljden
