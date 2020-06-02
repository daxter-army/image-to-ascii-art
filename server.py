from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import os, time

# Other files
from image_to_ascii import image_to_ascii
from image_type_convertor import convert

__author__ = 'Mehul Singh Teya'

app = Flask(__name__)
app.secret_key = 'iaminevitable'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, "upload\\")
        
        if os.path.isdir(target):
            print('Directory Exists')
        else:
            os.mkdir(target)
            # print('Directory Created')
        
        file = request.files['upload-image']
        fileName = file.filename

        # Removing special characters, because some images do not show up
        specialChars = ["'","!","@","#","$","%","^","&","*","(",")","_","-","=","+","/","*","-",";",":",">","<",",","?","}","{"]
        for badWord in specialChars:
            fileName = fileName.replace(badWord, "")
        # Print Filename
        # print("File Uploaded : " + fileName)
        
        #todo Checking Filesize
        
        # Checking File Extensions
        extension = os.path.splitext(fileName)[1]
        # print("File Extension : " + extension)

        if not (extension==".jpeg" or extension==".jpg" or extension==".png"):
            flash('File Format not supported')
            return redirect(url_for('index'))
        else:
            try:
                # Saving File
                destination = "/".join([target, fileName])
                file.save(destination)
                # Sending file to converter function
                finalFile = image_to_ascii(fileName)
                # Send Image back to user
                return render_template('response.html', image = finalFile)
            except:
                print('Converting...')
                output = convert(fileName)
                stream = image_to_ascii(output)
                return render_template('response.html', image = stream)

@app.route('/delete/<filename>')
def delete(filename):
    uploadedImage = os.path.join(APP_ROOT, "upload\\%s"%filename)
    source = os.path.join(APP_ROOT, 'static\\output\\%s'%filename)
    outputTextFile = os.path.join(APP_ROOT, 'output_ascii_art.txt')
    try:
        if os.path.exists(source):
            os.remove(source)
            os.remove(uploadedImage)
            os.remove(outputTextFile)
            # print('Deleted file : %s' % filename)
        else:
            print("Unable to delete")
        return '200'
    except:
        return '500 : Some Error Occurred...'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.debug = True
    app.run()