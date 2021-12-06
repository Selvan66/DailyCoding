
### Deep Neural Network (DNN)
Deep nets process data in complex ways by employing sophisticated math modeling.
A neural network consists of several connected units called nodes.
These are the smallest part of the neural network and act as the neurons in the human brain. 
When a neuron receives a signal, it triggers a process. 
The signal is passed from one neuron to another based on input received. 
A complex network is formed that learns from feedback.
The nodes are grouped into layers. 
A task is solved by processing the various layers between the input and output layers. 
The greater the number of layers to be processed, the deeper the network, therefore the term, deep learning.

<p align="center">  
  <img width="470" height="300" src="/images/DNN.png">
</p>

#### FaceDetectorDNN

The program uses the [caffe model](https://caffe.berkeleyvision.org/) as a neural network, which consists of two files: 
* [deloy.prototxt](assets/deploy.prototxt) - which describes the model archtecture
* [res10_300x300_ssd_iter_140000_fp16.caffemodel](assets/res10_300x300_ssd_iter_140000_fp16.caffemodel) - is the binary data for the model weights

<p align="center">  
  <img width="470" height="300" src="/images/rickroll2.jpeg">
</p>

### Haar Cascade

Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. 
Then we need to extract features from it.
They are just like our convolutional kernel. 
Each feature is a single value obtained by subtracting sum of pixels under the white rectangle from sum of pixels under the black rectangle.

<p align="center">  
  <img width="470" height="300" src="/images/haar_features.jpeg">
</p>

Now, all possible sizes and locations of each kernel are used to calculate lots of features.
It took a lot of computation, so to solve this problem they introduced the [integral image](https://en.wikipedia.org/wiki/Summed-area_table).
Later, the concept of Cascade of Classifiers group all the features into different stages of classifiers and applied one-by-one. 
Then, from all the calculated features, [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost) matches the best results with our expectations.  


#### FaceDetectorCascade

The program uses pre-trained Haar cascade models to detect objects. The main file used in programs is:
* [haarcascade_frontalface_alt2.xml](assets/haarcascades/haarcascade_frontalface_alt2.xml)

<p align="center">  
  <img width="470" height="300" src="/images/rickroll.jpeg">
</p>

### Building

To build a project, you need to have the [OpenCV](https://github.com/opencv/opencv) library installed on your PC. 

Build this directory
```
mkdir build && cd build
cmake..
cmake --build .
```
Then run
```
./FaceDetector
```
