![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/soft%20histograms.jpg)

# Luekemia Detection using Single Cell Blood Images 
#### By Abolaji Shiwoku 

### Introduction
  Much of a doctor's day is spent reading charts of patients, and deriving a diagnosis based on the patient data they have on hand. With the advent of Machine Learning and AI, 
models can be trained to recognize these diseases based on past scans or other patient related data. These tools can be used to lower barriers for access to medical care for many people without regular access for doctor 
visits. Images provide the perfect medium for this application as many diagnoses are made by studying a patient's MRI or single cell blood slides. This application requires a 
large image dataset: [Image Dataset](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=61080958#61080958171ba531fc374829b21d3647e95f532c), with over 15000 labeled
images among 15 image categories. They will be used to train a model to give a patient’s leukemia diagnoses using submitted blood scans. 

### Method
  To train a machine learning model, one must choose the form and structure of the model features. Model features are quantitative measures calculated for every observation in the 
dataset. The model will use these calculated measures to learn to predict the desired output. For this model, we generated histogram bins by applying a gaussian method to every
pixel image to assign a score to each bin. The gaussian method is essentially a normal distribution with a set mean and standard deviation assigned to each bin, and each pixel is assigned a score that represents the probability of getting a pixel value as extreme as the value being tested. 
To reduce noise, the bins would overlap slightly allowing for a pixel value to influence several bins, and allow for increased 
differentiation among the pictures. Our model will take in an annotated single cell image, and determine what form of leukemia, if detectable, the patient is diagnosed with. 
This method was chosen for its robustness for many diseases across numerous medical image types, and it would allow for the model builder to see what bins have the most 
information, and which bin is the least useful. This allows for the model to be optimized quick and easy as one sees fit, unlike neural networks which can be difficult to explain 
to non-technical personnel. The goal of this project is to show that a model with simple features can be a powerful tool in classifying medical images.

### Exploratory Data Analysis
  The dataset contained 15000 single cell images that had already been labeled and annotated by trained medical personnel. The dataset is heavily imbalanced, with the largest category NGS (segmented Neutrophil) containing over 8000 images, the 3 largest categories contained over 11000 images. 
![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/class_dist.png)

### Feature Engineering 
The features we will be using will be constructed as follows:
![](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/templetae.png)

The Gaussian Process is a process in which each pixel is subjected to a gaussian distribution, and its pdf score is calculated, with the mean and standard deviation pre-determined.
The result of this process is 16 features that are distinct between classes and are ready to be supplied to our model. 

![Feature Engineering Notebook](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/feature%20engineering_2%20(3%20colors).ipynb)

Initially, the features were generated using only the pixel intensity values, or the ![gray scale pixels only](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/Feature%20Engineering%20(Gray%20Scale%20Values)).
A later analysis separated the color channels and recalculated the intensity values for each color channel. This increased the number of features per image by three times, providing the model with more data to learn about the image. 

### Model Building and Results
  The issue of imbalance within the datasets was addressed with 2 methods: using **SMOTE (Synthetic Minority Oversampling Technique)** and **applying class weights** to the minority classes. The SMOTE analysis tool from sckit-learn is a tool that generates samples of the minority class by determining the hierarchical sample space and creating values 
for the minority classes from that space. The types of models used were **Logistic Regression** and **Support Vector Machines (SVM)**. The output labels were relabeled using 
dummy variables so that they can be properly input into the model. 

The notebook containing results of the models built with only the grayscale pixel values is ![here](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/Modeling%20.ipynb)

The notebook containing model results for all three-color channels is ![here](https://github.com/ashiwoku/blood-leukemia-capstone-/blob/main/modeling%20with%203%20color%20channels.ipynb)

### Results 
  The model results drastically improved with the implementation of SMOTE analysis, upwards of 20% for the minority classes. The use of all three-color channels allowed for 
the models to differentiate between the classes more easily, and the result could to improve the detection of the smaller classes, up to several hundred original images. After 
top 6 classes, model results were rather poor which is to be expected as the smallest classes contained as little as 11 images, which is not much material for a model to learn a
category. 

## Further Improvements 
- Implement image rotation, blurring, and other image augmentation techniques to improve the minority sample sizes. 
- Use of more powerful machine learning models such as Neural Networks. 
- Increase the number of bins and/or manipulating the mean and standard deviation of the feature bins to get better model performance. 
- Further research of the minority classes could allow for combining classes to reduce the number of classes as well as helping balance the categories. 
- Use a blob detector to generate more features for each image. 

## References
I would not have been able to complete this project without the help of my mentor, Dr. Ankur Argawal. He was very helpful in helping me understand the soft histogram technique
and how to best utilize it for this project. Here is the ![link](https://users.isy.liu.se/en/cvl/perfo/papers/ssab01_pf.pdf) of a paper that provides more information behind this feature engineering technique. I would love to hear feedback of those who discover this project, and what they think of my results at abolajishiwoku@yahoo.com. 

