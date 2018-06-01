"""
Routes and views for the flask application.
"""
from __future__ import print_function # In python 2.7
from datetime import datetime
from flask import render_template,request,session
from drawingCognitive import app
import sys
import time
import io
import uploadpictures
import logging
import predictionimage
import os
import json

cache ={}
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

@app.route('/last_result',methods = ['POST', 'GET'])
def last_result():
    #if request.method == 'POST':
    tag = request.args.get('tag')
    idfile = request.args.get('idfile')
    print(os.getcwd())
    with open(idfile + 'upload.txt', 'r') as content_file:
        content = content_file.read()
    print (session)
    return render_template("result.html", message=content)
    #try:
    #  message = tag
    #  app.logger.info('va a renderizar')
    #  return render_template("result.html", message=message)
    #except Exception as e:
    #  app.logger.error(str(e))
      #renderingresult = render_template("templates/result.html")
      #print(renderingresult, file=sys.stderr)

@app.route('/last_predict',methods = ['POST', 'GET'])
def last_predict():
    #if request.method == 'POST':
    #tag = request.args.get('tag')
    idfile = request.args.get('idfile')
    #idfile = request.args.get('idfile')
    print(os.getcwd())
    with open(idfile + 'prediction.txt', 'r') as content_file:
        content = content_file.read()
    data = {'chart_data': content}
    app.logger.info(data)
    return render_template("prediction.html", message=data)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   tag = request.args.get('tag')
   idfile = request.args.get('idfile')
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
        mensaje= uploadpictures.runupload(filename,tag,idfile)
        session['msgupload'] = mensaje
   except Exception as e:
        app.logger.error(str(e))

   try:
      message = tag
      app.logger.info('va a renderizar')
      return render_template("result.html", message=message)
   except Exception as e:
      app.logger.error(str(e))
      #renderingresult = render_template("templates/result.html")
      #print(renderingresult, file=sys.stderr)

@app.route('/predict',methods = ['POST', 'GET'])
def predict():
   tag = 'predicition'
   idfile = request.args.get('idfile')
   app.logger.info('Post received with this idfile.' +  idfile)
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
        predictionimage.runprediction(filename,idfile)
   except Exception as e:
        app.logger.error(str(e))

   try:
      #return redirect("http://localhost:5555/prediction.html", code=302)
      return render_template("prediction.html")
   except Exception as inst:
      print(inst.message, file=sys.stderr)
      #renderingresult = render_template("templates/result.html")
      #print(renderingresult, file=sys.stderr)

@app.route('/picture', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))


