"""Gabriel Söderberg, Lab 1, DD1317


I detta program matar in de tre värden som definierar en godtycklig aritmetisk eller geometrisk
talföljd, och tillbaka ut får du summan för den givna följden.
"""

print("Hej! Detta program räknar ut summor av geometriska och aritmetiska talföljder.")
print()
print("För den aritmetiska summan du vill beräkna skriver du in:")
print()
print("1. Det första talet i följden")
print("2. Differensen mellan talen i följden")
print("3. Antal tal i följden", end="\n")
print()
print("Och för den geometriska summan skriver du in:")
print()
print("1. Det första talet i följden")
print("2. Kvoten mellan talen i följden")
print("3. Antal tal i följden")
print("-------------------------------------------------------------------")

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


# Användaren skriver in värdena för sin aritmetiska talföljd
tal_1_ar = int(input("Första elementet i din aritmetiska talföljd: "))
diff_ar = int(input("Differensen i din aritmetiska talföljd: "))
antal_el_ar = int(input("Antal element i din aritmetiska följd: "))


# Användaren skriver in värdena för sin geometriska talföljd
tal_1_ge = int(input("Första talet i din geometriska talföljd: "))
kvot_ge = int(input("Kvoten i din geometriska talföljd: "))
antal_el_ge = int(input("Antal element i din geometriska talföljd: "))


print ("Den aritmetiska summan är:", end=" ")
print (hamta_summa_ar(tal_1_ar, antal_el_ar, hamta_tal_n_ar(tal_1_ar, diff_ar, antal_el_ar)))
print ("Den geometriska summan är:", end=" ")
print (hamta_summa_ge(tal_1_ge, kvot_ge, antal_el_ge))