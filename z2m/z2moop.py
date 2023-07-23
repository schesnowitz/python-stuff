# -*- coding: utf-8 -*-
"""z2mOOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nYOSu9p2MJuPSul5x1qBhx9gs9_xT0QG
"""

class Player:
    def __init__(self, name):
        self.name = name

    def run(self):
        return "Running"



player1 = Player(name="Driver")

print(player1.name)
print(player1.run())

"""@classmethod cls has access to class attributes"""

class Player:
    def __init__(self, name):
        self.name = name

    def run(self):
        return "Running"

    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2


player1 = Player(name="Driver")

print(player1.adding(1,2))
print(player1.run())

"""@staticmethod  no acceess to attibutes"""

class Player:
    def __init__(self, name):
        self.name = name

    def run(self):
        return "Running"
    # could update a Players age by adding 2 numbers to create age
    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding1(num1, num2):
        return num1 + num2


player1 = Player(name="Driver")

print(player1.adding1(1,2))
print(player1.run())

"""Inheritance"""

class User():
    # aka constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def logged_in(self):
        print("user is logged in")

class Driver(User):
    def __init__(self, passed_physical, truck_assigned, name, email):
        # User.__init__(self, name, email)
        super().__init__(name, email)
        self.passed_physical = passed_physical
        self.truck_assigned = truck_assigned


class Dispatcher(User):
    def __init__(self, live_loads, pending_loads):

        self.live_loads = live_loads
        self.pending_loads = pending_loads

dispatcher = Dispatcher(live_loads=3, pending_loads=2)
driver = Driver(passed_physical=True, truck_assigned='P72 Freightliner', name="Steve", email="steve@chesnowitz.com")
print(dispatcher.pending_loads)
print(driver.email)
print(isinstance(dispatcher, User))

"""MRO - Method Resolution Order

"""

class User():
    # aka constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def logged_in(self):
        print("user is logged in")

class Driver(User):
    def __init__(self, passed_physical, truck_assigned, name, email):
        # User.__init__(self, name, email)
        super().__init__(name, email)
        self.passed_physical = passed_physical
        self.truck_assigned = truck_assigned


class Dispatcher(User):
    def __init__(self, live_loads, pending_loads, name, email):
        User.__init__(self, name, email)
        self.live_loads = live_loads
        self.pending_loads = pending_loads

class Manager(User):
    def __init__(self, has_keys, name, email):
        User.__init__(self, name, email)
        self.has_keys = has_keys

class ManagerDispatcher(Manager, Dispatcher):
    def __init__(self, live_loads, pending_loads, has_keys, name, email):
        super().__init__(name, email, has_keys)
        Dispatcher.__init__(self, live_loads, pending_loads, name, email)


manager_dis = ManagerDispatcher(name="steve", has_keys=True, email="someemail@email.com", live_loads=7, pending_loads=0)
print(f"manager: {manager_dis.live_loads}")
print((ManagerDispatcher.__mro__))