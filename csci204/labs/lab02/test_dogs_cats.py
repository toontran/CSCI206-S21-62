'''
A test program for classes Cat and Dog.

Converted from the Java programs developed by Brian King for the Java version
of CSCI 204.

Xiannong Meng
2017-07-26
'''
from dog import *
from cat import *

def test_pet( this_pet ):

    print(this_pet)
    pet_name = this_pet.name
    print('Taking ' + pet_name + ' for a walk')
    this_pet.walk()
    print(this_pet)

    print('Feeding ' + pet_name)
    this_pet.eat()
    print(this_pet)

    print('Sending ' + pet_name + ' to bed.')
    this_pet.sleep()
    print(this_pet)

def main():
    my_pets = [Cat('Garfield', 4),
               Dog('Sleepy', 8)]

    for pet in my_pets:
        print('--- begin ---')
        test_pet(pet)
        print('--- end ---')

main()
