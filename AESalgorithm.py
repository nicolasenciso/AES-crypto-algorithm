from Crypto.Cipher import AES
import base64
import Image
import hashlib
import io
#Algorith made by Nicolas Ricardo Enciso, AES encryption
def convertToByteArray(originalImage):
    with open(originalImage, "rb") as f:
        return bytearray(f.read())

def menu():
    print(">>>>>>>>>>> Bienvenido <<<<<<<<<<<<<<<")
    print("> Ingrese el nombre de la imagen a cifrar (debe estar en el mismo lugar del presente software")
    image = raw_input()
    print("> Ingrese el formato de la imagen (jpg, png, gif) ")
    imageFormat = raw_input()
    print("> Ingrese el nombre para la imagen descifrada de salida")
    desimage = raw_input()
    originalImage = str(image)+str('.')+str(imageFormat)
    byteImage = convertToByteArray(originalImage)
    print("> Ingrese el modo de operacion (128, 192 o 256 bits)")
    mode = int(raw_input())
    print("> Ingrese la llave")
    key = raw_input()
    IV = 16 * '\x00'
    if mode == 128:
        key = hashlib.sha1(key).digest()
        key = key[0:len(key)-4]
    elif mode == 192:
        key = hashlib.sha224(key).digest()  #sha256 make padding to a key of size multiple of 16
        key = key[0:len(key)-4]
    elif mode == 256:
        key = hashlib.sha256(key).digest()
    aes = AES.new(key,AES.MODE_CBC, IV = IV)#A
    text = base64.b64encode(byteImage)      #B
    cipherImg = aes.encrypt(text)           #C
    cipherImg = base64.b64encode(cipherImg) #D
    print("> Texto codificado cifrado: ")
    print(cipherImg)
    print("> Iniciando descifrado: ")
    descipher = base64.b64decode(cipherImg)#E
    decryptor = AES.new(key,AES.MODE_CBC, IV = IV)
    plain = decryptor.decrypt(descipher)         #F
    deimage = base64.b64decode(plain)      #G
    image = Image.open(io.BytesIO(deimage))#H
    image.save(str(desimage)+'.'+str(imageFormat))
    print("> Su imagen ha sido descifrada")
    

menu()