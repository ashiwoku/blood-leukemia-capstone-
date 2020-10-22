import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
##from sklearn.model_selection import train_test_split
import pandas as pd
import random
import pickle

## Load in image folder.
data_directory = 'C:\\Users\\User\\Desktop\\leukemia capstone'
categories = ['BAS','EBO','EOS','KSC','LYA','LYT','MMZ','MOB','MON',
              'MYB','MYO','NGB','NGS','PMB','PMO']

## Turn images into numerical arrays for the CNN model.
data = []
IMG_SIZE = 100
def create_dataset():
    for label in categories:
        path = os.path.join(data_directory,label)
        classification = categories.index(label)
        for image in os.listdir(path):
            try:
                image_array = cv2.imread(os.path.join(path,image))
                image_array = cv2.resize(image_array,(IMG_SIZE,IMG_SIZE))
                data.append([image_array,classification])
            except Exception as e:
                print("Image was a problem {}".format(image))

## Shuffle data and seperate list of classifcation and image data. 
random.shuffle(data)
data_list =[]
label_list=[]
for dt, lb in data:
    data_list.append(dt)
    label_list.append(lb)

data_list = np.array(data_list).reshape(-1,IMG_SIZE,IMG_SIZE,1)

## Save data in its current form for future use. 
pickle_1 = open("data_list.pickle","wb")
pickle.dump(data_list,pickle_1)
pickle_1.close()

pickle_1 = open("label_list.pickle","wb")
pickle.dump(label_list,pickle_1)
pickle_1.close()



            

        
    






