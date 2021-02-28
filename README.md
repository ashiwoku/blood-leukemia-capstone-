![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/soft%20histograms.jpg)

# Luekemia Detection using Single Cell Blood Images 
#### By Abolaji Shiwoku 

### Introduction
  Much of a doctor's day is spent reading charts of patients, and deriving a diagnosis based on the patient data they have on hand. With the advent of Machine Learnign and AI, 
models can be trained to recoginize these diseases based on past scans. These tools can be used to lower barriers for entry for many people wihout regular access for doctor 
visits. Images provie the perfect medium for this application as many diagnoses are made by stsudying a patient's MRI or single cell bood slides. This applicaton requires a 
large image dataset: [Image Dataset](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=61080958#61080958171ba531fc374829b21d3647e95f532c), with over 15000 labeled
images amoung 15 image categories.

### Method
  To train a machine learning model, one must choose the form and structure of the model features. Model features are quantitative measures calculated for every observation in the 
dataset. The model will use these calculated measures to learn to predict the desired output. For this model, we generated histogram bins by applying a guassian method to every
pixel image to assign a socre to each bin. To reduce noice, the bins would overlap slightly allowing for a pixel value to influence several bins, and allow for increased 
differentiation among the pictures. Our model will taken in an annotated single cell image, and determine what form of leukemia, if detectable, the patient is diagnosed with. 
Ths method was chosen for its robustness for many diseases across numerous medical image types, and it would alllow for the model builder to see what bins have the most 
imfromation, and which bin is the least useful. This allows for the model to be optimized quick and easy as one sees fit, unlike neaural networks which can be difficult to explain 
to non-technical personnel. The goal of this project is to show that a model with simple features can be a powerful tool in classifying medical images. 

### Exploratory Data Analysis
  The dataset contained 15000 single cell images that had already been labeled and anotated by trained medical personnel. The datset is heavily imbalanced, with the largest category NGS (segmented Neutrophil) containing over 8000 images, the 3 largest categories contained over 11000 images. 
![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/class_dist.png)
The features we weill be constructing will be constructed as follows:
![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/templetae.png)
