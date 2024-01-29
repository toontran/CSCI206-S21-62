""" Game to play 'Lost Rovers'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
Put the three ADTs in their own files.
"""
from itertools import product
from gameboard import *
from random import *
from Queue import *
from LinkedList import *
from Stack import *
from HelperClasses import *

class Game:
        SIZE = 15 # rooms are 15x15
        
        def __init__(self):
                # Constants
                self.PARTS = ['bagel', 'cake', 'gear', 'lettuce', 'screw']
                self.COMPONENTS = ['cabin', 'cabinbroken', 'engine', 'enginebroken',
                                          'exhaust', 'exhaustbroken']
                self.ANTIGRAVITY_FUEL_SPAWN_RATE = 0.5 # Only two num after decimal point
                
                # put other instance variables here
                self.gui = GameBoard("Lost Rover", self, Game.SIZE)

                # Initialize inventory
                self.inventory = Linked_List()
                
                # To show the way back
                self._is_showing_the_way_back = False
                self.portals_gone_through_locations = Stack()
                
                # Locations of Broken Components 
                self._broken_components_locations = []

                # Initialize objects name and location on map 
                # (including parts, components, portals and the rover itself)
                self._home_room = Room(Game.SIZE)
                self.room = self._home_room
                self._randomize_initial_room()
                self._room_level = 1 # Room level 1 is the place we call Home
                
                # Generate Tasks based on Broken Components locations
                self._tasks = Stack()
                self._generate_tasks()
                
                # Antigravity matter
                self._num_antigravity_matter = 0
                
                # Record number of steps took
                self._num_steps = 0
                
                # Winning condition
                self._has_won = False
                        
        def _2D_to_1D_coord(self, x, y):
                return Game.SIZE * y + x                

        def _randomize_initial_room(self):
                ''' Randomizes objects' quantity and location 
                    Changes self.inventory, self.object_names and self.object_locations
                    
                    Method: Using Cartesian product to create a list of all possible 
                            locations. Then pop location once it's occupied. 
                '''
                # List from 0 -> Game.SIZE
                temp = [i for i in range(Game.SIZE)]
                all_possible_locations = list(product(temp, repeat=2))
                
                # Take 9 middle positions, shuffle them up
                middle_positions = []
                mid = Game.SIZE // 2
                middle_positions.append(self._2D_to_1D_coord(mid, mid))
                middle_positions.append(self._2D_to_1D_coord(mid, mid-1))
                middle_positions.append(self._2D_to_1D_coord(mid-1, mid))
                middle_positions.append(self._2D_to_1D_coord(mid-1, mid-1))
                middle_positions.append(self._2D_to_1D_coord(mid+1, mid))
                middle_positions.append(self._2D_to_1D_coord(mid, mid+1))
                middle_positions.append(self._2D_to_1D_coord(mid+1, mid-1))
                middle_positions.append(self._2D_to_1D_coord(mid+1, mid+1))
                middle_positions.append(self._2D_to_1D_coord(mid-1, mid+1))
                shuffle(middle_positions)
                
                # Components with middle positions
                num_of_components = randint(7, 9)
                idxes = []
                
                for i in range(6):
                        idx = middle_positions[i]
                        idxes.append(idx)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        component = Component(self.COMPONENTS[i], all_possible_locations[idx])
                        self.room.set_location(component, point)
                        
                        # I'm sorry for the convoluted sh*ts I wrote
                        # Now I'm regretting it too :(
                        # If object is broken, add to self._broken_components_locations
                        if component.is_broken == True:
                            self._broken_components_locations.append(point)
                        
                        
                for i in range(6, num_of_components):
                        idx = middle_positions[i]
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        component = Component(self.COMPONENTS[randint(0,5)], all_possible_locations[idx])
                        self.room.set_location(component, point)
                        
                        if component.is_broken == True:
                            self._broken_components_locations.append(point)
                        
                for idx in idxes:
                        all_possible_locations.pop(idx)
                                                        
                # The Rover
                idx = randint(0, len(all_possible_locations)-1)
                x = all_possible_locations[idx][0]
                y = all_possible_locations[idx][1]
                point = Point(x, y)
                
                self.rover = Rover(all_possible_locations[idx])
                self.room.set_location(self.rover, point)
                all_possible_locations.pop(idx)

                # Portals 
                # num_portals = randint(1,3) # Version 1: Rooms expand linearly
                num_portals = randint(3,5)
                for i in range(num_portals):
                        idx = randint(0, len(all_possible_locations)-1)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        
                        portal = Portal(all_possible_locations[idx])
                        self.room.set_location(portal, point) # Assign portal to the room
                        self.room.portals.append(point)       # Save location of portal for later use
                        all_possible_locations.pop(idx)

                # Parts 
                num_parts = randint(4, 10)
                shuffle(self.PARTS)
                for i in range(num_parts):
                        if i >= 5:
                                i = randint(0, 4)
                                
                        idx = randint(0, len(all_possible_locations)-1)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        
                        part = Part(self.PARTS[i], all_possible_locations[idx])
                        self.room.set_location(part, point)
                        all_possible_locations.pop(idx)
                        
        def _generate_tasks(self):
                ''' Add tasks into self._tasks
                    Based on broken components location '''
                for location in self._broken_components_locations:
                        component = self.room.access_map(location)
                        task = Task(component)
                        self._tasks.append(task)
                        
        def _create_new_room(self, portal_current):
                ''' Creates a new room
                Randomizes Parts location and number 
                Randomizes Portal location and number
                Entangle portals current room to destination room'''
                
                room = Room(Game.SIZE, room_level=self.room.room_level+1)
                all_possible_locations = room.get_possible_locations()
                
                # Parts
                num_parts = randint(4, 10)
                shuffle(self.PARTS)
                for i in range(num_parts):
                        if i >= 5:
                                i = randint(0, 4)
                                
                        idx = randint(0, len(all_possible_locations)-1)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        part = Part(self.PARTS[i], all_possible_locations[idx])
                        room.set_location(part, point)
                        all_possible_locations.pop(idx)
                        
                # Portals
                num_portals = randint(3,5)
                for i in range(num_portals):
                        idx = randint(0, len(all_possible_locations)-1)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        
                        portal = Portal(all_possible_locations[idx])
                        room.set_location(portal, point) # Assign portal to the room
                        room.portals.append(point)       # Save location of portal for later use
                        all_possible_locations.pop(idx)
                        
                # Entangle portals
                '''
                # Version 1: Rooms expand linearly
                for i in range(len(self.room.portals)):
                        portal_current = self.room.access_map(self.room.portals[i])
                        portal_destination = room.access_map(room.portals[i])
                        
                        portal_current.target = portal_destination
                        portal_current.targetRoom = room
                        portal_destination.target = portal_current
                        portal_destination.targetRoom = self.room
                '''
                portal_destination = room.access_map(room.portals[0])
                
                portal_current.target = portal_destination
                portal_current.target = portal_destination
                portal_current.targetRoom = room
                portal_destination.target = portal_current
                portal_destination.targetRoom = self.room
                
                # Antigravity matter spawning
                space = [True if x <= self.ANTIGRAVITY_FUEL_SPAWN_RATE*100 else False for x in range(100)]
                is_spawning = choice(space)
                if is_spawning:
                        idx = randint(0, len(all_possible_locations)-1)
                        x = all_possible_locations[idx][0]
                        y = all_possible_locations[idx][1]
                        point = Point(x, y)
                        
                        ag_matter = Antigravity_Matter(all_possible_locations[idx])
                        room.set_location(ag_matter, point) 
                        all_possible_locations.pop(idx)

        def _warp(self, portal):
                ''' Changes room
                If target room is None then create new room '''
                
                if portal.target == None:
                        self._create_new_room(portal)
                        # Update portal since variable portal here's just a copy of the real thing
                        portal = self.room.access_map(self.rover.location) # Update since portal 
                else:
                        if self._is_showing_the_way_back:   
                            self._is_showing_the_way_back = False
                                
                        if portal.targetRoom.room_level < self.room.room_level:
                                self.portals_gone_through_locations.pop()  
                
                
                if portal.targetRoom.room_level > self.room.room_level:
                        self.portals_gone_through_locations.append(portal.target.location) 
                
                self.room.release_reserved()
                self.room = portal.targetRoom
                
                self.rover.location.x = portal.target.location.x
                self.rover.location.y = portal.target.location.y
                
                self.room.set_reserved(self.rover.location, portal.target)

        def start_game(self):
                self.gui.run()

        def get_rover_image(self):
                """ Called by GUI when screen updates.
                        Returns image name (as a string) of the rover.
                (Likely 'rover.ppm') """
                return 'rover.ppm'

        def get_rover_location(self):
                """ Called by GUI when screen updates.
                        Returns location (as a Point). """
                # Your code goes here, this code is just an example
                return self.rover.location

        def get_image(self, point):
                """ Called by GUI when screen updates.
                        Returns image name (as a string) or None for the
                part, ship component, or portal at the given
                coordinates. ('engine.ppm' or 'cake.ppm' or
                'portal.ppm', etc) """
                obj = self.room.map[point.y][point.x]
                if self._is_showing_the_way_back == True and self.room.room_level != 1:
                        last_portal_location = self.portals_gone_through_locations.peak()
                        if point.x == last_portal_location.x and \
                           point.y == last_portal_location.y:
                                return 'portal-flashing.ppm'
                return obj        
                        
                
        def _handle_events(self):
                ''' Rover can overlap another object, so object is saved using
                    self.set_reserved(), and released with self.release_reserved()
                    
                    Also warp the rover if the object is a rover '''
                self._num_steps += 1
                obj = self.room.access_map(self.rover.location)
                
                if obj == None:
                        pass
                elif obj.name == 'portal':
                        self._warp(obj)        # Warp the rover to the other portal
                elif obj.name == 'worm-hole':              
                        self.room = self._home_room
                        self.rover.location.x = self.room.portals[0].x
                        self.rover.location.y = self.room.portals[0].y
                        
                        destination_portal = self.room.access_map(self.rover.location)
                        self.room.set_reserved(self.rover.location, destination_portal)
                        self.portals_gone_through_locations = Stack()                        
                elif obj != None:               # If there's an object, put into reserved
                        self.room.set_reserved(self.rover.location, obj)
                                                
                self.room.set_location(self.rover, self.rover.location)
                
        def go_up(self):
                """ Called by GUI when button clicked.
                        If legal, moves rover. If the robot lands
                        on a portal, it will teleport. """
                self.room.set_location(None, self.rover.location)
                self.room.release_reserved() # Release reserved object upon moving
                if self.rover.location.y == 0:
                        return
                self.rover.location._move(0, -1)
                
                self._handle_events()
                                        
        def go_down(self):
                """ Called by GUI when button clicked.
                        If legal, moves rover. If the robot lands
                        on a portal, it will teleport. """
                self.room.set_location(None, self.rover.location)
                self.room.release_reserved() # Release reserved object upon moving
                if self.rover.location.y == Game.SIZE-1:
                        return
                self.rover.location._move(0, 1)
                
                self._handle_events()

        def go_left(self):
                """ Called by GUI when button clicked.
                        If legal, moves rover. If the robot lands
                        on a portal, it will teleport. """
                self.room.set_location(None, self.rover.location)
                self.room.release_reserved() # Release reserved object upon moving
                if self.rover.location.x == 0:
                        return
                self.rover.location._move(-1, 0)
                
                self._handle_events()

        def go_right(self):
                """ Called by GUI when button clicked.
                        If legal, moves rover. If the robot lands
                        on a portal, it will teleport. """
                self.room.set_location(None, self.rover.location)
                self.room.release_reserved() # Release reserved object upon moving
                if self.rover.location.x == Game.SIZE-1:
                        return
                self.rover.location._move(1, 0)
                
                self._handle_events()
                        
        def show_way_back(self):
                """ Called by GUI when button clicked.
                        Flash the portal leading towards home. """
                if self.room.room_level != 1:
                    self._is_showing_the_way_back = True

        def get_inventory(self):
                """ Called by GUI when inventory updates.
                        Returns entire inventory (as a string).
                3 cake
                2 screws
                1 rug
          """
                result = ''
                d = {}
                node = self.inventory.get_head()
                
                for i in range(len(self.inventory)):
                        try:
                                d[node.item] += 1
                        except:
                                d[node.item] = 1
                        node = node.next
                
                for key in d:
                        result += '{} {}\n'.format(d[key], key)
                        
                if self._num_antigravity_matter > 0:
                        result += 'antigravity matter {}'.format(self._num_antigravity_matter)
                        
                return result

        def pick_up(self):
                """ Called by GUI when button clicked.
                If rover is standing on a part (not a portal
                or ship component), pick it up and add it
                to the inventory. """
                if self.room.reserved == []:
                        return
                
                obj = self.room.reserved[1] # Object stepped on
                
                if obj == None or obj.name == 'portal' or obj.name in self.COMPONENTS:
                        return
                elif obj.name == 'antigravity-matter':
                        self._num_antigravity_matter += 1
                        self.room.reserved = []
                else:
                        self.inventory.append(obj.name)
                        self.room.reserved = []
               
        def get_current_task(self):
                """ Called by GUI when task updates.
                        Returns top task (as a string).
                'Fix the engine using 2 cake, 3 rugs' or
                'You win!'
                """
                # Default message
                if self._num_steps < 10:
                        message = 'Game Started! To play the game:\n'
                        message +=' - Just move around to see if the button works at first!\n'
                        message +=' - Fix all {} Ship Components to win! Easy!\n'\
                                                                .format(len(self._tasks))
                        message +='Tip: Find Antigravity Matter can help you teleport back'
                        return message    
                elif len(self._tasks) != 0:
                        return str(self._tasks.peak())
                else:
                        return 'You win Bruh'
                
        def perform_task(self):
                """ Called by the GUI when button clicked.
                        If necessary parts are in inventory, and rover
                        is on the relevant broken ship piece, then fixes
                        ship piece and removes parts from inventory. If
                        we run out of tasks, we win. """
                current_task = self._tasks.peak()
                # Check if necessary parts are in inventory
                for item_name in current_task.needed_items:
                        if not self.inventory.has_item(item_name):
                                return
                                
                # Change name of item to fixed
                print(self.room.reserved[1].name)
                print(current_task.broken_component.name)
                
                if self.room.reserved == []:
                        return
                elif self.room.reserved[1].name == current_task.broken_component.name:
                        self.room.reserved[1].fix()
                else:
                        return
                
                # If function continues, all items needed is in inventory
                # Remove from inventory those items
                for item_name in current_task.needed_items:
                        self.inventory.delete(item_name)
                          
                self._tasks.pop()
                print( 'Success, fixed {}'.format(self.room.reserved[1].name))
                        

        # Put other methods here as needed.
        def open_wormhole(self):
                """ Called by the GUI when button clicked.
                        If Antigravity Matter is in inventory, and space 
                        around rover has an unoccupied slot, then 
                        create a wormhole. """     
                if self._num_antigravity_matter == 0:
                        return
                        
                x = self.rover.location.x
                y = self.rover.location.y
                locations_around = [(x+1, y), (x, y+1), (x+1,y+1), 
                                (x-1, y-1), (x-1, y), (x, y-1)]
                
                for location in locations_around:
                        if self.room.access_map( Point(location[0], location[1]) ) == None:
                               worm_hole = Worm_Hole(location)
                               self.room.set_location( worm_hole, Point(location[0], location[1]) )
                               self._num_antigravity_matter -= 1
                               return
      
      
""" Launch the game. """
g = Game()
g.start_game() # This does not return until the game is over
