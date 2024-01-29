'''CSCI 204 Lab 02 Class Design, Implementation, and Exceptions
Lab section: CSCI 204.L60, Thursday 1-2:52
Student name: Tung Tran
Instructor name: Professor Fuchberger'''


from pet import *


class Cat(Pet):

    def walk(self):
        self.activity = 'WALKING'
        print('Walk? Dude, seriously?')

    def eat(self):
        self.activity = 'EATING'
        print('Lasagna, please.')

    def sleep(self):
        self.activity = 'SLEEPING'
        print('Yes. I need 23 hours of this each day!')
