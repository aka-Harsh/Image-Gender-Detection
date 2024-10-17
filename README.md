# Image Gender Detection

🛠️ This project contains a gender detection system that detects genders from realtime video feed and facial features with the help of **Convolutional Neural Network (CNN)**. Furthermore, we can capture the images and respective gender and log them in a csv file.<br>
<br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
<img width="12" />
<img src="https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png" height="26" alt="vscode logo"  />
<img width="12" />
<img src="https://github.com/opencv/opencv/wiki/logo/OpenCV_logo_no_text.png" height="30" alt="open cv" />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="30" alt="tensorflow logo"  />

## Video Demo
🎥 Here you can find a video of the working project.



## Prerequisites
⚠️***Optional: Doing this part is completey optionals as I have provided my pretrained model in the models folder***.<br><br>
Intall the face images dataset to train your model from 👉 [Face Images](https://www.kaggle.com/datasets/ashwingupta3012/male-and-female-faces-dataset).<br><br>
🚨NOTE 1: Extract the zip file and create a **data** folder in your root directory, and in the data folder create 2 more folders named **train** and **validation**.<br>
🚨NOTE 2: Create 2 more folders in both **train** and **validation** folder named **male** and **female** and put images in those folders accordingly.<br>
🚨NOTE 3: Make sure to have a good split of images in **train** and **validation** folder, I used 70% images for **train** and 30% images for **validation**.

## Deployment

To run this project first clone this repository using:

```bash
  git clone https://github.com/aka-Harsh/Image-Gender-Detection.git
```
Locate this repository using terminal and then create a virtual enviroment and activate it:

```bash
  python -m venv venv
  .\venv\Scripts\activate
```
Perform this in your VScode editor to select python intepreter:
```bash
  Select View > Command Palette > Python: Select Interpreter > Enter Interpreter path > venv > Script > python.exe
```

Install all the required packages:
```bash
  pip install -r requirements.txt
```
Train the Models (This will create 3 trained model in your empty models folder):
```bash
  python train_model.py
```

Finally run the app.py file:
```bash
  streamlit run app.py
```


## Project Outlook
<br>
