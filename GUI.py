from huffmanimplementation import *
from tkinter import *
import tkinter as tk
import os
from functools import partial 
from tkinter import filedialog

h = Huffman()
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    bytesize = os.path.getsize(filename)
    kb_size = bytesize/1000

    label_file_explorer.configure(text= f"File to Compress: {filename} \n Size of file before Compression: {kb_size}KB")
    compress = Button(window, text = 'Compress File', command = partial(huffman, filename), fg = 'green').place(x=210, y = 150)
    
    

      
def members():
    root = Toplevel(window)
    root.geometry('400x150') 
    root.minsize(400, 150)
    root.maxsize(400, 150)
    root.title('Group Members')
    labelnames = Label(root, 
                        text = 'Group Members: \n Ayesha Shaikh \n Dania Salman \n Haniya Khan \n Shafay Iqbal \n Shayan Qadri',
                         
                        width = 55, height = 6,
                        fg = 'blue'
                        ).place(x=5, y=15)

def huffman(filename):
    new = Toplevel(window)
    new.geometry('400x150')
    #new.minsize(400, 150)
    #new.maxsize(400, 150)
    new.title('Compressed File!')
    
    h.encoding_txt_file(filename, 'encoded.bin')
    bytesize = os.path.getsize(r"C:\Users\Dania\Downloads\DataStructuresII-FInalProject-final1\encoded.bin")
    kb_size = bytesize/1000

    labelcompress = Label(new, 
                        text = f"File size of compressed file: {kb_size}KB",
                        width = 55, height = 6,
                        fg = 'blue'
                        ).place(x=5, y=15)
    decmpres = Button(new, text = 'Decompress and Open' , command = decompress, fg = 'green').place(x=135, y=80)
    
     
     

def decompress():
    h.decode('encoded.bin', 'decoded')
    h.inspect_tree(h.txt_file_data)
    os.startfile('decoded')


# Create the root window
 
window = Tk()

# Set window title
window.title('Huffman Coding Project')
  
# Set window size
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500,500)
  
#Set window background color
window.config(background = "grey")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Data Structures II Project \n Huffman Coding Using Pairing Heap",
                            width = 72, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit,
                     fg = 'red',
                     activebackground = 'red',
                     activeforeground = 'white')

button_people = Button(window,
                     text = "Members",
                     fg = 'green',
                     command = members,
                     activebackground = 'red',
                     activeforeground = 'white')
 

label_file_explorer.place(x=0,y=200)
button_explore.place(x=200,y=280)
button_exit.place(x=280, y=280)
button_people.place(x=225, y=310)
 
  
# Let the window wait for any events
 
window.mainloop()

 