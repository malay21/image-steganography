import base64 

def decrypt(base64_msg):
    base64_bytes=base64_msg.encode('ascii')
    message_bytes=base64.b64decode(base64_bytes)
    message=message_bytes.decode('ascii')
    #print("decrypted message : ", message)

def encrypt(message):
    message_bytes=message.encode('ascii')
    base64_bytes=base64.b64encode(message_bytes)
    base64_msg=base64_bytes.decode('ascii')
    #print("encrypted message : ", base64_msg)


