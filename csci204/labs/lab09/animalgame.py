""" 
Tree lab, CSCI 204 

Tung Tran
"""
import pickle
import os


def play(node):
    """ Play the Animal Game from the given node. """
    # Your code goes here. You may write additional methods as needed.
    if node.left == None and node.right == None:
        # Hit the leaf, Make the guess
        ans = input( 'Is it a {}? '.format(node.data) ) 
        if is_yes(ans):
            print( 'Wow! I guessed it!' )
        else:
            print( 'I guessed wrong? T_T' )
            correct_animal = input( 'What animal were you thinking of? ' )
            question = input( 'What question should I have asked to tell your {} and my {} apart? '.format(node.data, correct_animal) )
            correct_ans = input( 'Is the correct answer yes or no? ' )
            
            cur_animal = node.data
            node.data = question
            if is_yes( correct_ans ):
                node.right = Node( correct_animal )
                node.left = Node( cur_animal )
            else:
                node.right = Node( cur_animal )
                node.left = Node( correct_animal )
    else:
        ans = input( node.data + ' ' )
        if is_yes(ans):
            play(node.right)
        else:
            play(node.left)       

def is_yes(response):
    """ Was this a yes response? """
    return response=="yes" or response=="y" or response=="Yes" or\
    response=="Y" or response == 'ye' or response=='Ye' or response=='YE' or\
    response=='YES'

def main():
    """ Run the Animal Game. """
    # See if they want to print the tree.
    debugMode = input("Print the tree as you play? ")
    debug = is_yes(debugMode)

    if not os.path.exists('game_data.p'):
        # Assemble the initial tree
        root = Node("Does it have feathers?")
        left = Node("tiger")
        right = Node("chicken")
        root.left = left
        root.right = right
    else:
        root = pickle.load( open('game_data.p', 'rb') )

    while True:
        print("Think of an animal.")
        play(root)
        if debug:
            root.print()
            print()
        pickle.dump( root, open('game_data.p', 'wb') ) # Save the tree #StayGreen
        response = input("Play again? ")
        if not is_yes(response): 
            print('Thank you for playing!')
            break

class Node:
    def __init__(self, data):
        """ Initialize a binary tree node with given data. The left and right
            branches are set to None (null). """
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        """ Print out the tree rooted at this node. """
        lines = []
        strings = []
        self.print_nodes(lines, strings)
        st = ""
        for string in strings:
            st = st + string
        print(st)

    def print_nodes(self, lines, strings):
        """ Helper function for print(). """
        level = len(lines)
        if self.right != None:
            lines.append(False)
            self.print_lines(lines, strings, "\n")
            self.right.print_nodes(lines, strings)
            lines.pop(level)
        else:
            self.print_lines(lines, strings, "\n")

        if level>0:
            old = lines.pop(level-1)
            self.print_lines(lines, strings, "  +--")
            lines.append(not old)
        strings.append(self.data + "\n")

        if self.left != None:
            lines.append(True)
            self.left.print_nodes(lines, strings)
            self.print_lines(lines, strings, "\n")
            lines.pop(level)
        else:
            self.print_lines(lines, strings, "\n")

    def print_lines(self, lines, strings, suffix):
        """ Helper function for print(). """
        for line in lines:
            if line: strings.append("  |  ")
            else:    strings.append("     ")
        strings.append(suffix)

main()
