"""Gabriel Söderberg, Lab 1, DD1317"""


def hamta_tal_n_ar(startvarde, differens, antalelement):
    """Tar första talet i en aritmetisk följd,
    differensen och antal element, ger sista elementet i följden"""
    tal_n_ar = startvarde + differens * (antalelement -1)
    return tal_n_ar

def hamta_summa_ar(startvarde, antalelement, sistatal):
    """Tar första talet i ar. följd, antal element
    och sista elementet i följden, ger summan av följden"""
    return antalelement * ((startvarde + sistatal) / 2)

def hamta_summa_ge(startvarde, kvot, antalelement):
    """Tar första talet i ge. följd, kvoten och antal 
    element, ger summan av följden"""
    summa_ge = startvarde *((kvot ** antalelement -1) / (kvot - 1))
    return summa_ge


# Skriv in värdena för din aritmetiska talföljd här
tal_1_ar = 2     # Första elementet
diff_ar = 4        # Differensen
antal_el_ar = 3  # Antal element


# Skriv in värdena för din geometriska talföljd här
tal_1_ge = 1     # Första talet
kvot_ge = 3         # Kvoten
antal_el_ge = 5  # Antal element


print ("Den aritmetiska summan är:", end=" ")
print (hamta_summa_ar(tal_1_ar, antal_el_ar, hamta_tal_n_ar(tal_1_ar, diff_ar, antal_el_ar)))
print ("Den geometriska summan är:", end=" ")
print (hamta_summa_ge(tal_1_ge, kvot_ge, antal_el_ge))
