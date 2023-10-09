# Modul till Labb 3
# Tiago Venhammar
def input_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Du måste ange ett heltal, försök igen!")

def input_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Du måste ange ett flyttal, försök igen!")