# -*- coding: utf-8 -*-
"""CNN Architecture.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/139cmfqXnRppWossbUaijc9CQlwzhEX-h

1.)What is a Convolutional Neural Network (CNN), and why is it used for image processing?

ANS

A Convolutional Neural Network (CNN) is a specialized type of deep neural network designed to process structured data, particularly images. CNNs are highly effective at recognizing patterns and features in data like edges, textures, and objects, making them the go-to architecture for image processing and computer vision tasks.

Key Components of CNNs
 1.Convolutional Layers
*  Apply filters (kernels) to the input data to extract features like edges, textures, or patterns.
*   These filters slide (convolve) over the input to produce feature maps.
2.Pooling Layers
*   Downsample the feature maps to reduce spatial dimensions and computational complexity.
*  Max Pooling takes the maximum value in a region, while Average Pooling computes the average.

2.)What are the key components of a CNN architecture?

ANS

The architecture of a Convolutional Neural Network (CNN) is composed of several distinct components, each playing a crucial role in learning and extracting features from images. Here's an overview of the key components:

1. Input Layer
*   Purpose: Accepts the raw data, such as images.
*  Input Format:
  *   For grayscale images: 2D (height × width).
  *  For color images: 3D (height × width × channels, where channels = 3 for RGB).
  
Example: For a 28 × 28 grayscale image, the input shape is (28, 28, 1).

3.) What is the role of the convolutional layer in CNNs?

ANS

The convolutional layer is the fundamental building block of a Convolutional Neural Network (CNN). Its primary role is to automatically extract features from the input data, such as edges, textures, and more complex patterns. It enables the network to learn spatial hierarchies of features from low-level (e.g., edges) to high-level (e.g., objects).

4.)What is a filter (kernel) in CNNs?

ANS

A filter, also called a kernel, is a small matrix of learnable weights used in the convolutional layer of a Convolutional Neural Network (CNN). Filters are applied to the input data (e.g., an image) to extract specific features, such as edges, textures, or patterns.

Key Characteristics of Filters

1.Size (Dimensions):

*   Filters are typically small compared to the input dimensions, such as 3 * 3,5 * 5,7*7
*  For images with multiple channels (e.g., RGB), the filter depth matches the input depth
2.Learnable Parameters:
*   The values in the filter are initially initialized randomly and updated during training through backpropagation to learn meaningful patterns.

5.)What is pooling in CNNs, and why is it important?

ANS

Pooling is a downsampling technique used in Convolutional Neural Networks (CNNs) to reduce the spatial dimensions (width and height) of feature maps while retaining the most important information. It operates independently on each feature map and reduces the computational complexity of the model, making it more efficient and less prone to overfitting.

Key Types of Pooling

1.Max Pooling:
*  Selects the maximum value from each patch of the feature map.
*   Highlights the most prominent feature in the region.
*   Commonly used due to its effectiveness in feature preservation.
2.Average Pooling:
*  Computes the average value of each patch of the feature map.
*   Smoother representation of features.
*   Less commonly used in comparison to max pooling.

6.) What are the common types of pooling used in CNNs?

ANS

Common Types of Pooling Used in CNNs:

Pooling is a key component of CNNs that helps reduce the dimensions of feature maps while retaining important information. The common types of pooling are as follows:

1. Max Pooling
*   Description: Retains the maximum value from each region of the input feature map.
*   Purpose: Captures the most prominent feature in a local region.
*   Advantages:

Focuses on the most significant features.

*  Reduces noise by ignoring lower-intensity values.



  *   Focuses on the most significant features.

8.)What is the role of activation functions in CNNs?

ANS

Role of Activation Functions in CNNs

Activation functions are a critical component of Convolutional Neural Networks (CNNs) and other neural network architectures. Their primary role is to introduce non-linearity into the network, enabling it to learn and model complex patterns in the data. Without activation functions, the network would be a simple linear transformation, limiting its capacity to solve non-linear problems.

Key Roles of Activation Functions in CNNs

1.Introducing Non-Linearity:

*   CNNs perform linear operations such as convolution and pooling.
*   Activation functions add non-linearity, allowing the network to learn more complex patterns like edges, textures, and shapes in images.
2.Mapping Input to Output:
*   Activation functions map input values to a specific range, helping normalize activations and stabilize training.

*   For example, sigmoid maps inputs to the range
[
0
,
1
]
[0,1], making it suitable for probabilistic outputs.

9.)What is the concept of receptive fields in CNNs?

ANS

Concept of Receptive Fields in CNNs

The receptive field in Convolutional Neural Networks (CNNs) refers to the region of the input image that influences a particular feature (activation) in the output feature map. It defines the spatial area of the input that a neuron in a given layer is "looking at" or affected by.

Mathematics of Receptive Fields

The size of the receptive field depends on:


*   Kernel size: The dimensions of the convolutional filter.


*   Stride: The step size when sliding the filter over the input.

*   Padding: Adds borders to the input, allowing filters to process edges and corners.



*   Depth of the layer: Receptive fields grow with depth because each layer combines information from the previous layer's receptive field.

10.)Explain the concept of tensor space in CNNs?

ANS

Concept of Tensor Space in CNNs

In the context of Convolutional Neural Networks (CNNs), a tensor space refers to the multidimensional data structure that represents various transformations and feature maps throughout the network. It is where the input data, intermediate activations, and learned features are stored and processed.

What Is a Tensor in CNNs?

A tensor is a generalization of scalars, vectors, and matrices to higher dimensions:

*   0D Tensor: Scalar (e.g., a single number).
*   1D Tensor: Vector (e.g., a list of numbers).
*  2D Tensor: Matrix (e.g., an image with height and width).
*   3D Tensor: Volume or a stack of matrices (e.g., RGB image with height, width, and color channels).

11.)What is LeNet-5, and how does it contribute to the development of CNNs?

ANS

LeNet-5: An Overview:-

LeNet-5 is one of the earliest Convolutional Neural Networks (CNNs), introduced by Yann LeCun et al. in 1998. It was designed for handwritten digit recognition and became a foundational architecture in the field of deep learning. It demonstrated the power of CNNs for image classification tasks, particularly with structured data like grayscale images.

Key Contributions of LeNet-5
1.Introduction of Convolutional Layers:

*   Highlighted how convolutional layers can extract local patterns and features (edges, shapes) from images.
2.Pooling for Dimensionality Reduction:
*   Showcased the use of pooling layers to reduce computational complexity and introduce translational invariance.
3.Parameter Sharing:
*   Demonstrated how parameter sharing in convolutional layers reduces the number of learnable parameters compared to fully connected layers.
4.Feature Hierarchy:
*   Leveraged hierarchical feature extraction, with early layers capturing basic features (e.g., edges) and deeper layers learning more abstract representations.

13.)What is VGGNet, and how does it differ from AlexNet?

ANS

VGGNet: Overview

VGGNet (Visual Geometry Group Network) is a Convolutional Neural Network (CNN) architecture introduced by Karen Simonyan and Andrew Zisserman in 2014. The network was designed to improve image classification performance by increasing the depth of the network while maintaining simplicity in its design.

VGGNet became popular due to its uniform architecture and exceptional performance in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2014, where it achieved second place. It is characterized by its deep and straightforward architecture, consisting of sequential 3 × 3 convolutional layers, ReLU activations, and max-pooling layers.

Key Characteristics of VGGNet
1.Depth:
*   VGGNet explores deeper networks (16 and 19 layers in its most popular versions, called VGG-16 and VGG-19).
2.Small Convolution Filters:
*   Uses
3
×
3
3×3 filters exclusively, allowing smaller receptive fields and capturing fine-grained features while keeping computational efficiency.

15.)What is ResNet, and what problem does it solve?

ANS

ResNet (Residual Network): Overview

ResNet, introduced by Kaiming He et al. in 2015, is a deep Convolutional Neural Network (CNN) architecture designed to address the vanishing gradient problem and facilitate the training of very deep networks. ResNet was a groundbreaking development in deep learning and won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) 2015 by achieving remarkable accuracy.

Key Problem Solved: Vanishing Gradient in Deep Networks

1.Vanishing Gradient Problem:
*   As networks become deeper, gradients tend to diminish during backpropagation, leading to weights not being updated effectively. This limits the depth of trainable networks and negatively impacts performance.
2.Degradation Problem:
*   Simply stacking more layers in a deep network does not always improve performance. Instead, accuracy often saturates and can degrade as the network depth increases.

16.)What is DenseNet, and how does it differ from ResNet?

ANS

DenseNet (Densely Connected Convolutional Networks): Overview

DenseNet, introduced by Gao Huang et al. in 2017, is a deep learning architecture that builds on the idea of residual learning (as in ResNet) but takes it a step further. Instead of using skip connections between blocks, DenseNet introduces dense connections, where each layer is connected to every other layer in a feed-forward fashion.

Key Idea: Dense Connections
1.Each layer receives the feature maps from all preceding layers as input.
2.Each layer passes its own feature maps to all subsequent layers.

17.) What are the main steps involved in training a CNN from scratch?

ANS

Training a Convolutional Neural Network (CNN) from scratch involves several key steps. Here’s a step-by-step overview of the process:

1. Data Collection and Preprocessing
*   Data Collection: Gather the dataset for training the model. This can be an existing dataset (e.g., CIFAR-10, MNIST, ImageNet) or a custom dataset of images.
"""

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

"""1.) Implement a basic convolution operation using a filter and a 5x5 image (matrix)?

ANS

To implement a basic convolution operation manually, let's consider a 5x5 image and a 3x3 filter (kernel). The process involves sliding the filter across the image, computing the dot product at each position, and producing a feature map.


"""

# python code impletation


import numpy as np

# Define the image (5x5)
image = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Define the filter (3x3)
filter = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

# Get the dimensions of the image and filter
image_height, image_width = image.shape
filter_height, filter_width = filter.shape

# Output dimensions (assuming stride = 1 and no padding)
output_height = image_height - filter_height + 1
output_width = image_width - filter_width + 1

# Initialize an empty output feature map
output = np.zeros((output_height, output_width))

# Perform convolution
for i in range(output_height):
    for j in range(output_width):
        # Extract the region of interest from the image
        region = image[i:i+filter_height, j:j+filter_width]

        # Perform element-wise multiplication and sum the result
        output[i, j] = np.sum(region * filter)

# Print the output feature map
print("Output Feature Map (3x3):")
print(output)

"""2.Implement max pooling on a 4x4 feature map with a 2x2 window?

ANS

To implement max pooling on a 4x4 feature map with a 2x2 window (stride = 2), we need to apply the following steps:


"""

#python code Implementation:

import numpy as np

# Define the 4x4 feature map
feature_map = np.array([
    [1, 3, 2, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Define the pooling window size (2x2) and stride (2)
window_size = 2
stride = 2

# Output dimensions (assuming no padding and stride=2)
output_height = (feature_map.shape[0] - window_size) // stride + 1
output_width = (feature_map.shape[1] - window_size) // stride + 1

# Initialize an empty output matrix for max pooling result
output = np.zeros((output_height, output_width))

# Apply max pooling
for i in range(output_height):
    for j in range(output_width):
        # Extract the 2x2 region for max pooling
        region = feature_map[i*stride:i*stride+window_size, j*stride:j*stride+window_size]

        # Perform max pooling operation (find the maximum value in the region)
        output[i, j] = np.max(region)

# Print the result of max pooling
print("Output after Max Pooling (2x2 window, stride 2):")
print(output)

"""4.) Create a simple CNN model with one convolutional layer and a fully connected layer, using random data?

ANS

Here’s how to create a simple Convolutional Neural Network (CNN) model with one convolutional layer and a fully connected layer, using random data in TensorFlow 2.0 and Keras.


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Create random data: 100 samples of 28x28 grayscale images
# The shape will be (100, 28, 28, 1) for 100 images of size 28x28 with 1 channel (grayscale)
X_train = np.random.random((100, 28, 28, 1))

# Create random labels: binary classification (0 or 1) for 100 samples
y_train = np.random.randint(2, size=(100, 1))

# Build the CNN model
model = models.Sequential()

# Add the convolutional layer with 32 filters, 3x3 kernel size, ReLU activation, and 'same' padding
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max pooling layer to downsample the feature map
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten the output to feed into the fully connected layer
model.add(layers.Flatten())

# Add a fully connected (Dense) layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add the output layer for binary classification (1 output neuron with sigmoid activation)
model.add(layers.Dense(1, activation='sigmoid'))

# Compile the model with binary crossentropy loss, Adam optimizer, and accuracy as a metric
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summarize the model architecture
model.summary()

# Train the model on the random data (just for demonstration purposes)
model.fit(X_train, y_train, epochs=5, batch_size=16)

"""5.)Generate a synthetic dataset using random noise and train a simple CNN model on it?

ANS

To train a simple Convolutional Neural Network (CNN) on a synthetic dataset generated using random noise, we'll follow these steps:


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Step 1: Generate the synthetic dataset
# Create random noise images: 1000 samples of 28x28 grayscale images (28, 28, 1)
X_train = np.random.random((1000, 28, 28, 1))

# Create random binary labels: 1000 labels (0 or 1)
y_train = np.random.randint(2, size=(1000, 1))

# Step 2: Define the CNN Model
model = models.Sequential()

# Convolutional Layer: 32 filters, 3x3 kernel, ReLU activation, padding 'same'
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Max Pooling Layer: 2x2 window to downsample the feature map
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from convolutional layers
model.add(layers.Flatten())

# Fully Connected (Dense) Layer: 128 units with ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Output Layer: 1 unit for binary classification with sigmoid activation
model.add(layers.Dense(1, activation='sigmoid'))

# Step 3: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 4: Model summary to see the architecture
model.summary()

# Step 5: Train the model on the synthetic dataset
model.fit(X_train, y_train, epochs=5, batch_size=32)

"""6.) Create a simple CNN using Keras with one convolution layer and a max-pooling layer?

ANS

To create a simple CNN using Keras with one convolutional layer and a max-pooling layer, we can follow the steps outlined below:


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Step 1: Generate synthetic data (random noise for images)
# Let's generate 1000 random 28x28 grayscale images (28x28x1) and binary labels (0 or 1)
X_train = np.random.random((1000, 28, 28, 1))  # 1000 images of size 28x28 with 1 channel
y_train = np.random.randint(2, size=(1000, 1))  # 1000 labels, either 0 or 1

# Step 2: Create the CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, 3x3 kernel, ReLU activation, and 'same' padding
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max-pooling layer with a 2x2 window
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Step 3: Flatten the output from the convolution and pooling layers
model.add(layers.Flatten())

# Add a fully connected (dense) layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add an output layer with 1 unit (binary classification)
model.add(layers.Dense(1, activation='sigmoid'))

# Step 4: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 5: Model summary to show the architecture
model.summary()

# Step 6: Train the model (using random data for demonstration)
model.fit(X_train, y_train, epochs=5, batch_size=32)

"""7.) Write a code to add a fully connected layer after the convolution and max-pooling layers in a CNN?

ANS

To add a fully connected (dense) layer after the convolution and max-pooling layers in a CNN, we need to flatten the output from the convolution and pooling layers before passing it to the dense layer. Here’s how you can modify the previous CNN model to include a fully connected layer after the convolution and max-pooling layers.


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Step 1: Generate synthetic data (random noise for images)
# Let's generate 1000 random 28x28 grayscale images (28x28x1) and binary labels (0 or 1)
X_train = np.random.random((1000, 28, 28, 1))  # 1000 images of size 28x28 with 1 channel
y_train = np.random.randint(2, size=(1000, 1))  # 1000 labels, either 0 or 1

# Step 2: Create the CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, 3x3 kernel, ReLU activation, and 'same' padding
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max-pooling layer with a 2x2 window
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Step 3: Flatten the output from the convolution and pooling layers
model.add(layers.Flatten())

# Add a fully connected (dense) layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add an output layer with 1 unit (binary classification)
model.add(layers.Dense(1, activation='sigmoid'))

# Step 4: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 5: Model summary to show the architecture
model.summary()

# Step 6: Train the model (using random data for demonstration)
model.fit(X_train, y_train, epochs=5, batch_size=32)

"""9.)Write a code to add dropout regularization to a simple CNN mode?

ANS

To add dropout regularization to a simple CNN model, we can insert the Dropout layer after the convolutional or fully connected layers. Dropout helps to prevent overfitting by randomly setting a fraction of the input units to 0 during training, which forces the network to learn more robust features.


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Step 1: Generate synthetic data (random noise for images)
# Let's generate 1000 random 28x28 grayscale images (28x28x1) and binary labels (0 or 1)
X_train = np.random.random((1000, 28, 28, 1))  # 1000 images of size 28x28 with 1 channel
y_train = np.random.randint(2, size=(1000, 1))  # 1000 labels, either 0 or 1

# Step 2: Create the CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, 3x3 kernel, ReLU activation, and 'same' padding
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max-pooling layer with a 2x2 window
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Add a dropout layer with a rate of 0.25 to reduce overfitting
model.add(layers.Dropout(0.25))

# Step 3: Flatten the output from the convolution and pooling layers
model.add(layers.Flatten())

# Add a fully connected (dense) layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add a dropout layer after the dense layer to further regularize the model
model.add(layers.Dropout(0.5))

# Add an output layer with 1 unit (binary classification)
model.add(layers.Dense(1, activation='sigmoid'))

# Step 4: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 5: Model summary to show the architecture
model.summary()

# Step 6: Train the model (using random data for demonstration)
model.fit(X_train, y_train, epochs=5, batch_size=32)

"""10.)Write a code to print the architecture of the VGG16 model in Keras?

ANS

To print the architecture of the VGG16 model in Keras, you can use the VGG16 model from tensorflow.keras.applications and the model.summary() function to display the architecture. Here's the code:



"""

import tensorflow as tf
from tensorflow.keras.applications import VGG16

# Load the VGG16 model pre-trained on ImageNet data (exclude the top fully connected layers)
model = VGG16(weights='imagenet', include_top=True)

# Print the architecture of the model
model.summary()

"""11.)Write a code to plot the accuracy and loss graphs after training a CNN model?

ANS

To plot the accuracy and loss graphs after training a CNN model, you can use the Matplotlib library to visualize the training progress. After training the model, you can access the history of the training process, which contains the loss and accuracy values for each epoch.


"""

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import layers, models

# Step 1: Generate synthetic data (random noise for images)
X_train = np.random.random((1000, 28, 28, 1))  # 1000 grayscale images of size 28x28
y_train = np.random.randint(2, size=(1000, 1))  # Binary labels (0 or 1)

# Step 2: Create a simple CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, 3x3 kernel, and ReLU activation
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max-pooling layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the convolution and pooling layers
model.add(layers.Flatten())

# Add a fully connected layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add an output layer with 1 unit for binary classification
model.add(layers.Dense(1, activation='sigmoid'))

# Step 3: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 4: Train the model and save the training history
history = model.fit(X_train, y_train, epochs=5, batch_size=32)

# Step 5: Plot the accuracy and loss graphs
# Plot Accuracy
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Plot Loss
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.plot(history.history['loss'], label='Train Loss', color='red')
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()

"""12.)Write a code to print the architecture of the ResNet50 model in Keras?

ANS

To print the architecture of the ResNet50 model in Keras, you can use the ResNet50 model from tensorflow.keras.applications and the model.summary() function to display the architecture. Here's the code:


"""

import tensorflow as tf
from tensorflow.keras.applications import ResNet50

# Load the ResNet50 model pre-trained on ImageNet data (include top layers)
model = ResNet50(weights='imagenet', include_top=True)

# Print the architecture of the model
model.summary()

"""13.) Write a code to train a basic CNN model and print the training loss and accuracy after each epoch?

ANS

To train a basic CNN model and print the training loss and accuracy after each epoch, you can define the model, compile it, and use the fit method. By setting the verbose argument to 1, Keras will print the training progress, including the loss and accuracy after each epoch.


"""

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Step 1: Generate synthetic data (random noise for images)
X_train = np.random.random((1000, 28, 28, 1))  # 1000 grayscale images of size 28x28
y_train = np.random.randint(2, size=(1000, 1))  # Binary labels (0 or 1)

# Step 2: Create a simple CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, 3x3 kernel, and ReLU activation
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(28, 28, 1)))

# Add a max-pooling layer
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the convolution and pooling layers
model.add(layers.Flatten())

# Add a fully connected layer with 128 units and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Add an output layer with 1 unit for binary classification
model.add(layers.Dense(1, activation='sigmoid'))

# Step 3: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 4: Train the model and print the training loss and accuracy after each epoch
history = model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=1)

