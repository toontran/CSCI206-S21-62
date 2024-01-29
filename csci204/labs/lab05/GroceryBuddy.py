""" A grocery 'app' that uses a List behind the scenes. """
from graphics import *
from ListException import *

class GroceryApp:
    """ The app is a long grocery list of pictures and numbers
        (3 bags of frozen peas). It has a button bar on the left side."""
    def __init__(self, list):
        
        self.length = 9 # max number of items to show
        self.offset = 10      # horizontal offset from left side
        self.vspace = 25      # vertical offset between rows
        self.hspace = 80      # horizonal offset to space column 2
        self.ewidth = 10      # width of entry boxes
        self.eoffset = 5      # extra vertical offset for entry boxes which appear high
        self.rheight = 100    # height of image rectangles
        self.rwidth = 100     # width of image rectangles
        self.nwidth = 20      # width of number column
        self.noffset = 10     # offset between rectangles and numbers
        
        # full window
        width = self.offset*2 + self.hspace*3 + self.rwidth + self.noffset*2 + self.nwidth
        height = self.rheight * self.length + self.vspace*2
        self.window = GraphWin("GroceryBuddy", width, height)
        self.window.setBackground('steel blue')

        # controls
        
        # Add Button
        self.add = Button(Point(self.offset, self.vspace*1), "Add an item")
        self.add.draw(self.window)
        addInstr = Text(Point(self.offset, self.vspace*2), "Adds after the selected item \nor first if nothing is selected.")
        addInstr.draw(self.window)
        addPicLabel = Text(Point(self.offset, self.vspace*4), "PPM file")
        addPicLabel.setStyle('bold')
        addPicLabel.draw(self.window)
        self.addPic = Entry(Point(self.offset + self.hspace + self.ewidth*5, self.vspace*4 + self.eoffset), self.ewidth)
        self.addPic.draw(self.window)
        addNumLabel = Text(Point(self.offset, self.vspace*5), "Quantity")
        addNumLabel.setStyle('bold')
        addNumLabel.draw(self.window)
        self.addNum = Entry(Point(self.offset + self.hspace + self.ewidth*5, self.vspace*5 + self.eoffset), self.ewidth)
        self.addNum.draw(self.window)

        # Remove Button
        self.remove = Button(Point(self.offset, self.vspace*8), "Remove selected item")
        self.remove.draw(self.window)
        remInstr = Text(Point(self.offset, self.vspace*9), "Removes the selected item \nor none if nothing is selected.")
        remInstr.draw(self.window)

        # Update Button
        self.update = Button(Point(self.offset, self.vspace*13), "Update")
        self.update.draw(self.window)
        updateInstr = Text(Point(self.offset, self.vspace*14), "Updates the quantity of the \nselected item.")
        updateInstr.draw(self.window)
        updateLabel = Text(Point(self.offset, self.vspace*16), "Quantity")
        updateLabel.setStyle('bold')
        updateLabel.draw(self.window)
        self.updateNum = Entry(Point(self.offset + self.hspace + self.ewidth*5, self.vspace*16 + self.eoffset), self.ewidth)
        self.updateNum.draw(self.window)

        # Swap Button
        self.swap = Button(Point(self.offset, self.vspace*19), "Swap")
        self.swap.draw(self.window)
        swapInstr = Text(Point(self.offset, self.vspace*20), "Swaps the currently selected item \nwith the next one to be selected. \nTo cancel the operation mid-swap, \nsimply click elsewhere \non the application.")
        swapInstr.draw(self.window)

        # Quit Button
        self.quit = Button(Point(self.offset, self.vspace*25), "Quit")
        self.quit.draw(self.window)
        
        # the grocery items (stored in lists for rectangles (highlighting), images (pictures), and nums (quantity))
        self.rects = []
        for row in range(self.length):
            r = Rectangle(Point(self.offset + self.hspace*3, self.vspace + self.rheight*row),
                          Point(self.offset + self.hspace*3 + self.rwidth, self.vspace + self.rheight*row + self.rheight))
            r.setFill("grey")
            r.draw(self.window)
            self.rects.append(r)
        self.selected = -1
        self.images = []
        for row in range(self.length):
            i = Image(Point(self.offset + self.hspace*3 + .5*self.rwidth,
                            self.vspace + self.rheight*row + .5*self.rheight),
                      90,90)
            i.draw(self.window)
            self.images.append(i)
        self.nums = []
        for row in range(self.length):
            n = Text(Point(self.offset + self.hspace*3 + self.rwidth + self.noffset,
                           self.vspace + self.rheight*row + self.rheight*.5), "")
            n.setStyle('bold')
            n.draw(self.window)
            self.nums.append(n)

        # the list implemented by the students
        self.list = list

    def updateGui(self):
        """ Update the groceries shown on the gui to match the list. Only
            the groceries which fit on the screen will be shown. The actual
            list may be longer. If the screen is larger than the list, extra
            spaces appear as blanks. """
        
        # show all of the images that will fit in the gui
        try:
            length = min(len(self.list), self.length)
        except Exception:
            print("__len__ method is buggy or may not have been implemented.")
            length = 0

        for index in range(length):
            try:
                item = self.list.peek(index)
                (img, num) = item.get()
            except ListException:
                print("peek raised a ListException on the perfectly good index:", index)
                (img, num) = ("default.ppm", 0)
            except:
                print("peek method may not have been implemented.")
                (img, num) = ("default.ppm", 0)
                
            try:
                self.images[index].setImage(img+".ppm")
            except Exception:
                print("Bad image: " + img)
                self.images[index].setImage("default.ppm")
#                item.image = "default.ppm"
                
            self.images[index].undraw()
            self.images[index].draw(self.window)
            self.nums[index].setText(num)

        # fill in any remaining spaces with blanks
        for index in range(length,self.length):
            self.images[index].setImage(90,90)
            self.images[index].undraw()
            self.images[index].draw(self.window)
            self.nums[index].setText("")
                
    def run(self):
        """ Get and process a mouse click. Repeat till quit is pressed. """
        self.updateGui()
        
        # wait for clicks
        pt = self.window.getMouse()
            
        # Click image: stop highlighting any old image,
        # highlight this new one and select it
        if self.onImage(pt):
            self.dehighlight()
            self.selected = self.getImage(pt)
            self.highlight()
            self.run()

        # Click add: make a new item. if any rects selected,
        # put this after them, else put it first
        elif self.add.contains(self.window, pt):
            item = Item(self.addPic.getText(), self.addNum.getText())
            if self.selected > -1 and self.selected < self.length:
                try:
                   listSize = len(self.list)
                   if listSize == None:
                       print("__len__ method is buggy. It returned a None.")
                       listSize = 0
                except Exception:
                    print("__len__ method is buggy or may not have been implemented.")
                    listSize = 0
                if listSize <= self.selected:
                    self.dehighlight()
                    self.selected = listSize-1
                    self.highlight()
                self.dehighlight()
                try:
                    self.list.insert(item, self.selected+1)
                    # print("insert at ", self.selected+1)
                except Exception:
                    print("1) insert method is buggy or may not have been implemented.")
                self.selected = self.selected + 1
            else:
                try:
                    self.list.insert(item, 0)
                except Exception:
                    print("2) insert method is buggy or may not have been implemented.")
                self.selected = 0
            self.highlight()
            self.run()

        # Click remove: if anything highlighted, remove it
        elif self.remove.contains(self.window, pt):
            if self.selected > -1 and self.selected < self.length:
                self.dehighlight()
                try:
                    self.list.delete(self.selected)
                except Exception:
                    print("delete method is buggy or may not have been implemented.")
                self.selected = -1
            self.run()

        # Click update: if anything higlighted, update its quantity
        elif self.update.contains(self.window, pt):
            if self.selected > -1 and self.selected < self.length:
                try:
                    item = self.list.peek(self.selected)
                    if item == None:
                        print("peek method is buggy. It returned a None.")
                    else:
                        item.num = self.updateNum.getText()
                except ListException:
                    print("peek method raised a ListException on index:", self.selected)
                except Exception:
                    print("peek method buggy or may not have been implemented.")
            self.run()

        # Click swap: swap items
        elif self.swap.contains(self.window, pt):
            if self.selected > -1 and self.selected < self.length:
                first = self.selected
                # wait for second click
                pt = self.window.getMouse()
                # if second click is an image and not longer than list
                if self.onImage(pt):
                    second = self.getImage(pt)
                    try:
                        listSize = len(self.list)
                        if listSize == None:
                            print("__len__ method is buggy. It returned a None.")
                            listSize = 0
                    except Exception:
                        print("__len__ method is buggy or may not have been implemented.")
                        listSize = 0
                    if second < listSize:
                        # swap them
                        a = min(first, second)
                        b = max(first, second)
                        try:
                            bItem = self.list.peek(a)
                            aItem = self.list.peek(b)
                            if aItem == None or bItem == None:
                                print("peek method is buggy. It returned a None.")
                        except ListException:
                            print("peek method raised a ListException on index:", a, "or", b);
                        except Exception:
                            print("peek method is buggy or may not have been implemented.")
                          
                        try:
                            self.list.delete(b)
                            self.list.delete(a)
                        except Exception:
                            print("delete method is buggy or may not have been implemented.")

                        try:
                            self.list.insert(aItem, a)
                            self.list.insert(bItem, b)
                        except Exception:
                            print("3) insert method is buggy or may not have been implemented.")
            self.run()

        # Click quit: close window
        elif self.quit.contains(self.window, pt):
            self.window.close()

        # Click elsewhere: un highlight and un select selected image
        else:
            self.dehighlight()
            self.selected = -1
            self.run()
        
    def highlight(self):
        """ Highlight the selected image """
        if self.selected > -1 and self.selected < self.length:
            self.rects[self.selected].setOutline("orange")
            self.rects[self.selected].setFill("orange")

    def dehighlight(self):
        """ Dehighlight the selected image """
        if self.selected > -1 and self.selected < self.length:
            self.rects[self.selected].setOutline("black")
            self.rects[self.selected].setFill("grey")
            
    def onImage(self, pt):
        """ Is the point on one of the rectangles? """
        return pt.x >= self.offset + self.hspace*3 and pt.x <= self.offset + self.hspace*3 + self.rwidth and pt.y >= self.vspace and pt.y <= self.vspace + self.rheight*self.length
        
    def getImage(self, pt):
        """ Get which image the point is on. Assumes its on one! """
        return (pt.y - self.vspace) // self.rheight
        
class Item:
    """ The item container to be put in the linked list. Each item consists
        of an image (file name) and a quantity. """
    def __init__(self, image, num):
        self.image = image
        self.num = num

    def get(self):
        return (self.image, self.num)

    def __str__(self):
        return self.image + str(self.num)


