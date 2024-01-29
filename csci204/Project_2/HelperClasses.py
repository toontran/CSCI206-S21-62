'''
Helper classes for Game
'''
from random import *
from graphics import *

PARTS = ['bagel', 'cake', 'gear', 'lettuce', 'screw']

# Put other classes here or in other files as needed.
class Room:

        def __init__(self, room_size, room_level=1):
                self.room_size = room_size
                self.map = [[None for x in range(room_size)] for x in range(room_size)]
                self.reserved = [] # When the rover overlap with an object, store the 
                                   # location and the object itself here
                self.portals = [] # List of _Portal locations in self
                self.room_level = room_level
        
        def get_possible_locations(self):
                ''' Possible location '''
                possible_locations = []
                for y in range(self.room_size):
                        for x in range(self.room_size):
                                if self.map[y][x] == None:
                                        possible_locations.append([x, y])
                return possible_locations
        
        def access_map(self, point):
                return self.map[point.y][point.x]
                
        def remove(self, point):
                self.map[point.y][point.x] = None
        
        def set_location(self, obj, location):
                x = location.x
                y = location.y
                self.map[y][x] = obj
                
        def set_reserved(self, location, obj):
                self.reserved = [location, obj]
                
        def release_reserved(self):
                if self.reserved != []:
                        location = self.reserved[0]
                        obj = self.reserved[1]
                        self.set_location(obj, location)
                        self.reserved = []
                else:
                        return None

class Object:
        ''' Base class for all objects '''

        def __init__(self, name, location):
                self.name = name
                self.location = Point(location[0], location[1])

        def __str__(self):
                return '{}.ppm'.format(self.name, self.location.x, self.location.y)


class Rover(Object):
        ''' _Rover class '''
        def __init__(self, location):
                self.name = 'rover'
                super().__init__(self.name, location)


class Portal(Object):
        ''' _Portal class '''
        def __init__(self, location):
                self.name = 'portal'
                super().__init__(self.name, location)
                self.target = None
                self.target_room = None
                
        def entangle(self, portal_2):
                self.target = portal_2
                portal_2.target = self


class Component(Object):
        ''' Ship _Component class '''
        def __init__(self, name, location):
                super().__init__(name, location)
                if self.name[-6:] == 'broken':
                        self.is_broken = True
                else:
                        self.is_broken = False
       
        def fix(self):
                assert self.is_broken == True, 'Object is not broken!'
                
                self.name = self.name[:-6]
                self.is_broken = False


class Part(Object):
        ''' _Part class '''
        def __init__(self, name, location):
                super().__init__(name, location)
                
                
class Antigravity_Matter(Object):
       
        def __init__(self, location):
                self.name = 'antigravity-matter'
                super().__init__(self.name, location)
                
                
class Worm_Hole(Object):
        
        def __init__(self, location):
                self.name = 'worm-hole'
                super().__init__(self.name, location)
                
class Task:
        
        def __init__(self, broken_component):
                assert isinstance(broken_component, Component), 'Must be a Broken Component'
                assert broken_component.is_broken == True, 'Must be a Broken Component'
                self.broken_component = broken_component
                self.needed_items = []
                self.randomize_needed_items()
                
        def _capitalize(self, s):
                l = s.split()
                for i in range(len(l)):
                        l[i] = l[i][0].upper() + l[i][1:]
                
                return ' '.join(l)
                
        def randomize_needed_items(self):
                num_tasks = randint(2,4)
        
                self.needed_items = [ PARTS[randint(0,4)] for x in range(num_tasks) ]
                
        def __str__(self):
                ''' E.g.
                Broken Cabin! To fix the cabin, you'll need:
                - 2 Lettuces
                - 1 Screw
                - 2 Gears
                - 2 Cakes
                '''

                item_name = self.broken_component.name[:-6]
                
                result = 'Broken {}! To fix the {}, you\'ll need:\n'\
                        .format( self._capitalize(item_name), item_name )
                
                d = {}
                for item in self.needed_items:
                        if item not in d:
                                d[item] = 1
                        else:
                                d[item] += 1
                
                for key in d:
                        s = ''
                        if d[key] > 1:
                                s = 's'
                        result += '- {} {}\n'.format( d[key], self._capitalize(key)+s )
                        
                return result
                
                
if __name__ == '__main__':
        broken_component = Component('cabinbroken', [0,0])
        task = Task(broken_component)
        print(task.needed_items)
        print(task)
        
        
        
        
        
        
        
        
        
                


