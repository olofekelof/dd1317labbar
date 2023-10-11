#Modul labb 3
"""
Programmet felhanterar inputs från användaren och säkerställer att de är korrekta
"""
#Olof Ekelöf
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