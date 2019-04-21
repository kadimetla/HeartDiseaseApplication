#!/usr/bin/env python
import os
from flask import Flask, redirect, url_for, request, render_template, send_from_directory
from werkzeug import secure_filename
import heartdisease_diagnosis_using_ML
import sklearn
import pandas as pd




# todo: more pretty interface

# folder to upload pictures
UPLOAD_FOLDER = 'uploads/'
# what files can upload
ALLOWED_EXTENSIONS = set('csv')

# start + config
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']=ALLOWED_EXTENSIONS

# main route
@app.route('/')
def index():
    return render_template('upload.html')

# is file allowed to be uploaded?
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config[ALLOWED_EXTENSIONS]


# file upload route, in browser when you click upload, CSV is coming in
# can put in
@app.route('/upload', methods=['POST'])
def upload():
    print("upload")
    # Get the name of the uploaded file
    file = request.files['file']
    print(file.filename)
    # Check if the file is one of the allowed types/extensions
    if file:
        # remove unsupported chars etc
        filename = secure_filename(file.filename)
        #save path
        save_to=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(save_to)
        print("myout")
        #save file
        file.save(save_to)
        #pass file to model and return bool
        output= heartdisease_diagnosis_using_ML.diagnosis(save_to)
        print(output)
        print("myout")
        #show if photo is a photo of hotdog
        return render_template('result.html', results=output)

#file show route (not using now)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
   app.run(debug=True)