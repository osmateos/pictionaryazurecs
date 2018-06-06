from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models
import json
# Now there is a trained endpoint that can be used to make a prediction
prediction_key = "89b40e9a881243beb1a1e7867d8d519f"
predictor = prediction_endpoint.PredictionEndpoint(prediction_key)



project = "e828c5a0-b8e8-4e38-a72f-571930f39d82"

def predictImage(picture):
    with open(picture, mode="rb") as image_contents:
       results = predictor.predict_image(project, image_contents)
    return results



def runprediction(picture,idfile):
    total=""
    mylist = []
    dicttag={}
    results = predictImage(picture)
    for prediction in results.predictions:
        total = total +  "\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100) + "\n"
        #data[prediction.tag_name]=prediction.probability * 100
        dicttag={}
        dicttag['tag']=prediction.tag_name
        dicttag['value']=prediction.probability * 100
        mylist.append(dicttag)
    with open(idfile + "prediction.txt", "w") as text_file:
        text_file.write(json.dumps(mylist, indent=2))
    return (mylist)

#runprediction('face.jpeg','112')
