# Gender Detection By Facial Features
This project contains a gender detection system that detects genders from realtime video feed and facial features with the help of **Convolutional Neural Network (CNN)**. Furthermore, we can capture the images and respective gender and log them in a csv file.<br>
<br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
<img width="12" />
<img src="https://github.com/opencv/opencv/wiki/logo/OpenCV_logo_no_text.png" height="30" alt="open cv" />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="30" alt="tensorflow logo"  />

## Video Demo

https://github.com/user-attachments/assets/7dad3355-5d21-4691-97d9-b11c13006b23

## Prerequisites
Face images dataset [Face Images](https://www.kaggle.com/datasets/ashwingupta3012/male-and-female-faces-dataset).

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

![Screenshot 2024-10-18 025019](https://github.com/user-attachments/assets/221b3bf7-3f78-4123-9c33-eb8f70720f9e)
![Screenshot 2024-10-18 025103](https://github.com/user-attachments/assets/8bdae2de-e3ee-4df4-9bbb-82e80a807da0)
![Screenshot 2024-10-18 025246](https://github.com/user-attachments/assets/70fe447a-25b8-463b-97ea-858fdb38c913)
