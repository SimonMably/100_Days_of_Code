
# Class inheritance is the inheritance of attributes and methods from a
# parent class to a child class (or a class taking attributes and methods
# from another class and using them as its own).
#    A child class can, not only, inherit attributes and methods, but they can
# have their own versions of the same attributes and methods (the same named
# method appearing in the parent class and the child class). The parent class
# can have a method that does a more general thing that fits every situation
# while a child class can have its own version of the same method that is
# modified specifically for that child class. This modified method within the
# child class will override the parent class variation of the same method.
#   Inheritance allows us to take an existing class that we or someone else
# has created and build on top of it without having to reinvent the wheel and
# redefine everything that's in a class.

# eg
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        # super() refers to the parent class. Placing 'super().__init__()'
        # inside child class init method (or constructor) will allow child
        # class to inherit (or take on and use) all of the parent classes
        # attributes and methods. The super() method is recommended but not
        # strictly required.
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water")


nemo = Fish()
# Method from Fish() class
nemo.swim()
# Method inherited from Animal() class, accessed via Fish() class, also modified
nemo.breathe()
# Attribute inherited from Animal() class, accessed via Fish() class
print(nemo.num_eyes)

#
