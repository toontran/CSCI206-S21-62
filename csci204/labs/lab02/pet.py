'''CSCI 204 Lab 02 Class Design, Implementation, and Exceptions
Lab section: CSCI 204.L60, Thursday 1-2:52
Student name: Tung Tran
Instructor name: Professor Fuchberger'''


class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.activity = 'doing UNKNOWN'

    def __str__(self):
        return '{} (age: {}) is {}'.format(self.name, self.age, self.activity)

    def walk(self):
        self.activity = 'WALKING'

    def eat(self):
        self.activity = 'EATING'

    def sleep(self):
        self.activity = 'SLEEPING'

    
