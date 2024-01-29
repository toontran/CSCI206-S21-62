""" Game to play 'Lost Rovers'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
Put the three ADTs in their own files.
"""
from gameboard import *
from random import *
from MatrixADT import * #from lab 4
from StackADT import * #from stack exercise
from Queue import * # for phase 5

class Game:
    SIZE = 15 # rooms are 15x15
    def __init__(self):
        # put other instance variables here
        self.gui = GameBoard("Lost Rover", self, Game.SIZE)
        self.room = Room() # populates a random setup
        #self.rooms = [] # should we do this ?
        self.room.generate_portals()
        self.room.generate_ship_components()
        self.room.generate_parts()
        self.rover = Rover() # populates a Rover that starts at a random location
        self.inventory = Inventory() # list to represent inventory implemented with linked notes
        self.python_inv = {} # type: dictionary
        self.stack = Stack() #phase 4, stack adt to hold portals that the rover stepped through
        self.steps_counter = 0 #count the steps the rover has moved to generate new tasks
        self.queue = Queue(10) # phase 5, queue adt to hold the tasks with a maximum of 10 tasks at a time
        task1 = Task()
        task1.generate_a_task()
        self.queue.enqueue(task1)
        task2 = Task()
        task2.generate_a_task()
        self.queue.enqueue(task2)




    def start_game(self):
        self.gui.run()
    def populating_a_room(self):
        '''
        manipulates the behaviour of the game when the rover lands on a portal
        if the portal it has landed on is unconnected, then created a new room and make the connection
        if the portal it has landed on is connected then simply travel to the connected portal and arrive at the connected room
        '''

        #first check the portal the rover is on to see if it has a connection to it or not
        # if there is no connection then we create the new room and put a portal beneath the rover and connect that portal to the portal we stepped in
        if self.room.board[self.rover.getX(), self.rover.getY()].next == None:
            prev_por = self.room.board[self.rover.getX(), self.rover.getY()]
            prev_por.data = self.room
            self.room = Room()
            self.room.generate_parts()
            self.room.generate_portals()
            new_por = Portal()
            new_por.set_image_portal()
            self.room.board[self.rover.getX(), self.rover.getY()] = new_por
            new_por.data = self.room
            new_por.next = prev_por
            prev_por.next = new_por
        else:
            self.room = self.room.board[self.rover.getX(), self.rover.getY()].next.data

    def get_rover_image(self):
        """ Called by GUI when screen updatesself.room = Room().
            Returns image name (as a string) of the rover.
		(Likely 'rover.ppm') """
        return 'rover.ppm'

    def get_rover_location(self):
        """ Called by GUI when screen updates.
            Returns location (as a Point Object). """
        # Your code goes here, this code is just an example
        # maybe an if statement to first initialize the Rover after that we would just return updated location (as a Point object)
        #return self.rover_location()
        if self.rover.getX() == None and self.rover.getY() == None:
            self.rover.spawn_rover()
        return Point(self.rover.getX(), self.rover.getY())



    def get_image(self, point):
        """ Called by GUI when screen updates.
            Take in Point object as an input
            Returns: .ppm (as a string) or None for the
		part, ship component, or portal at the given
		coordinates. ('engine.ppm' or 'cake.ppm' or
		'portal.ppm', etc)
            Called every single time for every single coordinate point in the room if a button is pressed
            """
        # Your code goes here, this code is just an example
        # return self.room.get_item().get_image()
        x = point.getX()
        y = point.getY()
        #then fill this coordinate into Room and get the object there then get the picture off of the object
        if self.room.board[ x , y ] != None:
            return self.room.board[ x , y ].getImage()

    def go_up(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self.rover.getY() != 0:
            self.rover.setY(self.rover.getY()-1)
        object = self.room.board[self.rover.getX(), self.rover.getY()]
        '''if type(object) == Portal and object.image == 'portal-flashing.ppm':

            self.populating_a_room()
            object.set_image_portal()
            self.portal_stack(object)'''
        if type(object) == Portal:
            self.populating_a_room()
            self.portal_stack(object)
            self.reset_portals()
        self.steps_counter += 1
        return Point(self.rover.getX(), self.rover.getY())


    def go_down(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self.rover.getY() != 14:
            self.rover.setY(self.rover.getY()+1)
        object = self.room.board[self.rover.getX(), self.rover.getY()]
        '''if type(object) == Portal and object.image == 'portal-flashing.ppm':

            self.populating_a_room()
            object.set_image_portal()
            self.portal_stack(object)'''
        if type(object) == Portal:
            self.populating_a_room()
            self.portal_stack(object)
            self.reset_portals()
        self.steps_counter += 1
        return Point(self.rover.getX(), self.rover.getY())

    def go_left(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self.rover.getX() != 0:
            self.rover.setX(self.rover.getX()-1)
        object = self.room.board[self.rover.getX(), self.rover.getY()]
        '''if type(object) == Portal and object.image == 'portal-flashing.ppm':

            self.populating_a_room()
            object.set_image_portal()
            self.portal_stack(object)'''
        if type(object) == Portal:
            self.populating_a_room()
            self.portal_stack(object)
            self.reset_portals()
        self.steps_counter += 1
        return Point(self.rover.getX(), self.rover.getY())

    def go_right(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        if self.rover.getX() != 14:
            self.rover.setX(self.rover.getX()+1)
        object = self.room.board[self.rover.getX(), self.rover.getY()]
        '''if type(object) == Portal and object.image == 'portal-flashing.ppm':

            self.populating_a_room()
            object.set_image_portal()
            self.portal_stack(object)'''
        if type(object) == Portal:
            self.populating_a_room()
            self.portal_stack(object)
            self.reset_portals()
        self.steps_counter += 1
        return Point(self.rover.getX(), self.rover.getY())

    def portal_stack(self, portal):
        if self.stack.is_empty():
            self.stack.push(portal.next)
        elif self.stack.peek() != portal: #the rover is on a new portal
            self.stack.push(portal.next)
        elif self.stack.peek() == portal:# the portal the rover is standing on is indeed the way back
            popped_portal = self.stack.pop()



    def show_way_back(self):
        """ Called by GUI when button clicked.
            Flash the portal leading towards home. """
        print(self.stack)
        if not self.stack.is_empty():
            way_back = self.stack.peek()
            way_back.set_image_flashing()
        else:
            pass

    def reset_portals(self):
        '''
        everytime the rover goes through a portal resets the image of the portal on top
        of the stack from flashing to normal portal
        '''
        if not self.stack.is_empty():
            portal = self.stack.peek()
            portal.set_image_portal()
        else:
            pass


    def get_inventory(self):
        """ Called by GUI when inventory updates.
            Returns entire inventory (as a STRING).
		3 cake
		2 screws
		1 rug
	  """
        #traverse through the linked list then count the number of items then return it as a STRING
        bagel = 0
        cake = 0
        gear = 0
        lettuce = 0
        screw = 0
        ### linked list implementation of the GUI
        '''node = self.inventory._head
        while node != None:
            if node.data == 'cake':
                cake += 1
            elif node.data == 'bagel':
                bagel +=1
            elif node.data == 'gear':
                gear +=1
            elif node.data == 'lettuce':
                lettuce +=1
            elif node.data == 'screw':
                screw +=1
            node = node.next
            '''
        for key in self.python_inv:
            if key == 'bagel':
                bagel = self.python_inv[key]
            elif key == 'cake':
                cake = self.python_inv[key]
            elif key == 'gear':
                gear = self.python_inv[key]
            elif key == 'lettuce':
                lettuce = self.python_inv[key]
            elif key == 'screw':
                screw = self.python_inv[key]
        s= ''
        if bagel != 0:
            s += str(bagel)+' bagel'+'\n'
        if cake != 0:
            s += str(cake)+' cake'+'\n'
        if gear != 0:
            s += str(gear)+' gear'+'\n'
        if lettuce != 0:
            s += str(lettuce)+' lettuce'+'\n'
        if screw != 0:
            s += str(screw)+' screw'+'\n'
        return s




    def pick_up(self):
        """ Called by GUI when button clicked.
		If rover['bagel.ppm', 'cake.ppm', 'gear.ppm', 'lettuce.ppm', 'screw.ppm'] is standing on a part (not a portal
		or ship component), pick it up and add it
		to the inventory. """
        # check if the rover is standing on a part
        if type(self.room.board[self.rover.getX(), self.rover.getY()]) == Part:
            #add the part to the inventory and delete the part on the board
            item = self.room.board[self.rover.getX(), self.rover.getY()]
            self.room.board[self.rover.getX(), self.rover.getY()] = None
            item_image = item.getImage()[:-4] #get rid of .ppm
            if item_image not in self.python_inv:
                self.python_inv[item_image] = 1
            else:
                self.python_inv[item_image] += 1
            print(self.python_inv)
            if len(self.inventory) == 0:
                node = Node(item_image)
                self.inventory._head = node
                self.inventory._current = self.inventory._head
                self.inventory._size += 1
                #print(self.inventory)
            else:
                node = Node(item_image)
                self.inventory._current.next = node
                self.inventory._current = node
                self.inventory._size += 1
                #print(self.inventory)


    def get_current_task(self):
        """ Called by GUI when task updates.
            Returns top task (as a string).
		'Fix the engine using 2 cake, 3 rugs' or
		'You win!'
 	  """
        if not self.queue.is_empty():
            return self.queue.peek()
        else:
            print('You Win')

    def perform_task(self):
        """ Called by the GUI when button clicked.
            If necessary parts are in inventory, and rover
            is on the relevant broken ship piece, then fixes
            ship piece and removes parts from inventory. If
            we run out of tasks, we win. """
        # check for broken component
        # check for items in inventory
        # delete those items from inventory
        # reset image to unbroken
        object = self.room.board[self.rover.getX(), self.rover.getY()]
        current_task = self.queue.peek()
        print(self.enough_items(current_task))
        if type(object) == Ship_Component and 'broken' in object.image and self.enough_items(current_task) == True:
            object.image = object.image.replace('broken','') # change the image to a non-broken one
            self.decrement_items(current_task)
            self.queue.dequeue()
            self.steps_counter = 0

    def decrement_items(self,task):
        '''if you have enough items in your inventory, delete the amount of items needed for the task you performed '''
        list_amount = [task.item1_amount, task.item2_amount, task.item3_amount]
        task.item1 = task.item1.lower()
        task.item2 = task.item2.lower()
        task.item3 = task.item3.lower()
        list_items = [task.item1, task.item2, task.item3]
        print(list_items)
        for i in range(len(list_items)):
            self.python_inv[list_items[i]] -= list_amount[i]

    def enough_items(self, task):
        '''
        Check if you have the right types and amount of parts needed to carry out the task, Return a boolean
        Input: Task object, that means we have access to all the attributes of that Task object
        '''
        flag = False
        list_keys = list(self.python_inv.keys())
        print(list_keys)
        task.item1 = task.item1.lower()
        task.item2 = task.item2.lower()
        task.item3 = task.item3.lower()
        if task.item1 in self.python_inv and task.item2 in self.python_inv and task.item3 in self.python_inv :
            print('heyyy')
            if task.item1_amount <= self.python_inv[task.item1] and task.item2_amount <= self.python_inv[task.item2] and task.item3_amount <= self.python_inv[task.item3]:
                print('lolollol')
                flag = True
        return flag


    def generate_new_tasks(self):
        if self.steps_counter == 25:
            new_task = Task()
            self.queue.enqueue(new_task)
            self.steps_counter = 0
    # Put other methods here as needed.

# Put other classes here or in other files as needed.
class Task:
    def __init__(self):
        self.task_name = None
        self.item1 = None
        self.item1_amount = 0
        self.item2 = None
        self.item2_amount = 0
        self.item3 = None
        self.item3_amount = 0
    def generate_a_task(self):
        '''randomize type of item and the amount of each item '''
        self.item1_amount = randint(1,3)
        self.item2_amount = randint(1,3)
        self.item3_amount = randint(1,3)
        parts_list= ['Bagel', 'Cake', 'Gear', 'Lettuce', 'Screw']
        broken_list = ['Broken Engine', 'Broken Cabin', 'Broken Exhaust']
        shuffle(parts_list)
        shuffle(broken_list)
        self.task_name = broken_list[0]
        self.item1 = parts_list[0]
        self.item2 = parts_list[1]
        self.item3 = parts_list[2]

    def __repr__(self):
        '''repr function to represent the task '''
        s = self.task_name +'! To fix the engine you will need:\n' + '- '+ str(self.item1_amount) + ' ' + self.item1+ '\n' + '- '+ str(self.item2_amount) + ' ' + self.item2+ '\n' + '- '+ str(self.item3_amount) + ' ' + self.item3+ '\n'
        return s

class Room:
    '''
    Creates a grid with coordinates and places items by using Item objects and coordinates (from the Item class) correspondingly
    '''

    def __init__(self):
        self.board = Matrix(15,15) #creates a grid with None type in every cell

    def generate_ship_components(self):
        ''' This would hardcode ship component using spawn_components and set_image then append it to self.components_list '''
        a= [2,4,5]
        shuffle(a)
        for (i,times) in enumerate(a):
            for time in range(times):
                component = Ship_Component()
                component.image = component.ship_components[i]
                component.spawn_component()
                if self.board[component.getX(),component.getY()] == None:
                    self.board[component.getX(),component.getY()] = component


    def generate_portals(self):
        n_portals = randint(2,4) # we allow for a maximum of 3 portals
        for i in range(n_portals): # different number of portals every time
            portal = Portal()
            portal.set_image_portal()
            portal.spawn_item()
            if self.board[portal.getX(),portal.getY()] == None:
                self.board[portal.getX(),portal.getY()] = portal

    def generate_parts(self):
        a = [0, 1, 2, 3, 4]
        shuffle(a)
        for (i,times) in enumerate(a):
            for time in range(times):
                part = Part()
                part.image = part.ship_parts[i]
                part.spawn_item()
                if self.board[part.getX(),part.getY()] == None:
                    self.board[part.getX(),part.getY()] = part
class Item:
    '''
    Creates an Item object that has a pair of coordinates and an image indicating what the Item is
    Then we'll have the ShipComponent, Parts, and Portals subclasses that share the methods but differ in self.image
    '''
    def __init__(self):
        self.x = None
        self.y = None
        self.image = None
        self.point = None

    '''def set_image_random(self):
        #Do what Dancy did initially with his get_image
        pass'''
    def spawn_item(self):
        x = randint(0,14)
        y = randint(0,14)
        self.setX(x)
        self.setY(y)
    #setters
    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value
    #getter
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImage(self):
        return self.image

class Ship_Component(Item):
    '''
    hard coding the positions of ship components
    determining the .ppm through randomint
    '''
    def __init__(self):
        super().__init__()
        self.ship_components = ['cabinbroken.ppm', 'enginebroken.ppm', 'exhaustbroken.ppm']
    # spawn components bearing the pre-determined condition
    def spawn_component(self):
        x = randint(5,9)
        y = randint(5,9)
        self.setX(x)
        self.setY(y)

class Part(Item):
    def __init__(self):
        super().__init__()
        self.ship_parts = ['bagel.ppm', 'cake.ppm', 'gear.ppm', 'lettuce.ppm', 'screw.ppm']

class Portal(Item): # the portal needs to know of the room it is in and that will be its data
    def __init__(self):
        super().__init__()
        self.data = None # holds the room object that the portal is in
        self.next = None # pointer to the other portal object
    def set_image_portal(self):
        self.image = 'portal.ppm'
    def set_image_flashing(self):
        self.image = 'portal-flashing.ppm'

class Rover:
    '''
    To create a rover object which has the current position of the rover,
    Can not spawn on an item
    '''
    def __init__(self):
        self.x= None
        self.y= None
        self.image = 'rover.ppm'

    def spawn_rover(self):
        x = randint(0,14)
        y = randint(0,14)
        self.setX(x)
        self.setY(y)
#getters
    def getX(self):
        return self.x

    def getY(self):
        return self.y
#setters
    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value


class Node:
    def __init__(self, data=None, next=None):
        self.data = data # save the name with out the .ppm
        self.next = next
class Inventory:
    '''Represented with a List ADT implemented with a linked list '''
    def __init__(self, head= None):
        self._head = head
        self._size = 0
        self._current = None


    def __len__(self):
        '''Overwrites then len() function '''
        return self._size

    def __str__(self):
        '''return string representation of the inventory '''
        result = ''
        node = self._head
        if node != None:
            result+= node.data
            node = node.next
            while node != None:
                result += ', ' + node.data
                node = node.next
        return result

""" Launch the game. """
g = Game()
g.start_game() # This does not return until the game is over
