"""
Queue Simulation lab: CSCI 204
Original design: Prof Brian King
Port to Python: Prof Lea Wittie
Threading & Debugging: Karl Cronburg
"""

from graphics import *
from random import *
import threading
import time
import math
from myqueue import Queue

# number of servers to simulate
NUM_SERVERS = 75

# initial delay between submitting requests to the server pool
REQUEST_DELAY_MS = 50

# Maximum delay to allow
MAX_REQUEST_DELAY_MS = 50

# Capacity of the queue
QUEUE_SIZE = 25

# Debugging flag
DEBUG = False
#DEBUG = True

class ResourceSim(threading.Thread):
        """ A simple resource manager with a neat GUI to show the current
        load of each server queue. """

        def __init__(self, numServers, gui):
                """ Setup the window, scales, and graph for the GUI. """
                """ Setup the server list. """

                # Save a reference to the gui and guiQueue for future use by this thread
                self.gui = gui

                if DEBUG: print("Creating servers")
                # Create the servers
                self.lastServer = 0 # last server to be selected
                self.numServers = numServers
                self.servers = []
                for i in range(self.numServers):
                        self.servers.append(Server(i, self.gui.guiQueue))
                threading.Thread.__init__(self) # Initialize the thread

        def enqueue(self, cmd):
                """ Enqueues the given command into the guiQueue for execution by the GUI """
                self.gui.guiQueue.enqueue(cmd) #put(cmd)

        def run(self):
                """ Starts all of the server threads, then begins the request creation (infinite) loop """
                while True:
                        self.add_job(int(random()*10000))
                        time.sleep(self.gui.getRequestDelay()*0.001)
                        self.updateLoadOutput()

        def select_next_server(self):
                """ Determine which server to select when the next request comes in.
                Returns the index of the server to select. """

                """ Naive scheduling algorithm: put it all on server 0. """
                #return self.lastServer


                """ Round Robin Scheduler:
                Comment out the code provided above (do not delete it!)
                Finish this method by first implementing a round-robin scheduling
                scheme instead of the code shown here. You will need the following
                instance fields:

                self.lastServer # The last server selected
                NUM_SERVERS # The overall number of servers

                Put your code for round robin scheduling under this comment. """
                """if self.lastServer >= self.numServers-1:
                        self.lastServer = 0
                else:
                        self.lastServer += 1
                return self.lastServer"""
                        

                """ Randomized Load-Balancing Scheduler:
                Comment out your code for round robin (do not delete it!)
                Finish this method by implementing a randomized load-balanced scheduling
                scheme instead of the round robin scheduler. You will need the following
                functions and instance fields:

                self.gui.getSampleSize() # Gets sample size from the GUI
                self.servers[i].get_current_load() # Gets load of the ith server
                NUM_SERVERS # The overall number of servers

                Put your code for random scheduling under this comment. """
                sample_size = self.gui.getSampleSize()
                least_server = self.lastServer
                least_load = self.servers[ self.lastServer ].get_current_load()
                for i in sample( range(self.numServers), sample_size ):
                        load = self.servers[ i ].get_current_load()
                        if load < least_load:
                                least_load = load
                                least_server = i
                                
                self.lastServer = least_server
                return self.lastServer


        def start_server(self, i):
                """ Start the thread for the ith server. """
                self.servers[i].start()

        def start_all_servers(self):
                """ Start ALL of the server simulation threads. """
                for i in range(NUM_SERVERS):
                        self.start_server(i)

        def add_job(self, length):
                """ Add a new job to one of the servers. The server selected
		    is determined by the result of scheduleNextServer. Length is
		    the length of the job. """
                s = self.select_next_server()
                # if DEBUG: print("sim adding job of length %d to server %d" % (length,s))
                self.servers[s].add_job(length)
                # if DEBUG: print("Job ADDED!")

        def get_load_average(self):
                """ Compute the average load over all of the servers and return it. """
                totalLoad = 0.0
                for s in self.servers:
                        totalLoad = totalLoad + s.get_current_load()
                avgLoad = totalLoad/NUM_SERVERS
                return avgLoad

        def get_load_variance(self):
                """ Compute the load variance among all of the servers.
		    Variance is the square root of the sum of the squared means.
		    sqrt(sum of (mean squared)) """
                mean = self.get_load_average()
                meansSquared = 0.0
                for s in self.servers:
                        meansSquared = meansSquared + (s.get_current_load()-mean)**2.0
                variance = math.sqrt(meansSquared)
                return variance

        def updateLoadOutput(self):
                """ Update the current load output and current variance on the GUI. """
                string = "Total Load: %.2f    Variance: %.4f" % (self.get_load_average()*100.0,self.get_load_variance())
                self.enqueue('self.setGraphLabel("%s")'%(string))

class Server(threading.Thread):
        """ class to simulate a server. Since it is extended from Thread,
        it amounts to nothing more than overloading the Thread class run method. When
        start() is invoked on this server, the server thread is executed. """

        def __init__(self, idNum, guiQueue):
                """ Overload the Thread's init to setup our Server. """
                self.idNum = idNum
                self.requestQueue = Queue(QUEUE_SIZE)
                self.guiQueue = guiQueue
                threading.Thread.__init__(self)

        def enqueue(self, cmd):
                """ Enqueues the given command into the guiQueue for execution by the GUI """
                self.guiQueue.enqueue(cmd) #put(cmd)

        def run(self):
                """ Repeatedly run the server. It can do one of two things:
                    If the request Q is empty (thread is idle), sleep
                    Else, We have a request! Get the integer from the request, which
                    represents on CPU intensive the request is. Simulate being
                    busy by putting the thread to sleep that amount of time. When
                    the request is finish, update the bar for this server. """
                while True:
                        if self.requestQueue.is_empty(): #empty()
                                time.sleep(0.01)
                        else:
                                time.sleep(self.requestQueue.dequeue()*0.001) # get()
                                self.enqueue('self.adjustBarHeight(%d, %.8f)' % (self.idNum,self.get_current_load()))

        def add_job(self, length):
                """ Add a new job to this server's queue. """
                # if DEBUG: print("adding job to " + str(self.idNum))
                flag = self.requestQueue.enqueue(length) #put()
                if flag == -1:
                        print('Server', self.idNum, 'too full and failed to enqueue.')
                self.enqueue('self.adjustBarHeight(%d, %.8f)' % (self.idNum,self.get_current_load()))

        def get_current_load(self):
                return len(self.requestQueue) / QUEUE_SIZE #qsize()

def quitFncn(pt):
        """ Function to be called when Quit button is clicked"""
        exit(0)

class GUI:
        """ The GUI. """

        def mouseClick(self,p):
                """ This function is called when the mouse is clicked, and checks if the location
                clicked corresponds to anything which the GUI wishes to know about """
                # NOT WORKING
                # if p.x > self.quit.x and p.y > self.quit.y and p.x < self.quit.x2 and p.y < self.quit.y2:
                #    exit(0)

        def __init__(self, title):
                #Setup queue for handling GUI change requests by servers:
                self.guiQueue = Queue()

                # Setup window
                width = 500
                height = 400
                title = "Resource Manager Simulation"
                if DEBUG: print("Creating Window")
                self.window = GraphWin(title, width, height)

                # When mouse is clicked, this function is called.
                self.window._mouseCallback = self.mouseClick

                # Setup scales at the top of the window
                self.size = Text(Point(10,10), "Sample size [1]:")
                self.size.draw(self.window)

                self.sizeScale = Scale(Point(300,25), 1, 15, 2, 1, self.updateSize)
                self.sizeScale.draw(self.window)

                self.delay = Text(Point(10,45), "Request delay (ms) [1]:")
                self.delay.draw(self.window)

                #print(self.updateDelay)
                self.delayScale = Scale(Point(300,70),0, 200, 50, 50, self.updateDelay)
                self.delayScale.draw(self.window)


                # Setup graph and label in the middle
                self.plotWidth = int(width * 3/4)
                self.plotTop = 100
                plotTop = self.plotTop
                self.plotBottom = height-40
                plotArea = Rectangle(Point(width/2 - self.plotWidth/2, plotTop),
			       Point(width/2 + self.plotWidth/2, self.plotBottom))
                plotArea.draw(self.window)
                self.bars = []
                heights = []
                left = width/2 - self.plotWidth/2
                for i in range(0,NUM_SERVERS):
                        #self.bars.append(Rectangle(Point(left + i*(self.plotWidth/NUM_SERVERS), plotTop),
                        #	                  Point(left + (i+1)*(self.plotWidth/NUM_SERVERS), self.plotBottom)))
                        top = Point(left + i*(self.plotWidth/NUM_SERVERS), self.plotBottom)
                        bottom = Point(left + (i+1)*(self.plotWidth/NUM_SERVERS), self.plotBottom)
                        self.bars.append(Rectangle(top,bottom))
                        self.bars[i].setFill("green")
                        self.bars[i].draw(self.window)
                        heights.append(0)
                self.plotLabel = Text(Point(width/4., 0.93*height), "words")
                self.plotLabel.draw(self.window)
                # config label to center

                # setup quit button NOT WORKING
                #self.quit = Button(Point(450, 40), quitFncn, "Quit")
                #self.quit.draw(self.window)

        def run(self):
                """ Receives requests to execute code which changes the GUI from threads, and executes it. """
                if DEBUG: print("running gui")
                # Keep checking the guiQueue *forever*, executing the commands
                # which are passed to it. Queue.get() blocks until the queue is non-empty.
                """while True:
                        # self.window.getMouse()
                        try:
                                while True:
                                        cmd = self.guiQueue.peek() # return item or raise Empty
                                        if DEBUG: print("Executing: " + cmd)
                                        exec(cmd)
                                        # if DEBUG: print("Cmd completed.")
                        except Empty: pass
                        update()"""
                while True:
                        cmd = self.guiQueue.dequeue()
                        if cmd == None:
                                update()
                        else:
                                exec(cmd)

        def updateSize(self, val):
                self.size.setText("Sample size [" + str(val) + "]:")

        def updateDelay(self, val):
                self.delay.setText("Request delay (ms) [" + str(val) + "]:")

        def setGraphLabel(self, string):
                # if DEBUG: print("setting graph label: " + string)
                self.plotLabel.setText(string)

        def adjustBarHeight(self, idNum, load):
                topLeft = self.bars[idNum].getP1()
                botRight = self.bars[idNum].getP2()
                # pixels & the maximum possible load
                self.bars[idNum].adjust(Point(topLeft.x, self.plotBottom + load*(-self.plotBottom+self.plotTop)), botRight)
                self.bars[idNum].undraw()
                #self.bars[idNum].draw(self.window)
                #self.bars[idNum]._reconfig("p1", Point(topLeft.x, self.plotBottom + load))
                self.bars[idNum].draw(self.window)

        def getRequestDelay(self):
                return self.delayScale.getValue()

        def getSampleSize(self):
                return self.sizeScale.getValue()

def main():

	# Setup GUI
	title = "Resource Manager Simulation"
	gui = GUI(title)

	# Start-up servers
	r = ResourceSim(NUM_SERVERS,gui)
	if DEBUG: print("Starting all servers!")
	r.start_all_servers() # Need to start servers from *main* thread
	r.start() # starts all of the server & request threads

	# Let the GUI start handling requests in its queue:
	gui.run() # runs the GUI in the *main* thread (this one)

try:
        main()
except GraphicsError:
        pass
