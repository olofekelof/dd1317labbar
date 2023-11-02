import os
import vardetestare2

def clear_terminal():
    """
    Rensar terminalen
    """
    input("Tryck enter för att gå vidare")
    os.system('cls' if os.name == 'nt' else 'clear')

class Student:
    """
    Skapar obejektet student
    """
    def __init__(self, first_name, family_name, personal_registration_number):
        """
        En student kan ha följande attribut:
        Förnamn - Sträng
        Efternamn - Sträng
        Personnummer - Heltal
        """
        self.firstname = first_name
        self.familyname = family_name
        self.personalregistrationnumber = personal_registration_number

    def __str__(self):
        return f"Namn: {self.firstname} {self.familyname} Personnr: {self.personalregistrationnumber}"

alla_skolor = {}
class School:
    """
    Skapar objektet skola
    """
    def __init__(self, skola):
        """
        En skola har attributet skolnamn samt en lista av studenter till varje skolnamn
        """
        self.skolnamn = skola
        self.studentlista = []
        alla_skolor[self.skolnamn] = self
    
    def add_students(self, elev):
        """
        Lägger till elever i de olika skolorna
        """
        self.studentlista.append(elev)
    
    def search_student(self, student_personnummer):
        """
        Söker efter studenter efter deras personnummer
        """
        for s in self.studentlista:
            if s.personalregistrationnumber == student_personnummer:
                return s  #returnerar student objektet om det är vad som sökts efter
        return None #returnerar inget då ingen student finns

    def __str__(self):
        return f"Den studenten läser på {self.skolnamn}:"

def student_creator():
    """
    Skapar student- och skolobjektet
    """
    first_name = vardetestare2.string_tester("Vad heter studenten i förnamn? : ").capitalize()
    last_name = vardetestare2.string_tester("Vad heter studenten i efternamn? : ").capitalize()
    personnummer = vardetestare2.personalreg_tester("Vad är studentens personnummer? (OBS 12 SIFFROR) : ")
    elev = Student(first_name, last_name, personnummer)
    
    skola_name_str = vardetestare2.string_tester("Vilken skola går eleven på? : ").upper()

    if skola_name_str not in alla_skolor:
        skola_name = School(skola_name_str)
    else:
        skola_name = alla_skolor[skola_name_str]
    
    print("Objektet skapat!")
    return elev, skola_name


def main():
    """
    Skapar studenter efter användarens inputs
    Lägger till studenter i skolor
    Ger användaren möjlighet att söka efter studenter
    """
    print("Skriv in följande information om dina studenter:\n")
    number_of_students = vardetestare2.positive_integer_tester("Hur många studenter vill du lägga till? ")

    print("")
    while number_of_students > 0:
        number_of_students -= 1
        elev, skola_namn = student_creator()
        skola_namn.add_students(elev) #lägger till elever i respektive skola

    sok_funktion = vardetestare2.string_tester("Vill du söka efter en student? (Ja/Nej) ").capitalize()
    if sok_funktion == "Ja": #1 är det input som tilllåter att en användare får söka efter elever
        sok_varde = vardetestare2.positive_integer_tester("Vad har studenten för personnummer? : ")
        
        found = False #detta avsnitt är skapat av chat gpt
        for school_name, school_obj in alla_skolor.items():
            elev = school_obj.search_student(sok_varde)
            if elev:
                print(school_obj)
                print(elev)
                found = True
                break
        if not found:
            print("Det finns tyvärr ingen sådan student") #slut här
    else:
        print("Okej, ha en trevlig dag")

if __name__ == "__main__":
    clear_terminal()
    main()
    clear_terminal()
