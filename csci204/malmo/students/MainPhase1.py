###---------
# Written by Professor Chris Dancy @ Bucknell
#  uses some code written by Son Pham ('18 Bucknell Universtiy) &
#  some code from various malmo tutorials
# For CSCI 204
###---------

import malmoenv
import os, random, sys, time, json, random, errno, traceback, timeit
from MalmoAgent import *
#from PIL import Image

class MalmoMissionMain:
	'''
	Class to run Agent on Malmo Server
	Requires Agent, Item, & Block classes
		(see project document for minimum methods & attributes)
	'''

	MISSION_LENGTH = 500
	MISSION_WIDTH = 100
	HEIGHT = 225

	#These are the inventory that we'll explicitly process
	INVENTORY_ITEMS = ["red_flower white_tulip", "coal", "planks spruce", "planks birch", "planks dark_oak", "rabbit", "carrot", "potato", "brown_mushroom"]
	INVENTORY_POSITIONS = [[21, 24], [31, 33], [37, 30], [21, 13], [25,40], [35, 31], [33, 39], [23, 26], [29, 32]]

	def __init__(self, m_agent, mission_file_name=None, update_delay=0.025,
				server_add="127.0.0.1", port=9000, episode=0, exp_id="p1p1"):
		'''
		Malmo mission constructor
			Arguments:
			- m_agent : an object of the MAgent class
			- mission_file_name : a mission xml file, if we want to use a function, set to None
			- update_delay : the rate at which we'll check for new observation while the agent is running
			- server_add: address of minecraft server (most likely 127.0.0.1 on a local machine)
			- port : the port to which our agent will connect
			- episode : Starting episode for agent (should likely just be 0 for this project)
			- exp_id : string representing the id of this "experiment" (simulation)

		'''
		#Create the initial agent environment
		self._env = malmoenv.make()

		#Set our malmo agent
		self._m_agent = m_agent

		#We don't need multiagent, so we set these values so that we have a single agent mission
		server2_add = server_add
		port2 = None

		current_yaw_delta = 0

		correctActionStr = "uid:0, command:\"turn \" + str(current_yaw_delta)\n" + \
							"uid:1, command:\"move \" + str(1.0 - abs(current_yaw_delta))\n" + \
							"uid:2, command:\"turn 0\"\n" + \
							"uid:3, command:\"move 0\"\n" + \
							"uid:4, command:\"craft cooked_rabbit\"\n" + \
							"uid:5, command:\"move 1\"\n" + \
							"uid:6, command:\"swapInventoryItems 0 \" + str(curr_slot)"
		print("If everything is working and you are using the original actions.txt file, you should see:\n" + correctActionStr)
		print("\nThe actions you got were...\n")
		for key in self._m_agent.get_actions().keys():
			print("uid:{}, command:{}".format(key,self._m_agent.get_actions()[key]))

		#Get our mission either using explicit file, or using function
		# If we had an issue reading file, return without continuing
		if( self.get_mission(mission_file_name) == -1 ):
			return

		self._env.init(self._mission, port, server=server_add, server2=server2_add,
						port2=port2, role=0, exp_uid=exp_id, episode=episode, resync=0,
						action_space = malmoenv.ActionSpace(self._m_agent.get_actions()))

		print("Mission Running")

	def draw_square(self, x1, z1, x2, z2, y, block_type):
		'''
		Creates & returns string that represents XML for a square.
			x1:	starting x of square
			z1:	starting z of square
			x2: ending x of square
			z2: ending z of square
			y:	plane on which square should be located
			block_type: type of block used to draw line
		'''
		square_str = "<DrawLine x1=\"" + str(x1) + "\" y1=\"" + str(y) + "\" z1=\"" + str(z1) + "\" \
					 x2=\"" + str(x1) + "\" y2=\"" + str(y) + "\" z2=\"" + str(z2) + "\" \
					 type=\"" + block_type + "\" />"
		square_str += "\n<DrawLine x1=\"" + str(x1) + "\" y1=\"" + str(y) + "\" z1=\"" + str(z1) + "\" \
					 x2=\"" + str(x2) + "\" y2=\"" + str(y) + "\" z2=\"" + str(z1) + "\" \
					 type=\"" + block_type + "\" />"
		square_str += "\n<DrawLine x1=\"" + str(x1) + "\" y1=\"" + str(y) + "\" z1=\"" + str(z2) + "\" \
					 x2=\"" + str(x2) + "\" y2=\"" + str(y) + "\" z2=\"" + str(z2) + "\" \
					 type=\"" + block_type + "\" />"
		square_str += "\n<DrawLine x1=\"" + str(x2) + "\" y1=\"" + str(y) + "\" z1=\"" + str(z1) + "\" \
					 x2=\"" + str(x2) + "\" y2=\"" + str(y) + "\" z2=\"" + str(z2) + "\" \
					 type=\"" + block_type + "\" />"
		return (square_str)

	def draw_cuboid(self, x1, y1, z1, x2, y2, z2, block_type):
		'''
		Creates & returns string that represents XML for a square.
			x1:	starting x of square
			z1:	starting z of square
			x2: ending x of square
			z2: ending z of square
			y:	plane on which square should be located
			block_type: type of block used to draw line
		'''

		cube_str = "<DrawCuboid x1=\"" + str(x1) + "\" y1=\"" + str(y1) + "\" z1=\"" + str(z1) + "\" \
					 x2=\"" + str(x1) + "\" y2=\"" + str(y2) + "\" z2=\"" + str(z2) + "\" \
					 type=\"" + block_type + "\" />"

		return (cube_str)

	def draw_shapes(self):
		'''
		Returns custom xml for shapes that are dependent on class attributes
		'''
		shape_xml = self.draw_square(-1, -1, self.MISSION_LENGTH, self.MISSION_WIDTH, self.HEIGHT,  "stone")
		shape_xml += "\n" + self.draw_square(-1, -1, self.MISSION_LENGTH, self.MISSION_WIDTH, self.HEIGHT + 1,  "glowstone")
		shape_xml += "\n" + self.draw_square(-1, -1, self.MISSION_LENGTH, self.MISSION_WIDTH, self.HEIGHT + 2,  "glass")
		shape_xml += "\n" + self.draw_cuboid(0,  self.HEIGHT - 2,  0, self.MISSION_LENGTH - 1, self.HEIGHT - 2, self.MISSION_WIDTH - 1,  "cobblestone")
		shape_xml += "\n" + self.draw_cuboid(0,  self.HEIGHT,  0, self.MISSION_LENGTH - 1, self.HEIGHT, self.MISSION_WIDTH - 1,  "grass")
		return (shape_xml)

	def get_mission(self, mission_file_name, summary=""):
		if( mission_file_name is None ):
			self._mission = self._construct_mission(summary)
			#self._mission.drawCuboid(0,  self.HEIGHT + 1, 0, self.MISSION_LENGTH - 1, self.HEIGHT + 15, self.MISSION_WIDTH - 1, "air")
			#self._mission.createDefaultTerrain()
		else:
			print("Attempting to load your mission file - " + mission_file_name)
			#Load mission file
			try:
				m_file = open(mission_file_name, "r")
				self._mission = Path(args.mission).read_text()
			except IOError:
				print("Mission file not found!")
				return( -1 )
			try:
				self._agent_h.startMission(self._mission, self._mission_rs)
			except RuntimeError as e:
				print("Problem starting mission!: " + e)
				return( -1 )

	def run_mission(self):
		obs = self._env.reset()

		curr_info = None

		info = None

		#Move forward should only be one command, so we can just use 1st index
		#Just complete an action to get info
		(obs, rew, done, info) = self._env.step(5)

		print(info)

		#Sleep to give the server time to catch-up
		time.sleep(0.01)

		while (not done):
			#Get turn command string from agent
			t_acts = self._m_agent.get_goal_actions("find_item_turn")
			#Get move command string from agent
			m_acts = self._m_agent.get_goal_actions("find_item_move")
			#if (info == None or len(info) == 0):
			#	continue
			#Convert JSON info into dictionary if info is not empty
			if (len(info) != 0):
				curr_info = json.loads(info)

			if (not (curr_info is None)):
				info_inv = curr_info["inventory"]
				self._m_agent.update_inv(info_inv)

			if (not (curr_info is None) and (u'yawDelta' in curr_info)):
				curr_yaw_delta = curr_info.get(u'yawDelta', 0)
				#Used so that we can dynamically pull yaw delta
				curr_yaw_comm = "current_yaw_delta={}".format(curr_yaw_delta)


				#Should uid to '"turn " + str(current_yaw_delta)', if using default actions.txt
				for act in t_acts:
					try:
						(obs, rew, done, info) = self._env.step(act, [curr_yaw_comm])
						#Sleep to give the server time to catch-up
						time.sleep(0.001)
					except Exception as e:
						exc_type, exc_value, exc_traceback = sys.exc_info()
						traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)
						print("Problem evaluating a command, you likely have an issue w/ get_goal_actions, or the way you store actions")

				#Should be ['"move " + str(1.0 - abs(current_yaw_delta))'], if using default actions.txt
				for act in m_acts:
					try:
						(obs, rew, done, info) = self._env.step(act, [curr_yaw_comm])
						time.sleep(0.001)
					except Exception as e:
						exc_type, exc_value, exc_traceback = sys.exc_info()
						traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)
						print("Problem evaluating a command, you likely have an issue w/ get_goal_actions, or the way you store actions")
			else:
				#Get turn command string from agent
				t_acts = self._m_agent.get_goal_actions("stop_turn")
				#Get move command string from agent
				m_acts = self._m_agent.get_goal_actions("stop_move")

				#Should be ["turn 0"]
				for act in t_acts:
					try:
						(obs, rew, done, info) = self._env.step(act)
						time.sleep(0.001)
					except Exception as e:
						print(e)
						exc_type, exc_value, exc_traceback = sys.exc_info()
						traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)
						print("Problem evaluating a command, you likely have an issue w/ get_goal_actions, or the way you store actions")

				#Should be ["move 0"]
				for act in m_acts:
					try:
						(obs, rew, done, info) = self._env.step(act)
						time.sleep(0.001)
					except Exception as e:
						exc_type, exc_value, exc_traceback = sys.exc_info()
						traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)
						print("Problem evaluating a command, you likely have an issue w/ get_goal_actions, or the way you store actions")

				self.__select_action(curr_info)
		self._m_agent.update_inv(curr_info["inventory"])
		print("Mission Ended")

	def __select_action(self, curr_obs):
		if( self._m_agent.in_inventory("rabbit") ):
			print("We'll cook the rabbit")
			#Ensure we're cooking w/ coal fuel (if we have coal)
			self.__check_fuel_position()
			cook_rabbit_acts = self._m_agent.get_goal_actions("cook_rabbit")
			for act in cook_rabbit_acts:
				try:
					(obs, rew, done, info) = self._env.step(act)
				except Exception as e:
					exc_type, exc_value, exc_traceback = sys.exc_info()
					traceback.print_exception(exc_type, exc_value, exc_traceback,limit=2, file=sys.stdout)
					print("Problem evaluating a command, you likely have an issue w/ get_goal_actions, or the way you store actions")
				# Give time to action to complete
				time.sleep(1)


	def __check_fuel_position(self):
		'''Make sure our coal, if we have any, is in slot 0.'''
		# (We need to do this because the furnace crafting commands - cooking the potato and the rabbit -
		# take the first available item of fuel in the inventory. If this isn't the coal, it could end up burning the wood
		# that we need for making the bowl.)
		slot_nums = self._m_agent.get_inv_slots("coal", None)
		swap_item_acts = self._m_agent.get_goal_actions("swap_item_first")
		try:
			curr_slot_comm = "curr_slot={}".format(slot_nums[0])
			for act in swap_item_acts:
				self._env.step(act, [curr_slot_comm])
		except Exception as e:
			print("Issue finding coal in inventory!")
			print(e)


	def __get_inventory(self, obs):
		'''
		Get inventory using an observation
			obs - dictionary obtained from JSON parsing of  agent_host observation
			Returns: inventory as a list of
		'''

		variant = None
		color = None
		inv_list = []
		# Go through in-game inventory and record items to list
		for i in range (0,39):
			# Any item attributes should have same number (for slot)
			key = "InventorySlot_" + str(i) + "_item"
			s_key = "InventorySlot_" + str(i) + "_size"
			v_key = "InventorySlot_" + str(i) + "_variant"
			c_key = "InventorySlot_" + str(i) + "_color"

			# If our item is in the observation dictionary, get the item
			#  & any other available attributes
			if( key in obs ):
				item = obs[key]
				size = obs[s_key]
				item_list = [item, size]
				if( v_key in obs ):
					item_list.append(obs[v_key])
				if( c_key in obs ):
					item_list.append(obs[c_key])

				# Add item list to inventory list
				inv_list.append(item_list)

		return( inv_list )

	def _construct_item_xml(self, positions):
		drawing = ""
		index = 0
		for p in positions:
			item = self.INVENTORY_ITEMS[index].split()
			drawing += '<DrawItem x="' + str(p[0]) + '" y="230" z="' + str(p[1]) + '" type="' + item[0]
			if( len(item) > 1 ):
				drawing += '" variant="' + item[1]
				if( len(item) > 2 ):
					drawing += '" color="' + item[2]
			drawing += '" />'
			index += 1
		return drawing

	def _construct_subgoal_xml(self, positions):
		goals=""
		for p in positions:
			goals += '<Point x="' + str(p[0]) + '" y="226" z="' + str(p[1]) + '" tolerance="1" description="ingredient" />'
		return goals

	def find_random_positions(self, items):
		'''
		Find random positions for all items
			items - list of items that need positions assigned
			returns: list of positions
		'''
		positions=[]
		for item in items:
			positions.append((random.randint(20,40), random.randint(20,40)))
		return positions


	def _construct_mission(self, summary):
		'''
		Build an XML mission string that uses the RewardForCollectingItem mission handler.
		'''

		return( '''<?xml version="1.0" encoding="UTF-8" ?>
		<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
			<About>
				<Summary>''' + summary + '''</Summary>
			</About>

			<ServerSection>
				<ServerInitialConditions>
					<Time>
						<AllowPassageOfTime>false</AllowPassageOfTime>
					</Time>
				</ServerInitialConditions>
				<ServerHandlers>
					<FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" />
					<!-- DefaultWorldGenerator/> -->
					<DrawingDecorator>
						<DrawCuboid x1="-50" y1="226" z1="-50" x2="50" y2="226" z2="50" type="air" />   <!-- to clear old items-->
						<DrawCuboid x1="-50" y1="224" z1="-50" x2="50" y2="224" z2="50" type="monster_egg" variant="chiseled_brick" />
						<DrawCuboid x1="-3" y1="225" z1="-3" x2="3" y2="225" z2="3" type="dirt" />
						<!-- <DrawCuboid x1="25" y1="227" z1="25" x2="35" y2 s="227" z2="35" type="red_flower" variant="blue_orchid" />  yes, blue orchids are indeed a type of red flower. -->
						''' + self._construct_item_xml(self.INVENTORY_POSITIONS) + '''
						''' + self.draw_shapes() + '''
					</DrawingDecorator>
					<ServerQuitFromTimeUp timeLimitMs="150000"/>
					<ServerQuitWhenAnyAgentFinishes />
				</ServerHandlers>
			</ServerSection>
			<AgentSection mode="Survival">
				<Name>A-a-ron</Name>
				<AgentStart>
					<Placement x="5" y="226.0" z="5"/>
					<Inventory>
					</Inventory>
				</AgentStart>
				<AgentHandlers>
					<RewardForCollectingItem>
						<Item reward="10" type="planks" variant="spruce dark_oak" />
						<Item reward="100" type="cooked_rabbit carrot baked_potato brown_mushroom"/>
						<Item reward="500" type="bowl"/>
						<Item reward="1000" type="rabbit_stew"/>
					</RewardForCollectingItem>
					<RewardForDiscardingItem>
						<Item reward="-2" type="planks"/>
						<Item reward="-6" type="cooked_rabbit carrot baked_potato brown_mushroom"/>
					</RewardForDiscardingItem>
					<ContinuousMovementCommands turnSpeedDegs="480"/>
					<SimpleCraftCommands />
					<InventoryCommands />
					<ObservationFromSubgoalPositionList>''' + self._construct_subgoal_xml(self.INVENTORY_POSITIONS) + '''
					</ObservationFromSubgoalPositionList>
					<ObservationFromFullInventory flat="false" />
					<AgentQuitFromCollectingItem>
						<Item type="cooked_rabbit" description="Supper's Up!!"/>
					</AgentQuitFromCollectingItem>
					<VideoProducer want_depth="false">
						<Width>800</Width>
						<Height>600</Height>
					</VideoProducer>
				</AgentHandlers>
			</AgentSection>

		</Mission>''' )



start = timeit.default_timer()
sys.stdout.flush()
malmo_agent = MalmoAgent([], {},  "actions.txt", "ItemLog.txt")
new_mission = MalmoMissionMain(malmo_agent)
new_mission.run_mission()
