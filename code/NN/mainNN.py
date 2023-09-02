from keras.models import load_model
import numpy as np
import cv2
import json
    

def classify_pokemon(test_img, model, scale):
    # dict of pokemon
    with open('code/NN/pokemonNN.json') as f:
        diz_pokemon = json.load(f)
    # Read file
    #test_img = cv2.imread(test_file)
    # Resize the image testing with the input shape of neural network
    test_img = cv2.resize(test_img, scale)
    # change channel of color BGR to RGB
    test_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    # scaling image
    test_img = np.expand_dims(test_img, axis=0)
    test_img = test_img/255
    
    # Loading the model 
    model = load_model(model)
    # Gives the prediction --> probability for each pokemon
    prediction_prob = model.predict(test_img)
    # Gives the pokemon with highest probability
    classes_x=np.argmax(prediction_prob,axis=1)
    # Return name Pokemon
    return diz_pokemon[str(classes_x[0])]