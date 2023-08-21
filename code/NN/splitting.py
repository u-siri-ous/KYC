# Import os to move, modify and create directory for training set and test set
import os
# Import random to generate randomicaly a number
import random
# Import shutil to move the image 
import shutil

#%% ----------------------

#creating test dataset from the training set
def create_ValidationSet(data_path):
    
    # creating train directory 
    train_dir = data_path+"/Pokemon_train"
    os.system("mkdir " +train_dir)

    #moving all folders from root folder to train folder
    os.system("mv " + data_path+"/* " + train_dir+'/')

    val_dir = data_path+"/Pokemon_validation"
    os.system("mkdir " +val_dir)

    #copying all train data to test folder, in order to get same folder structure
    os.system("cp -r "+ train_dir+ "/* " + val_dir+'/')
    #deleting images from sub directories of test folder
    os.system("find " + val_dir + "/ -name '*.*' -type f -delete")

    return "Done we split the dataset into training set and validation set"


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

#%% ----------------------
# UN ALTRO MODO è FARE LO SPLITTING DEL 20%
def create_path(path):
  train_dir = path+"/Pokemon_train"
  test_dir =  path+"/Pokemon_test"
  os.system("mkdir " +train_dir)
  os.system("mkdir " +test_dir)
  return train_dir, test_dir

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