# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:03:51 2017

@author: Christian
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

# Define Constants
LARGE_FONT = ("Verdana", 12)
# Create sample graph for test use
f = Figure(figsize=(5,5), dpi=100)

# Plot the points and add subplot a to figure f
a = f.add_subplot(111)

# Define the style for matplotlib
style.use("ggplot")

# Animation function for animating the graphs
def animate(i):
    
    # Read data from the specified file and store into pullData
    pullData = open("sampleData.txt","r").read()
    
    # Split the data it reads by every newline character
    dataList = pullData.split('\n')
    
    # Create the xList and yList for the data
    xList = []
    yList = []
    
    # Loop through every line of the text file
    for eachLine in dataList:
        
        # Check to make sure the line is not just 1 character (gets rid of lone newline characters)
        if len(eachLine) > 1:
            # Split the data read again by ,
            x, y = eachLine.split(',')
            
            # Store into xList and yList respectively
            xList.append(int(x))
            yList.append(int(y))
            
    # Clear the plot so it doesn't plot a new graph over itself
    a.clear()
    
    # Plot the next instance of the graph
    a.plot(xList, yList)

class IPS_Man(tk.Tk):
    
    # Initialization of everything needed to start the application
    def __init__(self, *args, **kwargs):
        
        # Run the tkinter init function
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set the icon for the window
        tk.Tk.iconbitmap(self, "ninjastaricon128.ico")
        
        # Set the title for the window
        tk.Tk.wm_title(self, "IPS Man 0.0.1")
        
        # Create a container to contain everything 
        container = tk.Frame(self)
        
        # fill="both" will fill in the space allotted for the pack, expand = True will allow for expanding beyond the limits set
        container.pack(side="top", fill="both", expand = True)
        
        # Configure the rows and columns
        # 0 = minimum size, weight = 1 (priority)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Set self.frames = empty dictionary
        # Will hold the frames for the GUI
        self.frames = {}
        
        # Add all the pages to the dictionary self.frames
        for F in (StartPage, PageOne, PageTwo, PageThree):
        
            # Create the StartPage frame which is the initial page
            frame = F(container, self)
            
            # Put the StartPage into the frames dictionary
            self.frames[F] = frame
            
            # Set a grid at row 0 and column 0 and stretch/alignment north,south,east,west (entire window)
            frame.grid(row=0, column = 0, sticky="nsew")
        
        # Show the StartPage frame
        self.show_frame(StartPage)
        
    # show_frame function which shows whatever frame that is passed in as controller
    # Input: self, cont    :   cont = controller
    def show_frame(self, cont):
        
        # Set frame = the controller or frame to show
        frame = self.frames[cont]
        
        # Bring the frame to the front
        frame.tkraise()
        
# StartPage Class, inherits from tk.Frame        
class StartPage(tk.Frame):
    
    # Initialization for the StartPage
    def __init__(self, parent, controller):
        
        # Initialize tk.Frame
        tk.Frame.__init__(self, parent)
        
        # Create label object from the tk.Label class
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        
        # Put the label(text) onto the StartPage frame with padding
        label.pack(pady=10,padx=10)
        
        # Create a button object from tk.Button class
        # button1 = ttk.Button(self, text="Visit Page 1", command=functionhere)
        # button1 = ttk.Button(self, text="Visit Page 1", command=lambda: functionhere("works with params"))
        button1 = ttk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        
        # Put the button onto the StartPage frame
        button1.pack()
        
        # Create a button object from tk.Button class
        button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        
        # Put the button onto the frame
        button2.pack()
        
        # Create a button object from tk.Button class
        button3 = ttk.Button(self, text="Graph Page", command=lambda: controller.show_frame(PageThree))
        
        # Put the button onto the frame
        button3.pack()
        
# PageOne Class, inherits from tk.Frame
class PageOne(tk.Frame):
    
    # Initialization for the Page
    def __init__(self, parent, controller):
        
        # Initialize tk.Frame
        tk.Frame.__init__(self, parent)
        
        # Create label object from the tk.Label class
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        
        # Put the label(text) onto the frame with padding
        label.pack(pady=10,padx=10)
        
        # Create a button object from tk.Button class
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        
        # Put the button onto the frame
        button1.pack()
        
        # Create a button object from tk.Button class
        button2 = ttk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        
        # Put the button onto the frame
        button2.pack()

# PageTwo Class, inherits from tk.Frame
class PageTwo(tk.Frame):
    
    # Initialization for the Page
    def __init__(self, parent, controller):
        
        # Initialize tk.Frame
        tk.Frame.__init__(self, parent)
        
        # Create label object from the tk.Label class
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        
        # Put the label(text) onto the frame with padding
        label.pack(pady=10,padx=10)
        
        # Create a button object from tk.Button class
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        
        # Put the button onto the frame
        button1.pack()
        
        # Create a button object from tk.Button class
        button2 = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        
        # Put the button onto the frame
        button2.pack()
        
# PageThree Class, inherits from tk.Frame
class PageThree(tk.Frame):
    
    # Initialization for the Page
    def __init__(self, parent, controller):
        
        # Initialize tk.Frame
        tk.Frame.__init__(self, parent)
        
        # Create label object from the tk.Label class
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        
        # Put the label(text) onto the frame with padding
        label.pack(pady=10,padx=10)
        
        # Create a button object from tk.Button class
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        
        # Put the button onto the frame
        button1.pack()
        
        # Create the canvas to draw on
        canvas = FigureCanvasTkAgg(f, self)
        
        # Show the canvas
        canvas.show()
        
        # Put the canvas into the tkinter window
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        # Create the toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        
        # Show the toolbar and update
        toolbar.update()
        
        # Add the toolbar to the tkinter window
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
app = IPS_Man()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()