from PIL import Image
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def convert(filename):
    modifiedName = ''

    target = os.path.join(APP_ROOT,"upload\\")
    im = Image.open(target+filename)
    # Getting extension
    extension = os.path.splitext(filename)[1]

    if extension == '.jpg':
        modifiedName = filename.replace('.jpg', '')
        rgb_im = im.convert('RGB')
        rgb_im.save(target+'converted_'+modifiedName +'.png')
        print("File converted from JPG to PNG")
        name = "converted_"+modifiedName+'.png'
        return name

    elif extension == '.png':
        modifiedName = filename.replace('.png', '')
        rgb_im = im.convert('RGB')
        rgb_im.save(target+'converted_'+modifiedName +'.jpg')
        print("File converted from PNG to JPG")
        name = "converted_"+modifiedName+'.jpg'
        return name

    elif extension == '.jpeg':
        modifiedName = filename.replace('.jpeg', '')
        rgb_im = im.convert('RGB')
        rgb_im.save(target+'converted_'+modifiedName +'.png')
        print("File converted from JPEG to PNG")
        name = "converted_"+modifiedName+'.png'
        return name