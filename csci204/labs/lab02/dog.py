'''CSCI 204 Lab 02 Class Design, Implementation, and Exceptions
Lab section: CSCI 204.L60, Thursday 1-2:52
Student name: Tung Tran
Instructor name: Professor Fuchberger'''


from pet import *


class Dog(Pet):

    def walk(self):
        self.activity = 'WALKING'
        print('Walk?!?! Oh boy oh boy!!! Pant! Pant! Pant!')

    def eat(self):
        self.activity = 'EATING'
        print('Begging for food... kibbles and bits please.')

    def sleep(self):
        self.activity = 'SLEEPING'
        print('Zzzzzz (drooling)...')
