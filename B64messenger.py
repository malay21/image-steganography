import base64
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import  os

class imgstegno:
    #function to decrypt the message using base64
    def decrypt(base64_msg):
        base64_bytes=base64_msg.encode('ascii')
        message_bytes=base64.b64decode(base64_bytes)
        message=message_bytes.decode('ascii')
        #print("decrypted message : ", message)

    #fuction to encrypt the message using base64
    def encrypt(message):
        message_bytes=message.encode('ascii')
        base64_bytes=base64.b64encode(message_bytes)
        base64_msg=base64_bytes.decode('ascii')
        #print("encrypted message : ", base64_msg)
    
    #(GUI function)function for creating page after pressing decode button
    def d_page1(self,f):
        f.destroy()
        d_f2 = Frame(root)
        l1 = Label(d_f2, text='Give the path of Encoded image your image:')
        l1.grid(row=1)
        bws_button = Button(d_f2, text='path', command=lambda :self.d_give_path(d_f2))
        bws_button.grid()
        d_f2.grid(row=1)
    
    #(GUI function)function for creating page after pressing encode button
    def page2(self,f):
        f.destroy()
        f2 = Frame(root)
        l1= Label(f2,text='Give the path of your image:')
        l1.grid()
        bws_button = Button(f2,text='path',command=lambda : self.give_path(f2))
        bws_button.grid()
        f2.grid(row=1)
    
    #(GUI function)front page
    def main(self,root):
        o_image_size=0
        root.title('Bmessenger')
        root.geometry('400x400')
        root.resizable(width =False, height=False)
        f = Frame(root)
        
        title = Label(f,text='Bmessenger')
        title.config(font=('courier',20))
        title.grid(pady=30)

        b_encode = Button(f,text='encode',command= lambda :self.page2(f))
        b_encode.config(font=('courier',18))
        b_decode = Button(f,text='decode', command=lambda :self.d_page1(f))
        b_decode.config(font=('courier',18))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        f.grid(row =1)
        b_encode.grid()
        b_decode.grid()
root=Tk()
x=imgstegno()
x.main(root)
root.mainloop()