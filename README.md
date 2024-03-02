# KYC - Know Your Cards

<!--(https://docs.google.com/document/d/15KSVZAqyA_GNhRiiGIvUCIxvTrStHTObt-v6eMBhtZU/edit)-->


Project related to the examination of *AI Lab: Computer Vision and NLP* of the academic year 2022/2023. The project is organized by the following students:

- **Siria Sannino**                $|$  GitHub Profile: [u-siri-ous](https://github.com/u-siri-ous)
- **Christian Bianchi**         $|$  GitHub Profile: [Fascetta](https://github.com/Fascetta)
- **Nicola Mastrorilli**   $|$  GitHub Profile: [MastroCC8](https://github.com/MastroCC8)
- **Leonard Vincent Ramil**        $|$  GitHub Profile: [LeoRamill](https://github.com/LeoRamill)

The program is designed to analyze pictures of Pokemon TCG 1st gen cards. It aims to classify the Pokemon, providing information regarding name, type, abilities, attacks, and any special features or edition indicators, and grade the card’s condition based on the Beckett Grading Services, using Computer Vision technique like bitmask and Convolutional Neural Network


### Codebase Structure
All modules in the codebase were built by our team.

    ├── code                       # code folder contains the main and the three parts of the project: grader, classifier and GUI
      ├── GUI
        ├── GUI.py                 # code of GUI 
        ├── README.md      
      ├── NN
        ├── all_func_pok.ipynb    # file jupyter contains the whole neural network training procedure
        ├── auxNN_func.py         # file python with training, testing, predicting and evaluating functions
        ├── data_loader.py        # file python with data augmentation function
        ├── mainNN.py             # file python to classify the pokemon
        ├── modelsNN.py           # file python with the two models that we have used
        ├── splitting.py          # file python using to split the original dataset 
        ├── pokemonNN.json        # file json with key: number and value: pokemon
        ├── README.md
      ├── grader
        ├── refine.py            # file python to detect the edges of the card with CV technique
        ├── valutator.py         # file python for grading the card with respect to: centering, corners and edges
        ├── README.md
      ├── main.py
    ├── data                       # data folder contains datasets and models 
        ├── datasetNN              # dataset of images splitting in train and validation set for training Neural Network
        ├── datasets               # it contains the files csv and xlsx of the first three expansions of pokemon: base, fossil, jungle
        ├── models                 # models folder contains all pre-trained neural network that we use to classify the pokemon
    ├── images                     # images folder contains testing image card and GUI images
        ├── GUI                    # images using on the GUI 
        ├── grader_test            # images of cards we photographed used to test the grader and NN
        ├── nn_test                # images taken from the internet used to test the NN
    ├── research                   # resarch folder
    └── README.md

## How did we work?

The project is structured in three parts, namely:
- [Grader](/code/grader)
- [Classifier](/code/NN)
- [GUI](/code/GUI)

which are then implemented in a `main.py` file to coexist.
A strong variety of modules and techniques were used to achieve this objective, such as Keras for an easy neural network implementation, OpenCV for the wide range of functions it offers and Tkinter for a clean GUI.


## Installation

### Clone
```bash
git clone https://github.com/LeoRamill/KYC.git $KYC
```

### Install dependencies
The following packages are required to run the application:
```bash
# For GUI
tkinter
PIL
csv
sys

# For Grader
cv2
numpy

# For Neural Network
os 
shutil
tensorflow
keras
sklearn
matplotlib
visualkeras # optional
```


## How to run

1. Go to main.py (`code>main.py`):

2. Go to the function `main()` and add in the list `image_paths` the path of the interested pokemon card

3. You can launch the program only using:
```bash
python -u "./code/main.py"
```
4. Starting the program will open the GUI, you have to select the expansion and click the central button "Know Your Cards"


https://github.com/LeoRamill/KYC/assets/161584956/9ef6ac0f-666b-439f-8236-1604cfcd9451



## Future Developments
In the future, the aims of the project are:
1. To be extended to other popular trading card games, such as Magic The Gathering and Yu-Gi-Oh, by adapting the structure.
2. To be implemented in a mobile version for fast and practical use on the go.


<!--Research: Articles, papers, notes, and references.
Documents: Project proposal, outlines, drafts, and presentations.
Data: Raw data, datasets, spreadsheets, and other data files.
Code: Source code, scripts, and programming-related files.
Images: Visual assets, diagrams, graphs, and images.
Resources: Any additional resources like fonts, templates, or external files.-->

