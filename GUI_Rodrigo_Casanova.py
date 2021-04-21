#Name: Rodrigo Casa Nova

#the purpose of this program is to load and execute the other two projects there were
#assigned for the project 2.

import tkinter as tk
from tkinter import filedialog
import os

#Creates the GUI
root = tk.Tk()
apps = []

#this method will be used to add the path way to the .py programs that we want to execute
def addApp():

    #this command will set the open file window once clicked,to show all incially the
    #python files (.py) files
    filename = filedialog.askopenfilename(initialdir="/", title='Select File',
                                          filetypes=(("Python Files","*.py"),
                                                     ("Executables","*.exe"),
                                                     ("All Files","*.*")))
    #to append the file path to the GUI
    apps.append(filename)
    #for loop to show the path to the disired the (.py) file
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#method to run the (.py) file added previously by the addApp()
def runApps():
    for app in apps:
        os.startfile(app)


#sets the size and color of the GUI
canvas = tk.Canvas(root, height=700,width=700,bg="#263D42")
canvas.pack()

#adds a frame to the GUI
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1,rely=0.1)

#add the button "Press here to add the .py file that you want to open first"
openFile = tk.Button(root, text="Press here to add the .py file that you want to open first",
                     padx=100,pady=50,fg="white",bg="#263D42",
                     command=addApp)
openFile.pack()

#add the "Run the (.py) file button to lauch the program
runApps = tk.Button(root, text="Run the .py file", padx=10,pady=5,fg="white",bg="#263D42",
                    command=runApps)
runApps.pack()

#main root loop
root.mainloop()

