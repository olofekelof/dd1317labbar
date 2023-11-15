#Grupp 43
"""
Det här är ett program som låter användaren skapa listor av elever på olika skolor.
Funktioner:
- Läser in .txt filer
- Två klasser, en av typen student, en av typen skola
- Låter användaren söka efter elever på olika skolor
- Låter användaren lägga till elever i olika skolor
"""
import tests_values # Laddar in modulen för felhantering
import sys
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

all_schools = {} #Skolor sparas med elever i detta dictionary
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
        all_schools[self.skolnamn] = self #värden sparas i dictionaries
    
    def add_students(self, student):
        """
        Lägger till elever i de olika skolorna
        """
        self.studentlista.append(student)
    
    def search_student(self, student_personnummer):
        """
        Söker efter studenter efter deras personnummer
        """
        for s in self.studentlista:
            if str(s.personalregistrationnumber) == str(student_personnummer):
                return s  #returnerar student objektet om det är vad som sökts efter
        return None #returnerar inget då ingen student finns

    def __str__(self):
        return f"Den studenten studerar vid {self.skolnamn}:"

def creates_students():
    """
    Skapar student- och skolobjektet

    Inparameter: Inga
    Return: student (objekt av student), school (objekt av skola)
    """

    #Tar input från användare och skapar objektet Student
    first_name = tests_values.string_tester("Vad heter studenten i förnamn? : ").capitalize()
    last_name = tests_values.string_tester("Vad heter studenten i efternamn? : ").capitalize()
    personnummer = tests_values.personalreg_tester("Vad är studentens personnummer? (OBS 10 SIFFROR) : ")
    student = Student(first_name, last_name, personnummer)
    
    #Tar input från användare och skapar objektet School
    skola_name_str = tests_values.string_tester("Vilken skola går eleven på? : ").upper()

    #Skapar en ny skola om den inte redan finns i uppslagsverket, om skolor redan finns returneras det redan existerande objektet
    if skola_name_str not in all_schools:
        school = School(skola_name_str)
    else:
        school = all_schools[skola_name_str]
    
    print("Objektet skapat!")
    return student, school

def reads_student_files(path_to_file):
    """
    Läser .txt filer med format: 
    1. Personnummer
    2. Efternamn
    3. Förnamn
    Output: Sorterade listor i ordning: 1) personnummer 2) efternamn 3) förnamn
    """
    with open(path_to_file, "r", encoding="utf-8") as student_file:
        personal_reg_list = []
        last_name_list = []
        first_name_list = []
        student_personal_reg = student_file.readline().strip()

        #sorterar datan i separata listor för 1) personnummer. 2) efternamn, 3) förnamn
        while student_personal_reg != "": 
            student_last_name = student_file.readline().strip()
            student_first_name = student_file.readline().strip()
            personal_reg_list.append(student_personal_reg)
            last_name_list.append(student_last_name)
            first_name_list.append(student_first_name)
            student_personal_reg = student_file.readline().strip()
        
        #Skapar objekt av klassen School 
        school_student = "KTH"
        if school_student not in all_schools:
            school = School(school_student)
        else:
            school = all_schools[school_student]
        
        print("")
        print("Dessa studenter är skrivna vid KTH:")
        print("")

        #Skapar objekt av Student och sparar student tillsammans med skolan KTH
        for i in range(len(personal_reg_list)):
            student = Student(first_name_list[i], last_name_list[i], personal_reg_list[i])
            print(student)
            school.add_students(student)
        print("")
        return first_name_list, last_name_list, personal_reg_list
        

def main():
    """
    - Läser in filer av format 1) personnummer, 2) efternamn, 3) förnamn
    - Skapar objekt av Student och School
    - Lägger till studenter i sina respektive skolor
    - Användaren ges möjlighet att söka efter studenter
    """
    #Datorn hade fel path till filen och kunde således inte öppna andra filer i samma mapp
    print("Välkommen till Grupp 43 labb 6!")
    user_file_input = tests_values.string_tester("Vill du läsa in en fil med studenter till programmet? (ja/nej)").lower()

    if user_file_input == "ja":
        file_input = tests_values.tests_file_format("Vad heter filen med alla studenter? ")
        reads_student_files(file_input)

    while True:
        print(" ")
        print(" ")
        print("Välkommen till studentlistan!")

        function_choice = tests_values.positive_integer_tester("Vill du (1) söka efter en student i listan, (2) lägga till studenter i listan, eller (3) se listan med studenter? : ")
        while True: 
            #låter användaren lägga till studenter
            if function_choice == 2: 
                #Input av användarens val av studenter
                print("Skriv in följande information om dina studenter:\n")
                number_of_students = tests_values.positive_integer_tester("Hur många studenter vill du lägga till? ")
                print("")

                #Skapar Student och School objekt samt lägger till elever i respektive skola
                if number_of_students > 0:    
                    while number_of_students > 0:
                        number_of_students -= 1
                        student, school = creates_students()
                        school.add_students(student)
                else:
                    print("Okej, du har beslutat att inte lägga till några nya studenter")
                    print("")

                #avbryter programmet om det inte finns någon data för programmet att använda
                if len(all_schools) == 0:
                    sys.exit("Programmet har ingen data att hantera! Programmet avlsutas. Ha en trevlig dag!")
                break

            #skriver ut alla studenter
            elif function_choice == 3: 
                print("Här är listan med skolor och deras elever:")
                for school_name, school_obj in all_schools.items():
                    print(f"Skola: {school_name}")
                    for student in school_obj.studentlista:
                            print(f"   {student}")
                break
            #Låter användaren söka efter en student
            elif function_choice == 1: 
                search_value = tests_values.personalreg_tester("Vad har studenten för personnummer? : ")
                
                #Användaren får söka efter specifika studenter m.h.a personnummer
                #Returnerar om studenten finns samt informationen som finns sparad hos den
                found = False
                for specific_school in all_schools.values():
                    student = specific_school.search_student(search_value)
                    if student:
                        print(specific_school)
                        print(student)
                        found = True
                        break
                if not found:
                    print("Det finns tyvärr ingen sådan student")
                break
            else:
                print("Okej, ha en trevlig dag")

if __name__ == "__main__":
    tests_values.clear_terminal()
    main()
    tests_values.clear_terminal()