from keras.utils import image_dataset_from_directory
from keras.preprocessing.image import ImageDataGenerator
import numpy as np


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


def data_testing(test_dir, image_size, num_batch):
    # Create a generator for the test set
    test_set = image_dataset_from_directory(test_dir,
                                            image_size = image_size,
                                            color_mode = 'rgb',
                                            batch_size = num_batch,
                                            label_mode = 'categorical',
                                            shuffle = False,
                                            seed = 1)
    # labels of the test set
    y_test = np.concatenate([y for x, y in test_set], axis=0)
    y_test = [np.argmax(l) for l in y_test]

    return test_set , y_test