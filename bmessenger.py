import base64
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import  os

class frames:
    #main frame or start page
    def main(self,root):
        o_image_size=0
        root.title('Bmessenger')
        root.geometry('400x600')
        root.resizable(width =False, height=False)
        #root.minsize(width =400, height=500)  #if you want to make it resizable
        f = Frame(root)
        title = Label(f,text='Bmessenger')
        title.config(font=('courier',18))
        title.grid(pady=20)

        b_encode = Button(f,text='encode',command= lambda :self.encode_page(f))
        b_encode.config(font=('courier',16))
        b_encode.grid(pady=15)
        b_decode = Button(f,text='decode', command=lambda :self.decode_page(f))
        b_decode.config(font=('courier',16))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        f.grid(row =1)
        b_encode.grid()
        b_decode.grid()
    
    #frame for encode page 
    def encode_page(self,f):
        f.destroy()
        ef = Frame(root)
        l1= Label(ef,text='Select your image :')
        l1.config(font=('courier',18))
        l1.grid(pady=15)
        bws_button = Button(ef,text='select',command=lambda : func.e_path(self,ef))
        bws_button.config(font=('courier',16))
        bws_button.grid(pady=15)
        ef.grid(row=1)
        back_button = Button(ef, text='cancel', command=lambda :self.home(ef))
        back_button.grid()
        back_button.config(font=('courier',16))

    #frame for decode page
    def decode_page(self,f):
        f.destroy()
        df = Frame(root)
        l1 = Label(df, text='Select file to decode :')
        l1.config(font=('courier',18))
        l1.grid(pady=15)
        bws_button = Button(df, text='select', command=lambda :self.d_path(df))
        bws_button.config(font=('courier',16))
        bws_button.grid(pady=15)
        df.grid(row=1)
        back_button = Button(df, text='cancel', command= lambda :self.home(df))
        back_button.config(font=('courier',16))
        back_button.grid()
   
root=Tk()
x=frames()
x.main(root)
root.mainloop()