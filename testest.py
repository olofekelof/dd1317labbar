class Student:
    def __init__(elev, förnamn, efternamn, personnr):
        elev.förnamn = förnamn
        elev.efternamn = efternamn
        elev.personnr = personnr

    def __str__(elev):
        return f"Student Name: {elev.förnamn} {elev.efternamn}\nPersonnummer: {elev.personnr}"

# Starta en tom lista som kan fyllas med studentinformation
student_lista = []

# Ber användaren fylla i information om studenten som ska läggas till i listan
while True:
    förnamn = input("Ange studentens förnamn (eller skriv ""q"" om du är färdig): ")
    if förnamn.lower() == 'q':
        break

    efternamn = input("Ange studentens efternamn: ")
    personnr = input("Ange studentens personnr (12 siffror utan specialtecken): ")

    if not personnr.isdigit() or len(personnr) != 12:
        print("Felaktigt personnr. Personnummret måste bestå av 12 siffror utan specialtecken.")
        continue

    # Skapar en ny student och lägger till i listan
    student = Student(förnamn, efternamn, personnr)
    student_lista.append(student)

# Visa en lista med angivna studenter
print("\nStudentlista:")
for student in student_lista:
    print(student)