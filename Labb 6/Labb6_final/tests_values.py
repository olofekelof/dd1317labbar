
#Modul labb 6
"""
Programmet felhanterar inputs från användaren och säkerställer att de är korrekta
"""

import os

def integer_tester(prompt):
    """
    Testar om ett värde är ett heltal och ger ett felmeddelande
    """
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Det där var inte ett heltal, försök igen")

def float_tester(prompt):
    """
    Testar om ett värde är ett flyttal och ger ett felmeddelande om det är det
    """
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Det där var inte ett flyttal, försök igen")


def string_tester(prompt):
    """
    Testar om ett värde är en string
    Input: Användarens inmatning
    Output: En string
    """
    while True:
        try:
            user_input = str(input(prompt)).strip()
            if not user_input:
                print("Du måste ange ett namn : ")
                continue
            return user_input
        except ValueError:
            print("Namnet får bara innehålla bokstäver, försök igen! : ")

def positive_integer_tester(prompt):
    """
    Testar om ett värde är ett positivt heltal
    Input: Användarens inmatning
    Output: Ett positivt heltal
    """
    while True: 
        try:
            value_str = input(prompt).strip()  # Frågar användaren om ett värde
            value_int = int(value_str)  # Försöker omvandla värdet till ett heltal

            if value_int >= 0:  # Kontrollerar om värdet är ett positivt heltal
                return value_int 
            else:  # Om värdet inte är positivt, informeras användaren och loopen fortsätter
                print("Det angivna värdet är inte ett positivt heltal, försök igen! : ")
                
        except ValueError:  # Fångar ett undantag om omvandlingen till heltal misslyckas
            print("Antalet studenter måste anges i form av heltal, försök igen! : ")

def personalreg_tester(prompt):
    """
    Testar om ett värde är ett positivt heltal
    Input: Användarens inmatning
    Output: Ett positivt heltal
    """
    while True: 
        try:
            value_str = input(prompt)  # Frågar användaren om ett värde
            value_int = int(value_str)  # Försöker omvandla värdet till ett heltal
            
            if value_int > 0 and len(value_str) == 10:  # Kontrollerar om värdet är ett positivt heltal och har en längd på 10 siffror
                return value_int
            else:  # Om värdet inte är positivt, informeras användaren och loopen fortsätter
                print("Det angivna värdet är inte på rätt format, försök igen! : ")
                
        except ValueError:  # Fångar ett undantag om omvandlingen till heltal misslyckas
            print("Antalet studenter måste anges i form av heltal, försök igen! : ")

def clear_terminal():
    """
    Rensar terminalen efter avslutat program
    """
    input("Tryck enter för att gå vidare")
    os.system('cls' if os.name == 'nt' else 'clear')

def tests_file_format(prompt):
    """
    Testar om en fil har ändelsen .txt samt felhanterar om ingen sådan fil finns eller om den redan finns
    Output: En fil som inte redan existerar på korrekt format
    """
    while True:
        try:
            file_format = input(prompt)
            with open(file_format, "r", encoding="utf-8") as file:
                lines = file.readlines()
                lines = None
            if file_format.endswith(".txt"):
                return file_format
            else:
                print("Filen du matade in var inte på rätt format (ändelse = .txt), försök igen! : ")
        except FileNotFoundError:
            print("Den filen fanns inte! Skriv in en ny fil: ")
        except FileExistsError:
            print("Den filen finns redan, försök igen med en ny! : ")
