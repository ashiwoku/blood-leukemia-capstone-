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

### Feature Engineering 
The features we weill be constructing will be constructed as follows:
![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/templetae.png)

The Guassian Process is a process in which each pixel is subjected to a guassian distribution and its pdf score is calculated, with the mean and standard deviation pre-determined.
The result of this process is 16 features that are distinct between classes, and are ready to be supplied to our model. 

![Feature Engineering Notebook](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/feature%20engineering_2%20(3%20colors).ipynb)

Initialy, the features were generated using only the pixel intensity values, or the ![gray scale pixels only](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/Feature%20Engineering%20(Gray%20Scale%20Values)). 

### Model Building and Results
  The issue of imbalance within the datasets was addressed with 2 methods: using **SMOTE (Synthetic Minority Oversampling Technique)** and **applying class weights** to the minority classes.The SMOTE analysis tool from sckit-learn is a tool that generates sampels of the minority class by determining the heirarcheal sample space and creating values 
for the minorty classes from that space. The types of models used were **Logistic Regression** and **Support Vector Machines (SVM)**. The output labels were relabeled using 
dummy variables so that they can be properly input into the model. 

The notebook containing results of the models built with only the grayscale pixel values is ![here](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/Modeling%20.ipynb)

The notebook containing model results for all three color channels is ![here](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/modeling%20with%203%20color%20channels.ipynb)

### Results 
  The model results drastically improved with the implentation of SMOTE analysis, upwards of 20% for the minority classes. The use of all three color channels allowed for 
the models to differentiate between the classes more easily, and the reulst could to impove the detection of the smaller classes, up to several hundred original images. After 
top 6 classes, model results were rather poor which is to be expected as the smallest classes contained as little as 11 images, whic is not much material for a model to learn a
category. 

## Further Improvements 
- Implement image rotation, blurring, and other image augmentation techniques to improve the minority sample sizes. 
- Use of more powerful machine learning models such as Neural Networks. 
- Increase the nummber of bins and/or manipulating the mean and standrad deviation of the feature bins to get better model performance. 
- Further reasearch of the minority classes coud allow for combining classes to redce the number of classes as well as helping balance the categories. 
- Use a blob detector 

## References
I would not have been able to complete this porject without the help of my mentor, Dr. Ankur Argawal. He was very helpful in helping me understand the soft histogram technique
and how to best utilise it for this project. Here is the ![link](https://users.isy.liu.se/en/cvl/perfo/papers/ssab01_pf.pdf) of a paper that provides more information behind this feature engineering technique. I would love to hear feedback of those who discover this project, and what they thik of my results at abolajishiwoku@yahoo.com. 

