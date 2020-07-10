![Bmessenger](/logo/logo.png) <br/>
BMESSENGER

> "Bmessenger" is a cross-platform application, it can be used on windows or linux with proper setup.

> This is a python based image steganography application which provides double protection to create secret message.

---

## Requirement
 - python 3.8
 - pillow (python image library)
    - can be installed via <br/>
    ```shell
   $ pip install pillow
    ```
 - tkinter (python GUI library)
    - can be installd via <br/>
   ```shell
   $ pip install tk
    ```
---
## basic working
 - encode:
   - select any image.
   - this image is converted into png format.
   - you massage taken from text box converted to base64. 
   - merge this base64 encoded string with image.
   - user is given option to save image wherever he/she wants.

 - decode:
   - select image which is encoded.
   - the base64 string is seprated using decode function.
   - base64 string is decoded.
   - by tkinter the output is shown in a textbox.
---
## Guide
   - **for encoding**
      - select encode from home screen
      - next screen will give you option to select image or cancel operation and go back to home screen
      - select your image type by drop down menu if not listed use file type as "all files"
      - preview of your screen is provided here in a small size and user can add message in the text box.
      - after entering the message press encode and a save file window will open
      - user is strictly adviced to use PNG extension for saving the file
   ![encode_window](/readmeimages/encode_msg.png)
   - **for decoding**
      - select decode from home screen
      - next screen will give you option to select image or cancel operation and go back to home screen
      - next screen will show the hidden text
   ![encode_window](/readmeimages/decode_msg.png)
---

## Refrences
 - https://www.geeksforgeeks.org/image-based-steganography-using-python/
 - https://docs.python.org/3/library/tkinter.html
 - https://pillow.readthedocs.io/en/stable/
 - https://docs.python.org/3/library/base64.html