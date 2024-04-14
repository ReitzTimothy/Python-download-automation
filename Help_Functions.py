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

def settings():

    settings_file = open('Settings.txt', 'r+')
    settings.window = Tk()
    settings.window.title("Settings")
    settings.window.geometry("400x200")

    path_to_downloads_folder = StringVar()
    def button_1_press():
        path = path_to_downloads_folder.get()
        print(path)

    def button_2_press():
        settings.window.destroy()

    Label_1 = Label(settings.window, text='Path of your downloads folder:', font=(14))
    Label_1.grid(row=0, column=0, padx=5, pady=5)
    Entry_1 = Entry(settings.window,textvariable=path_to_downloads_folder,font=(14))
    Entry_1.grid(row=1,column=0,padx=5,pady=5)
    Entry_1.insert(END,"hello")
    button_1=Button(settings.window,command=button_1_press,text='Submit',font=(14))
    button_1.grid(row=2,column=0,padx = 80,pady=10,sticky=W)
    button_2=Button(settings.window,command=button_2_press,text='Close',font=(14))
    button_2.grid(row=2,column=1,padx=80,pady=10, sticky=E)
    settings.window.mainloop()
    settings_file.close()

#    if len(settings.path_to_downloads_folder.get()) == 0:
#        messagebox.showerror(title='Error',
 #                            message='Some settings are blank. Please make sure all settings are filled in correctly')
  #  else:
   #     setup.settings_file.write(settings.path_to_downloads_folder.get())
    #    messagebox.showinfo(title='Success', message='You have successful configured your program')