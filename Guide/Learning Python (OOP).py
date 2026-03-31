"""
class myClass:  #Object-oriented programming uses classes and objects to add organisation and reusability to programs. A class is created.
    message_1 = "Hello"  #Properties are assigned to it
    message_2 = "Hi"
    message_3 = "Good morning"

greeting1 = myClass()  #The class is used to create objects
greeting2 = myClass()
greeting3 = myClass()
print(greeting1.message_1)  #The object is called
print(greeting2.message_2)
print(greeting3.message_3)

class drink:
    def __init__(self, type, brand, price):  #__init__() is used to assign values to object properties
        self.type = type  #The self parameter is a reference to the current instance of the class
        self.brand = brand
        self.__price = price  # The "__" before the property makes it private (encapsulation), binding it to the class.

    def display(self):  #Methods are functions belonging to a class. They define the behaviour of properties.
        print(f"The details of this item are: {self.type}, {self.brand}, {self.__price}")

    def get_price(self):  #A getter to access the private property
        return self.__price
    
    def set_price(self, price):  #A setter to modify the private property
        if price > 0:
            self.__price = price
        else:
            print("Price must be set")

class safe(drink):  #A child class that inherits the properties and methods of the parent class (drink) by having the parent class name in the class name.
    label = "It is safe to consume"

drink1 = safe("Wine", "G", 7.99)
drink2 = safe("Water", "Buxton", 1.99)
drink3 = safe("Fizzy", "Pepsi", 3.99)
print(drink1.get_price())  #Getting the property
drink1.set_price(6.99)  #Setting the property
drink1.display()
print(drink1.label)
drink2.display()
print(drink2.label)
drink3.display()
print(drink3.label)
"""