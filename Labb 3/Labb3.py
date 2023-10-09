#Labb 3
# Tiago Venhammar
import os
import curses
import Labb3modul

def clear_terminal():
    input("Tryck ENTER för att gå vidare!")
    os.system('cls' if os.name == 'nt' else 'clear')

def aritmetisk_summa(a1, d, n):
    a_n = a1 + d * (n-1)
    a_summa = n * (a1 + a_n)/2
    return a_summa

def geometrisk_summa(g1, q, n):
    g_summa = g1 * ((q ** n - 1) / (q - 1))
    return g_summa
while True:
    print("Hej och välkommen till ännu en summe-jämförare!")
    print("Ange dina ingångsvärden")
    def main():
        while True:
            a1 = Labb3modul.input_float("Vad är värdet för a1?: ")
            print("Du har angett värdet", a1, "!")

            d = Labb3modul.input_float("Vad är värdet för d?: ")
            print("Du har angett värdet", d, "!")

            clear_terminal()
            
            aritmetisk = aritmetisk_summa(a1, d, n)

            print("Den aritmetiska summan är:", aritmetisk)

            g1 = Labb3modul.input_int("Vad är värdet för g1?: ")
            print("Du har angett värdet", g1, "!")

            q = Labb3modul.input_int("Vad är värdet för q?: ")
            print("Du har angett värdet", q, "!")

            while q <= 0:
                q = Labb3modul.input_int("Vad är värdet för q?: ")

            n = Labb3modul.input_int("Vad är värdet för n?: ")
            print("Du har angett värdet", n, "!")

            while n <= 0:
                n = Labb3modul.input_int("Felaktigt värde, n måste vara > 0, vad är värdet för n?: ")
                print("Du har angett värdet", n, "!")

            clear_terminal()
            
            geometrisk = geometrisk_summa(g1, q, n)

            print("Den geometriska summan är:", geometrisk)
            print("Den aritmetiska summan är:", aritmetisk)

            def jamfor_summa(summa1, summa2, rubrik1, rubrik2):
                if summa1 > summa2:
                    print(f"Den {rubrik1} summan är störst!")
                elif summa1 < summa2:
                    print(f"Den {rubrik2} summan är störst!")
                else:
                    print(f"{rubrik1} och {rubrik2} är lika stora!")

            if aritmetisk != 0 or geometrisk != 0:
                jamfor_summa(aritmetisk, geometrisk, "aritmetiska", "geometriska")
            clear_terminal()

            print("Bra jobbat!, vill du fortsätta jämföra summor eller vill du avsluta programmet?")
            print("För att fortsätta jämföra, skriv 'y' och tryck ENTER")
            print("För att avsluta, skriv 'n' och tryck ENTER")
            avsluta = input("y/n: ")
            if avsluta == "y":
                print("Du har valt att fortsätta! Kul för dig.")
            else:
                print("Du har valt att avsluta! Kul för dig.")
                break
            clear_terminal()
    break
if __name__ == "__main__":
    main()