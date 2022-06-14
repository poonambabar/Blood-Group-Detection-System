from keras.models import Sequential
from keras.models import model_from_json
from sklearn.metrics import classification_report

model_file = open('Data/modelfiles/model.json', 'r')
model = model_file.read()
model_file.close()
model = model_from_json(model)
    # Getting weights
model.load_weights("Data/modelfiles/weights.h5")
#Y = predict(model, X)
import numpy as np

labels =  ['tests']
img_size = 224
import os
import cv2

def get_data(data_dir):
    data = []
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img))[...,::-1] #convert BGR to RGB format
                resized_arr = cv2.resize(img_arr, (img_size, img_size)) # Reshaping images to preferred size
                data.append([resized_arr, class_num])
            except Exception as e:
                print(e)
    return np.array(data)


val = get_data('Data/Test')
x_val = []
y_val = []
for feature, label in val:
  x_val.append(feature)
  y_val.append(label)


x_val = np.array(x_val) / 255
x_val.reshape(-1, img_size, img_size, 1)
y_val = np.array(y_val)

predictions = model.predict(x_val)
#predictions = predictions.reshape(1,-1)[0]
print(predictions)

#print(classification_report(y_val, predictions, target_names = ['ExcuseMe (Class 0)','Hi (Class 1)','Sorry(Class 2)']))