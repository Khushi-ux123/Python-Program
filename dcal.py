from tkinter import *
import random 
root = Tk()  
root.geometry('400x240') 
root.title('Dosti Calculator????') 

def calculate_friendship(): 
	st = '0123456789'
	digit = 2
	temp = "".join(random.sample(st, digit)) 
	result.config(text=temp) 
 
heading = Label(root, text='Dosti Calculator????') 
heading.pack() 
slot1 = Label(root, text="Enter Your Name:") 
slot1.pack() 
name1 = Entry(root, border=5) 
name1.pack() 

slot2 = Label(root, text="Enter Your Friend Name:") 
slot2.pack() 
name2 = Entry(root, border=5) 
name2.pack()

bt = Button(root, text="Calculate", height=1, width=7, command=calculate_friendship) 
bt.pack() 


result = Label(root, text='Dosti Percentage between both of You:') 
result.pack() 
root.mainloop() 
