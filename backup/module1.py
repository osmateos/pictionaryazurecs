"""
Routes and views for the flask application.
"""
from __future__ import print_function # In python 2.7
from datetime import datetime
from flask import render_template,request
from drawingCognitive import app
import sys
import time
import io
import uploadpictures
import logging

#from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

PATH_TO_TEST_IMAGES_DIR = './images'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'train.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/result',methods = ['POST', 'GET'])
def result():
   tag = request.args.get('tag')
   app.logger.info('Post received with this tag.' +  tag)
   if request.method == 'POST' and len(request.data)>0:
      t = request.data
      app.logger.info('Length file is.' +  str(len(t)))
      #with io.open(fname, "w", encoding="utf-8") as f:
        #fo.write(t)
      #filename = tag + time.strftime("%Y%m%d-%H%M%S") +".jpeg"
   try: 
        filename = tag + time.strftime("%Y%m%d-%H%M%S") +".jpeg" 
        with io.open(filename,"wb") as fo:
            fo.write(t)
        uploadpictures.runupload(filename,tag)
   except Exception as e:
        app.logger.error(str(e))

   try:
      return render_template("result.html")
   except Exception as inst:
      print(inst.message, file=sys.stderr)
      #renderingresult = render_template("templates/result.html")
      #print(renderingresult, file=sys.stderr)


@app.route('/picture', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))



