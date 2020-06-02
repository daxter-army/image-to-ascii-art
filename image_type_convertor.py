from PIL import Image
import os

def convert(filename):
    modifiedName = ''

    im = Image.open("./upload/"+filename)
    # Getting extension
    extension = os.path.splitext(filename)[1]

    if extension == '.jpg':
        modifiedName = filename.replace('.jpg', '')
        rgb_im = im.convert('RGB')
        rgb_im.save('./upload/converted_'+ modifiedName +'.png')
        print("File converted from JPG to PNG")
        name = "converted_"+modifiedName+'.png'
        return name

    elif extension == '.png':
        modifiedName = filename.replace('.png', '')
        rgb_im = im.convert('RGB')
        rgb_im.save('./upload/converted_'+ modifiedName +'.jpg')
        print("File converted from PNG to JPG")
        name = "converted_"+modifiedName+'.jpg'
        return name

    elif extension == '.jpeg':
        modifiedName = filename.replace('.jpeg', '')
        rgb_im = im.convert('RGB')
        rgb_im.save('./upload/converted_'+ modifiedName +'.png')
        print("File converted from JPEG to PNG")
        name = "converted_"+modifiedName+'.png'
        return name