import tkinter as tk 
from tkinter import *
import randfacts 
import time 


def move(): 
	facts = randfacts.get_fact(True) 
	c = "*"
	label = Label(root, text=c+facts) 
	label.pack() 

def destroy(): 
	root.destroy() 


 
root = tk.Tk()  
root.config(bg="white") 
root.geometry("600x600") 

button = tk.Button(root, text="Click here for Facts", command=move) 
button1 = tk.Button(root, text="Clear and quit", command=destroy) 
button.pack() 
button1.pack() 

root.mainloop() 
