#Python માં Object Oriented Programming (OOP) એ એવી શૈલી છે જેમાં તમે વસ્તુઓ (objects) અને કલાસો (classes)ના આધાર પર પ્રોગ્રામ લખો છો.
#OOPs પદ્ધતિ Code ને વધુ organize, reusable અને scalable બનાવે છે.

#OOPs ના 4 મુખ્ય પિલ્લર
    # 1.Class – મોડેલ કે structure

    # 2.Object – Class નો instance

    # 3.Encapsulation(એન્કેપ્સ્યુલેશન) – ડેટા અને ફંક્શન્સને એકમમાં છુપાવવું

    # 4.Inheritance – એક class બીજી class ની વિશેષતાઓ લે શકે
   
    # 5.Polymorphism – એક જ નામના ફંક્શન્સ/મેથડ્સ જુદી રીતે કામ કરે


# 1. Class અને Object શું છે?
    #Class એ template છે જેમાંથી object બનાવાય છે.
    #Object એ class નું instance છે, એટલે કે original object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Object બનાવો
s1 = Student("Ravi", 20)
s1.display()

#2. Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

acc = Account(1000)
print(acc.get_balance())  # Output: 1000

    #🔹 3. Inheritance
    #એક Class બીજી Class ની વિશેષતાઓ મેળવે છે.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Parent class method
d.bark()   # Child class method

#🔹 4. Polymorphism
    #એક Function અથવા Method જુદા-જુદા objects માટે જુદી રીતે વર્તે છે.

class Cat:
    def sound(self):
        print("hello")

class Dog:
    def sound(self):
        print("hello2")

# polymorphism example
for animal in (Cat(), Dog()):
    animal.sound()