###---------
# Written by Professor Chris Dancy @ Bucknell University
# For CSCI 204 Projects
# Modified by:
# For Project #
###---------
import time


class MalmoAgent:
	'''
	Main Agent class that will be used to control aspects of the Malmo/Minecraft
	agent that you see moving on screen
	'''

	def __init__(self, inv_list=[], goals={}, action_file="actions.txt", item_log="ItemLog.txt"):
		self.__inv_list = inv_list
		self.__goals = goals
		self.__actions = {}
		self.set_actions(action_file)
		self.__item_log = item_log

	def update_inv(self, inv_list):
		'''
		update items from list already in inventory (that match attributes) &
		add any new items to inventory

		Params:
			inv_list - [list] A list of dictionaries, where each dictionary has an items attributes
		'''
		# Delete content of file when inv_list is None (when the game starts)
		if not inv_list: # O(1)
			f = open('ItemLog.txt', 'w') # O(1)
			f.close() # O(1)
			return
		# test + body = 1 + 1 + 1 = O(1)
	
		with open('ItemLog.txt', 'a+') as f: # O(1)
			is_different = False # O(1)    # Update if length of inv_list and self.__inv_list are different

			if len(inv_list) != len(self.__inv_list): # O(1)
				is_different = True # O(1)
			# test + body = 1 + 1 = O(1)

			# Prof. Dancy says: "Be creative!!"
			# so I made two kinds of variant and/or color to those with no such things:
			# "no_variant" and "colorless"! I'm such a creative student!
			for i in range(len(inv_list)):
                                if "variant" not in inv_list[i]:
                                        inv_list[i]['variant'] = 'no_variant'
                                if inv_list[i]['color'] == '':
                                        inv_list[i]['color'] = 'colorless'
                                        print(inv_list[i])
			
			# Find modifications
			modified_item_idx = [] # O(1)	#List of indexes of modified items
			item_updated_attr = [(x['type'], x['quantity'], x['index'], x['variant'], x['color']) for x in inv_list] # O(n)
			item_in_inv_attr = [(x.name, x.size, x.slot_num, x.variant, x.color) for x in self.__inv_list] # O(n)
			for i in range(len(self.__inv_list)): # Loop n times
				for j in range(3): # Loop 3 times
					if item_updated_attr[i][j] != item_in_inv_attr[i][j]: # test O(1)
						modified_item_idx.append(i) # O(n) although mostly O(1): ICS-46 covers details
			# n * 3 *(1+n) = O(n^2)

			# If there's a Modified	item		
			if modified_item_idx: # O(1)
				is_different = True # O(1)
			# test + body = 1+1 = O(1)
			
			if is_different: # O(1)
				# Create list of Items
				items = [] # O(1)
				for obj in inv_list: # O(n)
					items.append(Item(name=obj['type'], slot_num=obj['index'], size=obj['quantity'],
							  variant=obj['variant'], color=obj['color'])) # O(n)
				# n * (1+1+1+1+n) = O(n^2)
					
				# Then update the whole __inv_list
				self.__inv_list = self.__apply_rules(items, modified_item_idx) # O(n^2)

				# Display name, size, color, variant
				content_list = ['({},{},{},size:{}, modified:{}, created:{})'.format(x.name, x.color, x.variant, x.size, x.modified, x.created) for x in self.__inv_list] # O(n)
				content = ', '.join(content_list) # O(n)
				f.write(content + '\n') # O(1)
				print('Current inventory: ', content, '\n') # O(1)
		# Time complexity: O(n^2)
			
	def __apply_rules(self, items, idx: list) -> list:
		'''
		Apply 4 rules
		Input: list of Items; list of index of Modified Items
		Output: list of Items
		'''
		for i in range(len(items)): # O(n)
			if i in idx: # O(n)
				# Rule 1
				if i < len(items)-1 and items[i+1].name == items[i].name and \
				   items[i+1].variant != items[i].variant: # O(1)
					items[i+1].color = items[i].color # O(1)
					items[i+1].update_modified() # O(1)
					idx.append(i+1)
				# Rule 2
				if items[i].name == 'red_flower' and items[i-1].name == 'red_flower' and \
				   items[i].color == 'WHITE' and items[i-1].variant != items[i].variant: # O(1)
					items[i].color = 'BLUE' # O(1)
					items[i].update_modified() # O(1)

				# Rule 3
				if items[i].name == 'red_flower' and items[i].color == 'WHITE': # O(1)
					items[i].color = 'RED' # O(1)
					items[i].update_modified() # O(1)

				# Rule 4
				if items[i].name == 'red_flower' and items[i].color == 'RED': # O(1)
					items[i].color = 'WHITE' # O(1)
					items[i].update_modified() # O(1)
		# n * n * 8 = O(n^2)
		return items

	def get_item(self, index):
		'''
		Get the item at index

		Params:
			index - [int] The index at which the caller wishes to get the item
		Returns:
			[Item] the object at the given index, or -1 if there is no object at that index
		'''
		if index >= len(self.__inv_list) or index < 0:
			return -1
		else:	
			return self.__inv_list[index]

	def get_actions(self):
		'''
		Accessor for action dictionary

		Returns:
			[dictionary] the actions dictionary (should be __actions)
		'''
		return self.__actions

	def get_action(self, uid):
		'''
		Accessor for returning an individual action given an uid

		Params:
			uid - Unique identifier for a given action
		'''
		return self.__actions[uid]

	def get_goal_actions(self, key):
		'''
		Returns the value (list of strings representing actions) w/ corresponding key

		Params:
			key: [string] key that is used to get list of action numbers from goal dictionary
		Return:
			list of numbers (i.e., that are keys to actions in the action_dict data structure)
		'''
		return self.__goals[key]
	
	def add_action(self, goal, action_list):
		'''
		Adds a goal (key) list of actions (value) pair to dictionary
		'''
		self.__goals[goal] = action_list

	def in_inventory(self, item_name):
		'''
		Check if an item is in an inventory using the item's name
		'''
		for item in self.__inv_list:
			if item_name == item.name:
				return True
		return False

	def get_inv_slots(self, item_name, something_else):
		'''
		Check for item's slots based on item_name
		'''
		slot_nums = []
		for item in self.__inv_list:
			if item.name == item_name:
				slot_nums.append(item.slot_num)
		return slot_nums

	def set_actions(self, file_name):
		'''
		Sets the internal actions available to the agent according to the file_name given

		Params:
			file_name: [string] The name of the file that contains the actions
		Returns:
			[int] returns -1 if there was a caught error. Otherwise returns a 1
		'''

		#Read in the file

		#This will keep a unique identifier for each command (needed for Malmo gym API)
		curr_id = 0

		#---Pseudo Algo---#
		# For each line in the actions file:
		#  + Create a temporary list to hold action ids (you'll use this below)
		#  + Split the line into a list of commands
		#  + For each command in the list of commands:
		#   - Create a key-value pair in the __actions dictionary where:
		#    o the key is an incrementing unique ID (curr_id)
		#    o the value is the return value of __str_to_action
		#     - EX: self.__actions[curr_id] = self.__str_to_action(command)
		#   - Add that unique ID (curr_id) to the temporary list you created above
		#   - Increment your unique id (curr_id)
		#  + Add the goal (a string) and set of action uids (the temporary list you created) to your __goals dictionary (with the goal string as the key)
		try:
			with open(file_name, 'r') as action_file:
                                for line in action_file.readlines():
                                        goal_and_commands = line.strip().split(', ') # [goal, command_1, command_2, etc]
                                        action_ids = []				     # To be added into self.__goals
                                        
                                        # Turn each command into an Action object
                                        for i in range(1, len(goal_and_commands)):
                                                self.__actions[curr_id] = self.__str_to_action(goal_and_commands[i])

						# Also append into list of uid(s)
                                                action_ids.append(curr_id)
                                                curr_id += 1

					# Key: goal, Value: list of uid(s)
                                        self.__goals[goal_and_commands[0]] = action_ids
		except Exception as e:
			print('ERROR: Set actions Malmo Agent')
			print(e)
			return -1

		return 1

	def __str_to_action(self, a_string):
		'''
		Converts action in string form to Action object

		Params:
			a_string: an action string (e.g., "move 0")
		Retutrns:
			[Action] returns Action object given the input A-List
		'''
		a_list = a_string.partition(" ")
		#Notice that we expect the Action constructor to take in two parameters!
		return( Action(a_list[0], a_list[2]) )


class Item:
        
        def __init__(self, name='', size=0, slot_num=0, variant='', color='', modified=time.time(), created=time.time()):
                self.name = name
                self.size = size
                self.slot_num = slot_num
                self.variant = variant
                self.color = color
                self.modified = time.asctime(time.localtime(modified))[11:-5] # Only display from hours
                self.created = time.asctime(time.localtime(created))[11:-5]

        def update_modified(self):
                self.modified = time.asctime(time.localtime(time.time()))[11:-5]


class RedFlower(Item):

        pass
                

class Planks(Item):

        pass


class Action:

        def __init__(self, command='', command_value=''):
                self.command = command
                self.command_value = command_value

        def __str__(self):
                return '{} {}'.format(self.command, self.command_value)
