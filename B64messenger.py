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
    def decode_page(self,f):
        f.destroy()
        df = Frame(root)
        l1 = Label(df, text='Give the path of Encoded image your image:')
        l1.grid(pady=30)
        bws_button = Button(df, text='path', command=lambda :self.d_path(df))
        bws_button.grid()
        df.grid(row=1)
        back_button = Button(df, text='cancel', command= lambda :self.home(df))
        back_button.grid()
    
    #(GUI function)function for creating page after pressing encode button
    def encode_page(self,f):
        f.destroy()
        ef = Frame(root)
        l1= Label(ef,text='Select your image:')
        l1.config(font=('courier',18))
        l1.grid(pady=15)
        bws_button = Button(ef,text='select',command=lambda : self.e_path(ef))
        bws_button.config(font=('courier',16))
        bws_button.grid(pady=15)
        ef.grid(row=1)
        back_button = Button(ef, text='cancel', command=lambda :self.home(ef))
        back_button.grid()
        back_button.config(font=('courier',16))

    def e_path(self,ef):       
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('Image Files', '*.png *.jpg')]))
        myimg = Image.open(myfile)
        myimage = myimg.resize((250,150))
        ef.destroy()
        img = ImageTk.PhotoImage(myimage)
        l3= Label(ep,text='selected image')
        l3.grid()
        panel = Label(ep, image=img)
        panel.image = img
        self.o_image_size = os.stat(myfile)
        self.o_image_w, self.o_image_h = myimg.size
        panel.grid()
        l2 = Label(ep, text='Enter the message')
        l2.config(font=('courier',18))
        l2.grid(pady=15)
        text_area = Text(ep, width=50, height=10)
        text_area.grid()
        encode_button = Button(ep, text='Encode', command=lambda :self.enc_fun(text_area,myimg))
        encode_button.config(font=('courier',16))
        back_button = Button(ep, text='<--', command=lambda : self.home(ep))
        back_button.config(font=('courier',16))
        back_button.grid(pady=15)
        encode_button.grid()
        ep.grid(row=1)



    #(GUI function)front page
    def main(self,root):
        o_image_size=0
        root.title('Bmessenger')
        root.geometry('400x600')
        root.resizable(width =False, height=False)
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
    def home(self,frame):
        frame.destroy()
        self.main(root)
root=Tk()
x=imgstegno()
x.main(root)
root.mainloop()