# Classifier 

The classifier was implemented using Keras, with the aid of Jupyter Notebook. 
[This](https://www.kaggle.com/datasets/lantian773030/pokemonclassification) dataset was taken from Kaggle and adapted to the scope of the project, as some 1^st Pokémons were missing.

In particular, there are around 25 to 50 images for each Pokemon, all with the Pokemon in the centre. Most (if not all) images have relatively high quality (correct labels, centred).

## Pre-Processing Data: Splitting

The dataset was split using two techniques, namely:
- Sampling 15 images from the training set and using them in the validation set, as seen [in this article](https://medium.com/analytics-vidhya/pok%C3%A9mon-classification-974a10621381)

```python
# Copying 15 random images from train folders to test folders
def prep_test_data(pokemon, train_dir, test_dir):
  pop = os.listdir(train_dir+'/'+pokemon)
  test_data=random.sample(pop, 15)
  for f in test_data:
    shutil.copy(train_dir+'/'+pokemon+'/'+f, test_dir+'/'+pokemon+'/')

def loop_prep(train_dir, test_dir):
  #performing samething for each folder in train folder
  for poke in os.listdir(train_dir):
    prep_test_data(poke, train_dir, test_dir)
```
- The 80/20 technique

```python
def splitting(data_path, train_path, test_path, perc):
  
  # folders Pokemon
  fold = sorted(os.listdir(data_path))
  for f in fold:
    # Take the pokemon directory by data_path
    pok_dir = data_path+ f + '/'

    # CREATE POKEMON FOLDER IN THE TEST SET
    if not os.path.isdir(test_path+f):
      os.makedirs(test_path+f)
    pok_file = os.listdir(data_path+f) # list with image of pokemon
  
    # Number of pokemon for the test set
    num_test = round(len(pok_file)* perc)
    # select randomly the image of pokemon for the test set
    img_pok_test = random.sample(pok_file, num_test)

    # We move the image into test set
    for pok_test in img_pok_test:
      shutil.move(pok_dir + pok_test, test_path + f + '/'+ pok_test )

    # CREATE POKEMON FOLDER IN THE TRAIN SET
    if not os.path.isdir(train_path+f):
      os.makedirs(train_path+f)
    
    pok_file = os.listdir(data_path+f) # list with image of pokemon
    # We move the remaining image into train set
    for pok_train in pok_file:
      shutil.move(pok_dir+ pok_train, train_path+f+'/'+pok_train)
      
  return  "Done we split the dataset into training set and validation set"
```
## Pre-Processing Data: Data Augmentation

Data augmentation was implemented to increase the used dataset's size by applying various image transformations, such as rescaling, shear range, horizontal flip and zooming.

```python
def data_load(train_dir, validation_dir, image_size, num_batch):
    # Process Data Augmentation
    datagen=ImageDataGenerator(rescale = 1./255,     # Rescaling factor
                               shear_range=0.2,      # Shear Intensity (Shear angle in counter-clockwise direction in degrees) 
                               zoom_range=0.2,       # Range for random zoom.
                               horizontal_flip=True) # Randomly flip inputs horizontally. 
    
    print('------ Loading TRAIN SET -------')
    training_set=datagen.flow_from_directory(train_dir,
                                         target_size=(image_size[0], image_size[1]),
                                         batch_size=num_batch,
                                         class_mode='categorical',
                                         color_mode='rgb')
    
    print('\n\n------ Loading VALIDATION SET ------')
    validation_set=datagen.flow_from_directory(validation_dir,
                                           target_size=(image_size[0], image_size[1]),
                                           batch_size=num_batch,
                                           class_mode='categorical',
                                           color_mode='rgb')
    return training_set, validation_set

```

## CNN Models

Two CNNs were created to correctly classify the Pokémon, specifically:

1. The first CNN has two Convolutional layers:
  - 64 filters, (5, 5) stride
  - 128 filters, (3, 3) stride

followed by two (2, 2) Max Pooling layers to sharpen the image for the second one and a Flatten layer followed by 151 SoftMax layers to output class. This model uses a 64x64x3 input shape, a ReLU (hidden layers) and SoftMax (output layer) as activation functions, an Adam optimizer and the Categorical Cross Entropy loss function.

```python
#%% ----- MODEL 1 -----
#defining model
def model_1(image_size, num_classes):
    # Reset sezione
    clear_session()
    reset_uids()

    classifier = Sequential()
    classifier.add(Conv2D(64, (5, 5), input_shape=image_size, activation='relu', padding='same'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(num_classes, activation = 'softmax'))
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
    return classifier

```

2. The second CNN is similar, it has three Convolutional layers with the third layer being a duplicate of the second; and an input size of 128x128x3.

```python
#%% ----- MODEL 2 -----
#defining model
def model_2(image_size, num_classes):
    # Reset sezione
    clear_session()
    reset_uids()

    classifier = Sequential()
    classifier.add(Conv2D(64, (5, 5), input_shape=image_size, activation='relu', padding='same'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))

    classifier.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))

    classifier.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    classifier.add(Flatten())
    classifier.add(Dense(num_classes, activation = 'softmax'))
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
    return classifier
```


## Training and hyperparameters

Hyperparameters values for the CNNs were:

1. First
   - 30 epochs
   -  Batch size 32
   -   Learning rate .001

2. Second
   - 20 epochs
   - Batch size 32
   - Learning rate .001

Early stopping was implemented in the training stage to prevent data fitting problems. If the current epoch's loss function is greater than the previous epoch's, training is stopped and the model is saved, generating the .h5 file.

```python
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
```

## Results

```python
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
```

For the first model, a maximum of 96.9% accuracy during training with loss function of 0.11 and 96.7% accuracy on validation with loss function of 0.12 were achieved. For the second model, a maximum of 94% accuracy during training with loss function of 0.21 and 94% accuracy on validation with loss function 0.22 were achieved.
The values for hyperparameters were found useful, regardless of the loss of detailing due to the small scaling of the input image.

<div align="center">

  <img width="619" alt="Screenshot 2024-03-02 alle 21 07 02" src="https://github.com/LeoRamill/KYC/assets/161584956/7ab2b58a-03ec-4372-aaf6-285ec932ca86">
  
</div>




