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
        bws_button = Button(df, text='select', command=lambda :func.d_path(self,df))
        bws_button.config(font=('courier',16))
        bws_button.grid(pady=15)
        df.grid(row=1)
        back_button = Button(df, text='cancel', command= lambda :self.home(df))
        back_button.config(font=('courier',16))
        back_button.grid()
    #home function to loop back to main screen    
    def home(self,frame):
        frame.destroy()
        self.main(root)

class func:
    #function to select path of image for "encode"
    def e_path(self,ef):       
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("error","you have selected nothing !")
        else:
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
            encode_button = Button(ep, text='cancel', command=lambda : frames.home(self,ep))
            encode_button.config(font=('courier',16))
            back_button = Button(ep, text='Encode', command=lambda : func.e_fun(self,text_area,myimg))
            back_button.config(font=('courier',16))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
    #function to convert text into base64 & merge with image        
    def e_fun(self,text_area,myimg):
        message = text_area.get("1.0", "end-1c")
        message_bytes=message.encode('ascii')
        base64_bytes=base64.b64encode(message_bytes)
        data=base64_bytes.decode('ascii')
        if not data:
            messagebox.showinfo("error","no text found! ")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            newimg.save(tkinter.filedialog.asksaveasfilename(filetypes = (('png', '*.png')),defaultextension=".png"))
            newimg.save(my_file,'png')
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful")

root=Tk()
x=frames()
x.main(root)
root.mainloop()