#Modul labb 5
"""
Programmet felhanterar inputs från användaren och säkerställer att de är korrekta
"""
#Olof Ekelöf

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
            user_input = str(input(prompt))
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
            value = input(prompt)  # Frågar användaren om ett värde
            value = int(value)  # Försöker omvandla värdet till ett heltal

            if value > 0:  # Kontrollerar om värdet är ett positivt heltal
                return value 
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
            value = input(prompt)  # Frågar användaren om ett värde
            value = int(value)  # Försöker omvandla värdet till ett heltal

            if value > 0 and len(str(value)) == 12:  # Kontrollerar om värdet är ett positivt heltal
                return value
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