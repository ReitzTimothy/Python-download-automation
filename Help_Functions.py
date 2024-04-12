######################################################################
# Author: Timothy Reitz Date: 4-April-2024
#
# Description:
# This file contains helper function that are used in the main program.
#
# Revision History:
# Name: Timothy Reitz Date:4-April Description: Initial version
#######################################################################

# Libraries
from tkinter import *
from tkinter import messagebox

def setup():
    download_path = settings()

def settings():
    settings.window = Tk()
    settings.window.title("Settings")
    settings.window.geometry("400x200")

    Label_1 = Label(settings.window,text='Path of your downloads folder:', font=(14))
    Label_1.grid(row=0, column=0,padx=5,pady=5)
    settings.path_to_downloads_folder = StringVar()
    Entry_1 = Entry(settings.window,textvariable=settings.path_to_downloads_folder,font=(14))
    Entry_1.grid(row=1,column=0,padx=5,pady=5)
    button_1=Button(settings.window,command=button_1_press,text='Submit',font=(14))
    button_1.grid(row=2,column=0,padx = 80,pady=10,sticky=W)
    button_2=Button(settings.window,command=button_2_press,text='Close',font=(14))
    button_2.grid(row=2,column=1,padx=80,pady=10, sticky=E)
    settings.window.mainloop()
    return settings.path_to_downloads_folder.get()

def button_1_press():
    if len(settings.path_to_downloads_folder.get())==0:
        messagebox.showerror(title='Error', message='Some settings are blank. Please make sure all settings are filled in correctly')
    else:
        messagebox.showinfo(title='Success',message = 'You have successful configured your program')
def button_2_press():
    settings.window.destroy()