from cgitb import text
from email.mime import image
from posixpath import abspath
from struct import pack
import tkinter
from PIL import Image, ImageTk
import random
import Consoled20program
import os

#setup all images
currentdirectory = os.path.dirname(__file__)
abspath = os.path.join(currentdirectory, './d20images/')
image1 = Image.open(abspath+'d20_1.png') 
image2 = Image.open(abspath+'d20_2.png')
image3 = Image.open(abspath+'d20_3.png')
image4 = Image.open(abspath+'d20_4.png')
image5 = Image.open(abspath+'d20_5.png')
image6 = Image.open(abspath+'d20_6.png')
image7 = Image.open(abspath+'d20_7.png')
image8 = Image.open(abspath+'d20_8.png')
image9 = Image.open(abspath+'d20_9.png')
image10 = Image.open(abspath+'d20_10.png')
image11 = Image.open(abspath+'d20_11.png')
image12 = Image.open(abspath+'d20_12.png')
image13 = Image.open(abspath+'d20_13.png')
image14 = Image.open(abspath+'d20_14.png')
image15 = Image.open(abspath+'d20_15.png')
image16 = Image.open(abspath+'d20_16.png')
image17 = Image.open(abspath+'d20_17.png')
image18 = Image.open(abspath+'d20_18.png')
image19 = Image.open(abspath+'d20_19.png')
image20 = Image.open(abspath+'d20_20.png')

#setup window
root = tkinter.Tk()
root.geometry('400x400')
root.title('DnD D20 Roller')
root.configure(bg='cyan')

#setup placeholder image
test = ImageTk.PhotoImage(image20)
label1 = tkinter.Label(root, image=test, bg='cyan')
label1.pack()


def roll():
    number = Consoled20program.rolld20()
    print(number)
    match number:
        case 1: 
            test = ImageTk.PhotoImage(image1)
            label1.configure(image = test)
            label1.image = test
        case 2: 
            test = ImageTk.PhotoImage(image2)
            label1.configure(image = test)
            label1.image = test  
        case 3: 
            test = ImageTk.PhotoImage(image3)
            label1.configure(image = test)
            label1.image = test  
        case 4: 
            test = ImageTk.PhotoImage(image4)
            label1.configure(image = test)
            label1.image = test 
        case 5: 
            test = ImageTk.PhotoImage(image5)
            label1.configure(image = test)
            label1.image = test 
        case 6: 
            test = ImageTk.PhotoImage(image6)
            label1.configure(image = test)
            label1.image = test 
        case 7: 
            test = ImageTk.PhotoImage(image7)
            label1.configure(image = test)
            label1.image = test 
        case 8: 
            test = ImageTk.PhotoImage(image8)
            label1.configure(image = test)
            label1.image = test 
        case 9: 
            test = ImageTk.PhotoImage(image9)
            label1.configure(image = test)
            label1.image = test 
        case 10: 
            test = ImageTk.PhotoImage(image10)
            label1.configure(image = test)
            label1.image = test 
        case 11: 
            test = ImageTk.PhotoImage(image11)
            label1.configure(image = test)
            label1.image = test 
        case 12: 
            test = ImageTk.PhotoImage(image12)
            label1.configure(image = test)
            label1.image = test 
        case 13: 
            test = ImageTk.PhotoImage(image13)
            label1.configure(image = test)
            label1.image = test 
        case 14: 
            test = ImageTk.PhotoImage(image14)
            label1.configure(image = test)
            label1.image = test 
        case 15: 
            test = ImageTk.PhotoImage(image15)
            label1.configure(image = test)
            label1.image = test 
        case 16: 
            test = ImageTk.PhotoImage(image16)
            label1.configure(image = test)
            label1.image = test 
        case 17: 
            test = ImageTk.PhotoImage(image17)
            label1.configure(image = test)
            label1.image = test 
        case 18: 
            test = ImageTk.PhotoImage(image18)
            label1.configure(image = test)
            label1.image = test 
        case 19: 
            test = ImageTk.PhotoImage(image19)
            label1.configure(image = test)
            label1.image = test 
        case _: 
            test = ImageTk.PhotoImage(image20)
            label1.configure(image = test)
            label1.image = test      
             

#setup title
welcomemessage = tkinter.Label(root, text='Welcome to Dnd Roller', fg='black', bg='cyan', font='Helvetica 16 bold italic')
welcomemessage.pack()

#setup button
button = tkinter.Button(root, text='Roll D20', command= roll)
button.pack()

root.mainloop()