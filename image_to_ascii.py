from PIL import Image, ImageDraw, ImageFont
import math, os
from image_type_convertor import convert

# Path for current file system
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# If traditional method fails, then change the image format to png/jpg, and then again try
# Character array and slice each character

def image_to_ascii(filename):
    characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    # Converting into list
    charactersArray = list(characters)
    # Getting Length
    charactersLength = len(charactersArray)
    interval = charactersLength/256
    scaleFactor = 0.09
    # Dimensions of One character, space it will use
    oneCharacterWidth = 10
    oneCharacterHeight = 15

    def getChar(inputInt):
        return charactersArray[math.floor(inputInt*interval)]

    # Write output to a text file
    # text_file = open("output_ascii_art.txt", "w")
    # Open Image
    target = os.path.join(APP_ROOT,"upload\\")
    print(target)
    im = Image.open(target+filename)
    # Path to font
    fnt = ImageFont.truetype(os.path.join(APP_ROOT,"static\\font\\lucon.ttf"), 15)
    # Calculating size
    width, height = im.size
    # Resizing Image
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharacterWidth/oneCharacterHeight))), Image.NEAREST)

    # Assigning new size
    width, height = im.size
    pix = im.load()

    outputImage = Image.new('RGB', (oneCharacterWidth * width, oneCharacterHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            # text_file.write(getChar(h))
            d.text((j*oneCharacterWidth, i*oneCharacterHeight), getChar(h), font = fnt, fill = (r, g, b))

        # text_file.write('\n')
    # text_file.close()
    # Covert to grayscale
    # outputImage.convert('LA')
    outputImage.save(os.path.join(APP_ROOT,"static\\output\\"+filename))
    return filename