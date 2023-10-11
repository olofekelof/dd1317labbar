import os #Används för att kunna rensa terminalen
import olofmodullabb3 #Program som testar värden mot antigen heltal eller flyttal


def clear_terminal():
    """
    Rensar terminalen och väntar på att användaren ska fortsätta
    """
    input("Tryck enter för att gå vidare")
    os.system('cls' if os.name == 'nt' else 'clear')

def aritmetisk_talfoljdsberaknare(n, a1, d):
    """
    Beräknar den aritmetiska talföljden med
    INPUT: heltal/flytttal
    n = antalet tal
    a1 - första talet i talföljden
    d - differesen
    OUTPUT: heltal/flyttal
    """
    sista_talet = a1 + d * (n - 1)
    aritmetisk_talsumma = n * (a1 + sista_talet) / 2
    return aritmetisk_talsumma

def geometrisk_talfoljdsberaknare(n, g1, q):
    """
    Beräknar den geometriska talföljden med
    INPUT: Heltal/flyttal
    n - antalet tal
    A1 - första talet i talföljden
    q - kvot mellan talen
    OUTPUT: heltal/flyttal
    """
    geometrisk_talsumma = g1 * ((q ** n) - 1)/(q - 1)
    return geometrisk_talsumma
def main():
    """
    Huvudfunktion för programmet som beräknar geometrisk och aritmetiska talsummorna
    Testar inmatningsvärden, beräknar talsummorna, jämför och skriver ut dem för användaren
    """
    #Användarens indata kontrolleras
    print("Data för den aritmetiska summan")
    a1 = olofmodullabb3.float_tester("Skriv in värdet på a1: ")
    d = olofmodullabb3.float_tester("Skriv in värdet på d: ") 
    print("Data för den geometriska summan:")
    g1 = olofmodullabb3.float_tester("Skriv in värdet för g1: ")
    q = olofmodullabb3.float_tester("Skriv in värdet för q: ")
    #q måste vara större en noll och skiljt från ett för att undvika ZeroDivisionError
    while q <= 0:
        q = olofmodullabb3.float_tester("Skriv in värdet på q")
    while q == 1:
        q = olofmodullabb3.float_tester("q får inte vara 1, försök igen: ")
    print("Antal termer i summorna")
    #Antalet tal, n, måste vara större än 0 eftersom att det annars inte är en talföljd
    n = olofmodullabb3.integer_tester("skriv in värdet på n: ")
    while n <= 0: 
        n = olofmodullabb3.integer_tester("n måste vara ett heltal större än 0, försök igen: ") 

    aritmetisk_summa = aritmetisk_talfoljdsberaknare(n, a1, d)
    geometrisk_summa = geometrisk_talfoljdsberaknare(n, g1, q)
    clear_terminal() #Rensar terminalen för att ge en mer användarvänlig upplevelse
    #Skriver ut talsummornas värde för att ge användaren en större funktionalitet av programmet 
    print(f"Den aritmetiska summan är {aritmetisk_summa}")
    print(f"Den geometriska summan är {geometrisk_summa}")

    # Jämför de olika summorna och anger vilken som är störst
    if aritmetisk_summa > geometrisk_summa:
        print("Den aritmetiska talsumman är större än den geometriska")
    elif aritmetisk_summa < geometrisk_summa:
        print("Den geometriska talsumman är större än den aritmetiska")
    elif aritmetisk_summa == geometrisk_summa:
        print("Den aritmetiska talsumman är lika med den geometriska talsumman")
    else: 
        print("ett oväntat fel uppstod, vänligen kontakta skaparen")
    clear_terminal()

if __name__ == "__main__":
    main()
