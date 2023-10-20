import os #Möjliggör att användaren kan rensa terminalen
import olofmodullabb4 #importerar  felhanteringsfunktioner

def clear_terminal():
    """
    Rensar terminalen efter avslutat program
    """
    input("Tryck enter för att gå vidare")
    os.system('cls' if os.name == 'nt' else 'clear')


class Student:
    """
    Skapar en ny klass av objekt som heter Student
    En student kan ha följande attribut:
    - Förnamn
    - Efternamn
    - Personnummer

    Skapar även en metod som skriver ut vad varje objekt har för attribut
    """
    def __init__(self, first_name, family_name, personal_registration_number):
        self.firstname = first_name
        self.familyname = family_name
        self.personalregistrationnumber = personal_registration_number

    def __str__(self):
        return f"Namn: {self.firstname} {self.familyname} Personnr: {self.personalregistrationnumber}"

def student_creator():
    """
    Skapar objekt av klassen Student
    INPUT
    first_name: string
    last_name: string
    personnummer: heltal
    OUTPUT
    Ett objekt av klassen Student
    """
    first_name = olofmodullabb4.string_tester("Vad heter studenten i förnamn? : ")
    last_name = olofmodullabb4.string_tester("Vad heter studenten i efternamn? : ")
    personnummer = olofmodullabb4.integer_tester("Vad är studentens personnummer? : ")
    elev = Student(first_name, last_name, personnummer)
    print("")
    print("Objektet skapat!")
    print("")
    return elev


def main():
    """
    Användaren bestämmer hur många studenter som ska läggas till av klassen Student
    Användarens studenters information sparas i listan elevlista
    Elevlistan skrivs ut för användaren
    """
    print("Skriv in följande information om dina studenter:")
    print("")
    elevlista = [] #objektens attribut sparas i denna lista
    number_of_students = olofmodullabb4.positive_integer_tester("Hur många studenter vill du lägga till? ")
    print("")
    while number_of_students > 0: #Användaren lägger till attribut till sina studenter
        number_of_students -= 1
        elev = student_creator()
        elevlista.append(elev) #Sparar attributen med objektet i denna lista
    print("Följande information har sparats i elevlistan:")
    print("")
    for elev in elevlista: #skriver ut alla objekts attribut till användaren
        print(elev)

main()
clear_terminal()

if __name__ == "__main__": #förhindrar att programmet körs i externa moduler för att förhindra buggar
    main()