import tensorflow as tf
from keras.models import load_model
import sys
import numpy as np  
from PIL import Image
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D

# model = sys.argv[1]
# input_dir = sys.argv[2]
# output_dir = sys.argv[3]
# input_shape = (28, 28, 1)

# #build model
# model = Sequential()
# model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
# model.add(Dense(128, activation=tf.nn.relu))
# model.add(Dropout(0.2))
# model.add(Dense(10,activation=tf.nn.softmax))
# model.compile(optimizer='adam', 
#               loss='sparse_categorical_crossentropy', 
#               metrics=['accuracy'])



# #load model weights
# model.load_weights("my_mnist3.h5")
input_dir = sys.argv[1]
output_dir = sys.argv[2]
from keras import backend as K
# This line must be executed before loading Keras model.
K.set_learning_phase(0)
from keras.models import load_model
model = load_model('my_mnist_full.h5')

ref_output = {}
with open(f'{output_dir}\\result.txt') as f:
    lineList = f.readlines()

for a in lineList:
    ref_output[a.split(',')[0]] = a.split(',')[1].strip()

images = {}
for a in range(100):
    images[f'img_{a}.png'] = Image.open(f'{input_dir}\\img_{a}.png')

final_dict = {}
top1_accuracy = 0
for img in images:
    pred = model.predict(np.array(images[img]).astype('float32').reshape(1,28,28,1))
    print (pred.argmax())
    if int(ref_output[img]) == int(pred.argmax()):
        top1_accuracy +=1

print (top1_accuracy/len(images) * 100)