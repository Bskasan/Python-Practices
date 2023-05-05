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

# # Bir instance'daki ekleme/güncelleme diğer instance'ı ETKİLEMEZ.
# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# personel_1 = Person()
# personel_2 = Person()

# # print(personel_1)
# # print(personel_2)

# # personel_1.name = 'Rafe'

# # print(personel_1.name)
# # print(personel_2.name)

# personel_1.age = 40

# print(personel_1.age)
# print(personel_2.age)

#---------------------------------------------

# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# personal = Person # personal is not instance, it's class.
# other_instance = personal() # -> Created new instance from new class that is assigned above.

#---------------------------------------------

# class Person:
#     name = 'Qadir'
#     surname = 'Savran'

#     # this -> self 
#     def test(self):
#         # We use this instead of self.
#         # Self her zaman ilk arguman olmasi lazim.
#         # Instance'dan method cagirirken self parametresi yollamiyoruz.
#         print(self.name + ' ' + self.surname)

# personal = Person()

# personal.name = 'Bekir'
# personal.surname = 'Kasan'

# personal.test() # Person.test(personal) - Working like this in the background.

#---------------------------------------------

# Getter and Setter Methods

class Enemy: 
    name = 'Rusulir'
    surname = 'Dragonblade'

    # Underscore ile başlayan değişkenlerin instance tarafında çağrılmaması/değiştirilmemesi beklenir.
    # Piyasa standartıdır. Çağrılabilir.
    _team = 'Dwarves'

    # Double-Underscore ile başlayan değişkenlerin dışardan çağrılmasını engeller.
    __location = 'Khirerin Dynasty'

    def get_location(self): # Getter Method
        return self.__location

    def set_location(self, new_value): # Setter Method
        self.__location = new_value


enemy_troopy = Enemy()
print(enemy_troopy.get_location())
enemy_troopy.set_location('Acreabet Kingdom')
print(enemy_troopy.get_location())

print('##################')

#############################################
# enemy_lead = Enemy()
# print(enemy_lead.name)
# enemy_lead._team = 'Dragons'
# print(enemy_lead._team)
# print(personel.__location) # Private attr'e erişim sağlanmaz.
# print(personel._Person__location) # Private attr'e ulaşmanın yolu.
#############################################


class SendMail:

    __is_sent = False

    def set_send(self): # Setter Method
        # Mail gonderme komutlari
        # Mail gonderildikten sonra gonderildi bilgisin true yap.
        self.__is_sent = True
    
    def get_status(self): # Getter method
        # Mail gonderildi mi bilgisini ver.
        return self.__is_sent

mail = SendMail()
print('Mail Gonderildi mi?', mail.get_status())
mail.set_send()
print('Mail Gonderildi mi?', mail.get_status())

print('##################')

#---------------------------------------------






