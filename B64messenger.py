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
    def decrypt(self,base64_msg):
        base64_bytes=base64_msg.encode('ascii')
        message_bytes=base64.b64decode(base64_bytes)
        message=message_bytes.decode('ascii')
        #print("decrypted message : ", message)

    #fuction to encrypt the message using base64
    def encrypt(self,message):
        message_bytes=message.encode('ascii')
        base64_bytes=base64.b64encode(message_bytes)
        data=base64_bytes.decode('ascii')
        #print("encrypted message : ", base64_msg)
    
    #(GUI function)function for creating page after pressing decode button
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
    
    #(GUI function)function for creating page after pressing encode button
    def encode_page(self,f):
        f.destroy()
        ef = Frame(root)
        l1= Label(ef,text='Select your image :')
        l1.config(font=('courier',18))
        l1.grid(pady=15)
        bws_button = Button(ef,text='select',command=lambda : self.e_path(ef))
        bws_button.config(font=('courier',16))
        bws_button.grid(pady=15)
        ef.grid(row=1)
        back_button = Button(ef, text='cancel', command=lambda :self.home(ef))
        back_button.grid()
        back_button.config(font=('courier',16))

    #(GUI function)function for selecting image and take text input
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
            encode_button = Button(ep, text='cancel', command=lambda : self.home(ep))
            encode_button.config(font=('courier',16))
            back_button = Button(ep, text='Encode', command=lambda :self.e_fun(text_area,myimg))
            back_button.config(font=('courier',16))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
    #encode function for 
    def e_fun(self,text_area,myimg):
        message = text_area.get("1.0", "end-1c")
        message_bytes=message.encode('ascii')
        base64_bytes=base64.b64encode(message_bytes)
        data=base64_bytes.decode('ascii')
        if not data:
            messagebox.showinfo("error","no text found! ")
        else:
            messagebox.showinfo("encrypted text",data)
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            newimg.save('o.png')
            newimg.save(my_file,'png')
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful")
    
    def modPix(self,pix, data):

        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)

        for i in range(lendata):

            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def genData(self,data):

        # list of binary codes
        # of given data
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    #(GUI function)front page
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
    
    #loop for main frame
    def home(self,frame):
        frame.destroy()
        self.main(root)
root=Tk()
x=imgstegno()
x.main(root)
root.mainloop()