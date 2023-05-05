import os

os.system('cls' if os.name=="nt" else 'clear')

#---------------------------------------------
#--------------- PYTHON - OOP ----------------
#---------------------------------------------

# OOP = Object Oriented Programming
# Classes -> Blueprint: Mimarlarin kullandigi mavi sablon kagididir. Obje orada tanimlanmistir.
# DRY -> Don't repear yourself!

#---------------------------------------------

'''
def print_type(data_list):
    for data in data_list:
        print(data, type(data))

print_type(['Bekir', 123, 123.34, True, (1, 2, 3), [1, 2, 3], lambda x:x])
'''

#---------------------------------------------
# Creatin Class in Python:
# Classes are named in Pascal Case ( ClassName: )


'''
class ClassName:

    variable_for_class = 'value' # -> Attribute / Property

    # if (Conditions) ... --> Wrong Using...

    def example_function(parameter, arguman): # -> Method
        variable_for_func = 'value' # -> Parameter
        
        # if (Conditions) ...
'''

#---------------------------------------------

class Person:
    name = 'Bekir'
    surname = 'Adamson'

# print(Person)
# print(Person.name)
# print(Person.surname)

#---------------------------------------------
# Set Object from Class:

personel = Person() # -> Instance : Object created by using Class named Person.

print(personel)
print(personel.name)
