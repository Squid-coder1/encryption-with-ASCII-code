# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:33:15 2023

@author: kmmal
"""


from tkinter import *

root=Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background='snow')

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label =Label(root,text ="Name in Ascii :", bg="light yellow", fg="black")

def asciiCoverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        
btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg='black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
        
label.place(relx=0.5,rely=0.6,anchor=CENTER)
        
root.mainloop()