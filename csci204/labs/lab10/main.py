"""
This is a suggested solution for the list lab in CSCI 204. It was created
by CSCI 204 instructors.

In the lab exercise, students are asked to implement methods in the list adt
 using a linked list structure. Students are also asked to implement an iterator
 for the list and to write a main function (main.py) to test the list

Revised:
Christopher Dancy
2016-09-27
"""
from linkedlist import *

def main():
    new_list = create_list(10)
    new_list.append(12)
    print("Should be: 0 1 2 3 4 5 6 7 8 9 12")
    
    for item in new_list:
        print(str(item) + " ", end="")
    print(str(new_list.peek(10) == 12) + " - ")
    new_list.insert(25, 5)
    print("After insert @ 5, should be: 0 1 2 3 4 25 5 6 7 8 9 12")
    for item in new_list:
        print(str(item) + " ", end="")
    print("Peek @ 5 should be 25 " + str(new_list.peek(5) == 25) + " - ")
    new_list.pop()
    print("After pop, should be: 0 1 2 3 4 25 5 6 7 8 9")
    
    for item in new_list:
        print(str(item) + " ", end="")
    print("\nPeek @ 11 should result in exception.")
    try:
        new_list.peek(11)
        print(" - No exception.")
    except ListException:
        print(" - Exception.")

def create_list(list_size):
    new_list = List()
    for i in range(list_size):
        new_list.append(i)
    return (new_list)

main()
