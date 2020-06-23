#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jun 23, 2020 02:45:21 PM CEST  platform: Windows NT

import sys
from tkinter import filedialog

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    root = tk.Tk()
    top = IMA(root)
    root.mainloop()

w = None
def create_IMA(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_IMA(root, *args, **kwargs)' .'''
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    top = IMA(w)
    return (w, top)

def destroy_IMA():
    global w
    w.destroy()
    w = None

class IMA:
    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
           
        self.Selection = None
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 7"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x400+592+230")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("I.M.A")
        top.configure(background="#d9d9d9")

        self.ButtonRun = tk.Button(top)
        self.ButtonRun.place(relx=0.717, rely=0.8, height=63, width=146)
        self.ButtonRun.configure(activebackground="#b0b6e1")
        self.ButtonRun.configure(activeforeground="#000000")
        self.ButtonRun.configure(background="#d9d9d9")
        self.ButtonRun.configure(disabledforeground="#a3a3a3")
        self.ButtonRun.configure(foreground="#000000")
        self.ButtonRun.configure(highlightbackground="#d9d9d9")
        self.ButtonRun.configure(highlightcolor="black")
        self.ButtonRun.configure(pady="0")
        self.ButtonRun.configure(text='Run')

        self.LabelTitle = tk.Label(top)
        self.LabelTitle.place(relx=0.417, rely=0.05, height=48, width=92)
        self.LabelTitle.configure(activebackground="#f0f0f0f0f0f0")
        self.LabelTitle.configure(background="#d9d9d9")
        self.LabelTitle.configure(disabledforeground="#a3a3a3")
        self.LabelTitle.configure(foreground="#000000")
        self.LabelTitle.configure(text='I.M.A')

        self.LabelSubTitle = tk.Label(top)
        self.LabelSubTitle.place(relx=0.25, rely=0.125, height=26, width=292)
        self.LabelSubTitle.configure(background="#d9d9d9")
        self.LabelSubTitle.configure(disabledforeground="#a3a3a3")
        self.LabelSubTitle.configure(font=font9)
        self.LabelSubTitle.configure(foreground="#000000")
        self.LabelSubTitle.configure(text='Adapt your Music to your GamePlay')

        self.ButtonMusic = tk.Button(top)
        self.ButtonMusic.place(relx=0.467, rely=0.28, height=33, width=48)
        self.ButtonMusic.configure(activebackground="#ececec")
        self.ButtonMusic.configure(command=self.putInFile)
        self.ButtonMusic.configure(activeforeground="#000000")
        self.ButtonMusic.configure(background="#d9d9d9")
        self.ButtonMusic.configure(cursor="fleur")
        self.ButtonMusic.configure(disabledforeground="#a3a3a3")
        self.ButtonMusic.configure(foreground="#000000")
        self.ButtonMusic.configure(highlightbackground="#d9d9d9")
        self.ButtonMusic.configure(highlightcolor="black")
        self.ButtonMusic.configure(pady="0")
        self.ButtonMusic.configure(text='Done')

        self.LabelMusic = tk.Label(top)
        self.LabelMusic.place(relx=0.033, rely=0.30, height=26, width=132)
        self.LabelMusic.configure(background="#d9d9d9")
        self.LabelMusic.configure(disabledforeground="#a3a3a3")
        self.LabelMusic.configure(foreground="#000000")
        self.LabelMusic.configure(text='Add your music in :')

        self.ListboxMusic = tk.Listbox(top)
        self.ListboxMusic.place(relx=0.267, rely=0.255, relheight=0.14
                , relwidth=0.173)
        self.ListboxMusic.insert(1,"Calm")
        self.ListboxMusic.insert(2,"Action")
        self.ListboxMusic.insert(3,"Sad")
        self.ListboxMusic.bind('<<ListboxSelect>>', self.select)
        self.ListboxMusic.configure(background="white")
        self.ListboxMusic.configure(disabledforeground="#a3a3a3")
        self.ListboxMusic.configure(font="TkFixedFont")
        self.ListboxMusic.configure(foreground="#000000")
        self.ListboxMusic.configure(selectmode='single')
        
        self.MessageCMusic = tk.Message(top)
        self.MessageCMusic.place(relx=0.017, rely=0.825, relheight=0.075
                , relwidth=0.477)
        self.MessageCMusic.configure(anchor='w')
        self.MessageCMusic.configure(background="#d9d9d9")
        self.MessageCMusic.configure(cursor="fleur")
        self.MessageCMusic.configure(foreground="#000000")
        self.MessageCMusic.configure(highlightbackground="#d9d9d9")
        self.MessageCMusic.configure(highlightcolor="black")
        self.MessageCMusic.configure(text='Current Music :')
        self.MessageCMusic.configure(width=286)

        self.TPReset = ttk.Progressbar(top)
        self.TPReset.place(relx=0.233, rely=0.47, relwidth=0.35, relheight=0.0
                , height=15)
        self.TPReset.configure(length="210")
        self.TPReset.configure(cursor="fleur")

        self.ButtonReset = tk.Button(top)
        self.ButtonReset.place(relx=0.033, rely=0.45, height=33, width=86)
        self.ButtonReset.configure(activebackground="#ececec")
        self.ButtonReset.configure(activeforeground="#000000")
        self.ButtonReset.configure(background="#d9d9d9")
        self.ButtonReset.configure(disabledforeground="#a3a3a3")
        self.ButtonReset.configure(foreground="#000000")
        self.ButtonReset.configure(highlightbackground="#d9d9d9")
        self.ButtonReset.configure(highlightcolor="black")
        self.ButtonReset.configure(pady="0")
        self.ButtonReset.configure(text='Recalibrate')

    def select(self,event):
        self.Selection = self.ListboxMusic.selection_get()
        print(self.Selection)
    
    def putInFile(self):
        MusicFile = filedialog.askopenfilename(filetypes=(("Wav file", "*.wav"),))

        


if __name__ == '__main__':
    vp_start_gui()