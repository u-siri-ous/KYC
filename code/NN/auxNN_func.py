#from tensorflow import keras
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import load_model
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
import cv2

#%% -------- TRAINING ------------

def train_model(model, train_set, val_set, early_stopping, pat, num_model, num_epochs):
    # Apply early stop --> to predict overfitting case
    es = None
    if early_stopping == True:
        es = EarlyStopping(monitor='val_loss',
                           mode='min', 
                           patience=pat,
                           restore_best_weights = True,
                           verbose=1
                           )
        # Create a File Pre trained
        filepath = "model"+str(num_model)+".h5"
        # Checkpoint of file
        ckpt = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        # Fit the model with respect to training and validation generator
        history = model.fit_generator(generator=train_set, 
                                      validation_data= val_set,
                                      callbacks=[es, ckpt],
                                      epochs = num_epochs )
        
    else:
        filepath = "model"+str(num_model)+".h5"
        # Checkpoint of file
        ckpt = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        # Fit the model with respect to training and validation generator
        history = model.fit_generator(generator=train_set, 
                                      validation_data= val_set,
                                      callbacks=[ckpt],
                                      epochs = num_epochs)
    return history, filepath, es

def eval_model(model, train_set , val_set):
    # Evaluate the Model
    metrics_train = model.evaluate(train_set)
    metrics_val = model.evaluate(val_set)

    print("Train Accuracy = %.4f - Train Loss = %.4f" % (metrics_train[1], metrics_train[0]))
    print("Test Accuracy = %.4f - Test Loss = %.4f" % (metrics_val[1], metrics_val[0]))

#%% -------- ACCURACY AND LOSS FUNCTION ------------
# Define Loss Functions
def loss_function(hist):
    fig = plt.figure()
    plt.plot(hist.history['loss'], color='teal', label='loss')
    plt.plot(hist.history['val_loss'], color='orange', label='val_loss')
    fig.suptitle('Loss', fontsize=20)
    plt.legend(loc="upper left")
    plt.show()

# Define Accuracy Function
def accuracy_function(hist):
    fig = plt.figure()
    plt.plot(hist.history['acc'], color='teal', label='accuracy')
    plt.plot(hist.history['val_acc'], color='orange', label='val_accuracy')
    fig.suptitle('Accuracy', fontsize=20)
    plt.legend(loc="upper left")
    plt.show()

def plot_history(hist):
    loss_function(hist)
    accuracy_function(hist)

#%% -------- MAKE PREDICTION ------------
def make_prediction(model, test_set, model_h5):
    if type(model_h5) == str:
        model = load_model(model_h5)
        prediction_prob = model.predict(test_set)
    else:
        prediction_prob = model.predict(test_set)
    
    # Find the argmax of probabilities and put in the list
    y_pred = [np.argmax(prediction_prob[i]) for i in range(len(prediction_prob))]
    y_pred = np.array(y_pred)

    return y_pred

#%% -------- EVALUATE PREDICTION ------------
def evaluate_prediction(y_test, y_pred, labels):
  
  # Classification report
  cl = classification_report(y_test, y_pred, target_names = labels)
  print('\nClassification Report\n', cl)


#%% -------- TESTING  ------------
def testing(model,
            train_set, 
            scale,
            test_file):
    
    # Dict with key: Number 
    #           value: Pokemon 
    diz={v:k for k,v in train_set.class_indices.items()}

    # Read file
    test_img = cv2.imread(test_file)
    # Resize the image testing with the input shape of neural network
    test_img = cv2.resize(test_img, scale)
    # 
    test_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
    #plt.imshow(test_img)

    #test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    test_img = test_img/255
    #plt.imshow(test_img)

    if type(model) == str:
        model = load_model(model)
        prediction_prob = model.predict(test_img)
    else:
        prediction_prob = model.predict(test_img)
    classes_x=np.argmax(prediction_prob,axis=1)
    #plt.title(diz[classes_x[0]])
    return diz[classes_x[0]]
