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

# class Person:
#     name = 'Bekir'
#     surname = 'Adamson'

# # print(Person)
# # print(Person.name)
# # print(Person.surname)

# #---------------------------------------------
# # Set Object from Class:

# personel = Person() # -> Instance : Object created by using Class named Person.

# print(personel)
# print(personel.name)

# print('--------------------------')

# personel.name = 'Qadir'
# personel.surname = 'Stefano'
# personel.age = 40

# print(personel.name)
# print(personel.surname)
# print(personel.age)

# print('--------------------------')

# # We don't want to change the original class. That's why we use OOP Concepts.
# print(Person.name)
# # print(Person.age) -> Change we made in Instances don't affect the original class. 

#---------------------------------------------

'''

# Class'da yapilan degisiklikler Instance i etkilerler.

class Person:
    name = 'Qadir'
    surname = 'Adamson'

personel_1 = Person()

print(personel_1.name)

Person.name = 'Rafe'

print(personel_1.name)

'''

#---------------------------------------------