from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

import json
import os
# Replace with a valid key
training_key = "f1c36ee94690460290d8d774cd3fe426"
prediction_key = ""
project = "e828c5a0-b8e8-4e38-a72f-571930f39d82"
trainer = training_api.TrainingApi(training_key)

# Create a new project
#print ("Creating project...")
def checkTag(tagname):
    trainer.get_project(project)
    for i in trainer.get_tags(project):
        if tagname == i.name:
            return i.id
    return '0'

def createTag(tagname):
    trainer.get_project(project)
    return trainer.create_tag(project,tagname).id

def CreateOrGet(tagname):
    if checkTag(tagname) == '0':
        return createTag(tagname)
    else:
        return checkTag(tagname)

def uploadimage(picture,tagname):
    #with open(os.fsdecode(picture), mode="rb") as img_data: 
        #v= trainer.create_images_from_data(project, img_data)
    my_tag = CreateOrGet(tagname)
    images_to_upload = []
    with open(picture, mode="rb") as image_contents:
       images_to_upload.append(ImageFileCreateEntry(name=picture, contents=image_contents.read()))
    v = trainer.create_images_from_files(project,images=images_to_upload,tag_ids=[my_tag] )
    return v

def runupload(picture,tag,idfile):
    t = str(uploadimage(picture,tag).is_batch_successful)
    with open(idfile + "upload.txt", "w") as text_file:
        text_file.write(t)
    return (t)

#print (runupload('face.jpeg','face','111') )


