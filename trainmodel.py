import time
from azure.cognitiveservices.vision.customvision.training import training_api
project = "e828c5a0-b8e8-4e38-a72f-571930f39d82"
training_key = "f1c36ee94690460290d8d774cd3fe426"
trainer = training_api.TrainingApi(training_key)

def trainmodel(project):
    print ("Training...")
    iteration = trainer.train_project(project)
    while (iteration.status != "Completed"):
        iteration = trainer.get_iteration(project, iteration.id)
        print ("Training status: " + iteration.status)
        time.sleep(1)
    
    # The iteration is now trained. Make it the default project endpoint
    trainer.update_iteration(project, iteration.id, is_default=True)
    print ("Done!")

trainmodel(project)
