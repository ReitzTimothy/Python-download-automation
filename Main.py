######################################################################
# Author: Timothy Reitz Date: 4-April-2024
#
# Description:
# This file is the main driver file to automated the sorting of a downloads folder based on file type.
#
# Revision History:
# Name: Timothy Reitz Date:4-April Description: Initial version
#######################################################################

#Libraries
from os import *
from Help_Functions import *
from tkinter import *


def main ():
 Main_window = Tk()
 Main_window.title('Home Screen')
 Main_window.geometry("500x500")
 button_1 = Button(Main_window, command=settings, text='Settings', font=(14))
 button_1.grid(row=5, column=1, padx=80, pady=10, sticky=W)
 button_2 = Button(Main_window, text='Run', font=(14))
 button_2.grid(row=5, column=0, padx=80, pady=10, sticky=W)
 Main_window.mainloop()

if __name__ == "__main__":
 main()