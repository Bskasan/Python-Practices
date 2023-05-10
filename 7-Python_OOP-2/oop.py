import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP - 2
# ---------------------------------------------
# Encapcullation: 
# -> Kapsülleme. Aynı amaç için kullanılan değişken ve methodları bir class içinde yazıyor olmsı  ve class içinde tanımlanan private attre erişelmiyor olması.
# -> Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.
# --------------------------------------------- 
# Abstraction: Soyutlama. Kodların gizliliği ve birbirinde bağımsız çalışmaları. Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages. That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity.
# ---------------------------------------------
# Inheritance: Miras Alma. Bir classın tüm özelliklerinin başka bir classa aktarılmasına denir. Inheritance allows us to define a class that inherits all the methods and properties from another class.Parent class is the class being inherited from, also called base class.Child class is the class that inherits from another class, also called derived class.
# Polymorphism: Miras alınan (inherit edilen) classın özellik/metodlarını yeniden yazılabilyor/değiştirebiliyor olmasına denir. What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

# ---------------------------------------------

class Person:
    company = 'Google'

    def __init__(self, name, age, gender='Male'):
        self.name = name
        self.age = age
        self.gender = gender
        print('Person has been created!')

    def __str__(self):
        return f'{self.name} - {self.age}'

    def getDetails(self):
        return f'Name: {self.name} - Age : {self.age} - Gender : {self.gender} - Company : {self.company}'
    


# person_1 = Person('Bekir', 29)
# Bir classın atandığı değişkene instance denir.
# Bir classtan türetilmiş objeye instance denir.
# print(person_1)
# print(person_1.getDetails())

# ---------------------------------------------

class Department:

    def __init__(self):
        print('Departman çalıştı.')

    def set_department(self, department):
        self.department = department

# ---------------------------------------------
#! Inheritance (Inherited from another class called Person.)
#! JS -> class Employee extends Person
#! Person classının tüm özellikleri Employee classına aktarıldı.
class Employee(Person):

    salary = 5000

    def set_salary(self, salary):
        self.salary = salary

    # Override:
    def __init__(self, name, age, gender, salary, department='AWS'):
        # Super(), inherit ettiğimiz ilk class'dan itibaren bulduğu ilk methodu çağırır.
        super().__init__(name, age, gender)
        # Inherit edilen class methodunu çalıştırma:
        # super() kullanmıyor isek self parametresi gönderilmelidir.
        Department.set_department(self, department)
        self.salary = salary

    # Polymorphism (Override, Overload)
    # Mevcut bir methodu tekrar tanımlama imkanına "Polymorphism" denir.
    # Yeni methodun eski methodu ezmesine "override" denir.
    # Yeni method ile eski methodun aynı anda aktif olmasına da "overload" denir.
    # Python "overload" desteklemez.
    def get_detail(self):
        return f'{self.name} - {self.age} - {self.salary} - {self.gender} - {self.company} - {self.department}'

# person_1 = Employee('Busra', 29, 'Female')
# person_1.set_salary(3000)
# print(person_1.get_detail())

person_1 = Employee('Selim', 34, 'Male', 1500, 'Fullstack')
# person_1.set_department('FullStack')
print(person_1.get_detail())


