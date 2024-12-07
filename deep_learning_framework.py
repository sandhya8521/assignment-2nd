# -*- coding: utf-8 -*-
"""deep learning framework.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VDqpN3RnPVX5RSOInEBlaFLsYtOfwJIz

1.)What is TensorFlow 2.0, and how is it different from TensorFlow 1.x?

ANS

TensorFlow 2.0 is a major release of the TensorFlow library that introduced significant improvements in usability, scalability, and performance compared to TensorFlow 1.x. It was designed to make TensorFlow easier to use, more intuitive, and better aligned with modern deep learning workflows.

Key Features of TensorFlow 2.0

1.Eager Execution (Default):
*  Eager execution allows for immediate evaluation of operations and easier debugging.
*   In TensorFlow 1.x, operations are built into a computation graph and executed in a separate session, which can be complex to debug.


TensorFlow 1.x:
"""

x = tf.placeholder(tf.float32)
y = tf.constant(5.0)
z = x + y
with tf.Session() as sess:
    print(sess.run(z, feed_dict={x: 2.0}))

#TensorFlow 2.0:

x = tf.constant(2.0)
y = tf.constant(5.0)
z = x + y
print(z.numpy())

"""2.)How do you install TensorFlow 2.0?

ANS

Installing TensorFlow 2.0 is straightforward and can be done using the Python pip package manager. Below are the steps to install TensorFlow 2.0 on different platforms and environments.


"""

# Install TensorFlow 2.0 Using pip
#Basic Command:

pip install tensorflow

pip install tensorflow==2.0.0

python -c "import tensorflow as tf; print(tf.__version__)"   # verify the installation

pip install tensorflow-gpu    # Install GPU-compatible TensorFlow

import tensorflow as tf       #Verify GPU Availability
print("GPU Available:", tf.config.list_physical_devices('GPU'))

pip install --upgrade pip

""" 3.)What is the primary function of the tf.function in TensorFlow 2.0?

 ANS

 The primary function of tf.function in TensorFlow 2.0 is to optimize and accelerate the execution of TensorFlow code by converting Python functions into a TensorFlow graph. This graph execution improves performance and allows the model to run efficiently on different hardware, such as CPUs, GPUs, and TPUs.

Key Features of tf.function

1.Graph Compilation:

*   Converts a Python function into a TensorFlow computational graph.
*   Graphs enable TensorFlow to perform optimizations like operation fusion and parallel execution.

2.Performance Optimization:
*   Graph execution is faster than eager execution because it minimizes the overhead of Python function calls.
3.Hardware Portability:
*  Once a function is converted to a graph, it can run seamlessly on GPUs, TPUs, or other hardware without modification.
4.Serialization and Deployment:
*   Graphs can be serialized (saved) and deployed in production environments using tools like TensorFlow Serving.











"""

## How to Use tf.function
# You apply the @tf.function decorator to a Python function to convert it into a graph.

import tensorflow as tf

@tf.function
def add_numbers(x, y):
    return x + y

# Call the function
result = add_numbers(tf.constant(2.0), tf.constant(3.0))
print(result)  # Output: 5.0

"""4.) What is the purpose of the Model class in TensorFlow 2.0?

ANS

The Model class in TensorFlow 2.0, part of the tf.keras API, provides a high-level abstraction for defining, training, evaluating, and deploying neural network models. It inherits from Layer and acts as the foundation for custom model creation and more advanced functionality compared to the simpler Sequential API.

Primary Purposes of the Model Class

1.Custom Model Creation:

*   Enables you to define complex architectures beyond the linear stacking of layers (e.g., multi-input, multi-output, or dynamic models).
2.Enhanced Functionality:


* Provides access to additional methods like fit, evaluate, and predict for training and inference.
3.Flexibility:
*   Allows for customization of the forward pass (call method) to implement dynamic behavior.
4.Integration with TensorFlow Ecosystem:
*   Supports TensorBoard, serialization, and deployment.

5.)How do you create a neural network using TensorFlow 2.0?

ANS

Creating a neural network using TensorFlow 2.0 involves defining, compiling, training, and evaluating a model. TensorFlow 2.0 simplifies this process with its Keras API, allowing you to quickly build neural networks for various tasks. Below is a step-by-step guide.

Step-by-Step Guide
"""

pip install tensorflow


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Create a neural network with one hidden layer
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),  # Input layer + hidden layer
    Dense(32, activation='relu'),                    # Hidden layer
    Dense(1, activation='sigmoid')                   # Output layer
])


from tensorflow.keras.layers import Input

inputs = Input(shape=(20,))
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
outputs = Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs, outputs)


model.compile(optimizer='adam',              # Optimizer
              loss='binary_crossentropy',    # Loss function
              metrics=['accuracy'])          # Evaluation metrics

import numpy as np

# Generate synthetic data
X_train = np.random.random((1000, 20))  # 1000 samples, 20 features
y_train = np.random.randint(2, size=(1000, 1))  # Binary labels

X_test = np.random.random((200, 20))   # 200 samples, 20 features
y_test = np.random.randint(2, size=(200, 1))    # Binary labels

"""6.)What is the importance of Tensor Space in TensorFlow?

ANS

In TensorFlow, tensor space refers to the multidimensional structure where data resides in the form of tensors. Tensors are the core building blocks of TensorFlow, representing the input, output, and intermediate states of computations. Understanding tensor space is crucial for working effectively with TensorFlow because it directly influences how data is manipulated, processed, and computed in machine learning and deep learning workflows.

Key Reasons Tensor Space is Important

1. Fundamental Data Representation
*   Definition: Tensors are generalizations of scalars, vectors, and matrices to arbitrary dimensions (rank).
*   Rank 0: Scalar (e.g., 3.14)
*   Rank 1: Vector (e.g., [1.0, 2.0, 3.0])
*   Rank 2: Matrix (e.g., [[1, 2], [3, 4]])

7.)How can TensorBoard be integrated with TensorFlow 2.0?

ANS

TensorBoard is a powerful visualization tool for analyzing and debugging TensorFlow models. It helps monitor metrics like loss and accuracy, visualize the computation graph, and analyze training in real-time. Below is a step-by-step guide to integrating TensorBoard with TensorFlow 2.0.


1. Install TensorBoard
"""

pip install tensorboard   # install tesnorBoard

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard
import datetime

# Define the log directory for storing logs
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# Create the TensorBoard callback
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)


model = Sequential([
    Dense(128, activation='relu', input_shape=(20,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])


# Generate dummy data
import numpy as np
X_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))

X_test = np.random.random((200, 20))
y_test = np.random.randint(2, size=(200, 1))

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), callbacks=[tensorboard_callback])

"""8.) What is the purpose of TensorFlow Playground?

ANS

TensorFlow Playground is an interactive, web-based visualization tool designed to help users understand the fundamental concepts of deep learning. It is a simplified and intuitive environment for experimenting with neural networks, making it ideal for beginners and educational purposes.

Key Objectives of TensorFlow Playground

1. Intuitive Understanding of Neural Networks.
*   Allows users to build and experiment with simple neural networks interactively.
*   Visualizes the effects of adding layers, changing activation functions, or adjusting hyperparameters.

2. Demonstration of Deep Learning Principles
*   Feature representation: How input features transform through layers.
*   Activation functions: How different activations influence learning.
*   Overfitting and underfitting: Visualized through training and testing performance.
3. Experimentation Without Coding
*   No programming skills are required.
*   Users can modify neural network parameters directly in the browser and see results instantly.
4. Visualization of Data and Decision Boundaries
*   Offers clear, graphical representations of how the network learns to classify data.
*   Displays the evolution of decision boundaries during training.

9.)What is Netron, and how is it useful for deep learning models?

ANS

Netron is an open-source viewer for exploring and visualizing machine learning, deep learning, and artificial intelligence models. It supports a wide variety of model formats and provides a graphical interface to inspect the structure and details of a model. Netron is widely used by developers, data scientists, and researchers to understand, debug, and share models.

1. Supports Multiple Model Formats:
*   TensorFlow: .pb, .tflite, .keras, .h5
*   PyTorch: .pt, .pth, .onnx
*   ONNX: .onnx
*   Core ML: .mlmodel
*   Caffe: .caffemodel, .prototxt
*   MXNet: .json
2.Interactive Visualization:

*   Displays the architecture of neural networks, including layers, operations, and data flow.
*   Allows zooming, panning, and detailed inspection of model components.
3.Model Information:
*   Provides metadata such as input/output shapes, parameter counts, and layer configurations.
4. Cross-Platform:
*   Available as a standalone application for Windows, macOS, and Linux.
*  Can also be used as a web-based application.

10.)  How do you install PyTorch?

ANS

Installing PyTorch is straightforward and can be done using package managers like pip or conda. The installation process depends on your operating system, Python version, and whether you want to use GPU support (CUDA). Below are the detailed steps:

1. Check Your System Configuration
*   Operating System: Windows, macOS, or Linux.
*   Python Version: Ensure Python 3.7 or higher is installed.
*   GPU Support: If your machine has an NVIDIA GPU, check the CUDA version (nvidia-smi in the terminal).
*   Package Manager: Use pip or conda (if you have Anaconda/Miniconda).
2. Visit the PyTorch Installation Page
*   Go to the official PyTorch installation page to get installation commands specific to your configuration.

11.)What is the basic structure of a PyTorch neural network?

ANS

Basic Structure of a PyTorch Neural Network:-


In PyTorch, a neural network is typically defined as a class that inherits from torch.nn.Module. The basic structure involves defining the layers of the network in the __init__ method and implementing the forward pass in the forward method.

Here’s an overview of the key steps and an example:
1. Key Components

*     torch.nn.Module: Base class for all neural network models.

2.__init__ Method:
*   Define the layers of the model (e.g., fully connected layers, convolutional layers).
3.forward Method:
*   Implement the forward pass, defining how data flows through the layers.
4.Activation Functions:
*   Non-linear transformations like ReLU, Sigmoid, etc.

13.)What is the significance of tensors in PyTorch?

ANS

Significance of Tensors in PyTorch

Tensors are the fundamental data structure in PyTorch and serve as the building blocks for designing and training deep learning models. A tensor is essentially a multidimensional array, similar to a NumPy array, but with additional features tailored for deep learning and numerical computations.


1. Key Features of Tensors

1.Multidimensional Arrays:
*  Tensors can represent scalars (0D), vectors (1D), matrices (2D), or higher-dimensional arrays (ND).
2.Support for GPU Acceleration:
*   Tensors can be moved between CPU and GPU seamlessly.
*   GPU acceleration drastically improves the performance of large-scale computations.
3.Dynamic Computation Graph:
*  PyTorch uses dynamic computation graphs, and tensors are the nodes in these graphs.
2. Importance in Deep Learning

14.)What is the difference between torch.Tensor and torch.cuda.Tensor in PyTorch?

ANS

1. torch.Tensor

Definition: Represents a tensor allocated in the CPU memory by default.

Usage: Suitable for tasks that do not require GPU acceleration.

Advantages:


*   Simpler to use when GPU resources are unavailable.

*   No additional setup or driver installation needed.
"""

import torch

# Create a tensor on the CPU
cpu_tensor = torch.tensor([1.0, 2.0, 3.0])
print("CPU Tensor:", cpu_tensor)
print("Device:", cpu_tensor.device)  # Output: cpu

"""15.)What is the purpose of the torch.optim module in PyTorch?

ANS

Purpose of the torch.optim Module in PyTorch

ANS

The torch.optim module in PyTorch provides a suite of optimization algorithms essential for training machine learning models. It is designed to handle the optimization of model parameters during the training process, enabling models to minimize loss functions efficiently.

Key Functions of torch.optim

1.Parameter Optimization:
*   Adjusts the weights and biases of a model to minimize the loss function.
2.Gradient-Based Optimization:
*   Updates parameters using gradients computed during backpropagation.
*  Incorporates advanced techniques like momentum, learning rate schedules, and adaptive learning rates.
3.Convenience:
*   Provides pre-implemented, efficient optimizers that save time and effort.

17.) What are some common activation functions used in neural networks?

ANS

Common Activation Functions in Neural Networks

Activation functions introduce non-linearity into a neural network, enabling it to learn complex patterns in data. They are applied to the output of each neuron and play a critical role in determining the network's performance and efficiency. Below are some commonly used activation functions, categorized by their characteristics:
"""

import torch
import torch.nn as nn

sigmoid = nn.Sigmoid()
output = sigmoid(torch.tensor([-1.0, 0.0, 1.0]))
print(output)  # Outputs tensor([0.2689, 0.5000, 0.7311])

"""18.)How can you monitor training progress in TensorFlow 2.0?

ANS

Monitoring Training Progress in TensorFlow 2.0

ans

Monitoring the progress of a model during training helps you evaluate performance and adjust hyperparameters. TensorFlow 2.0 provides several tools and techniques for tracking metrics, losses, and other key information during training.

1. Using Built-In Keras Callbacks

Keras callbacks provide hooks into the training process to monitor metrics, log information, and visualize results.

Examples of Useful Callbacks

1.tf.keras.callbacks.EarlyStopping: Stops training when a monitored metric stops improving.
2.tf.keras.callbacks.ModelCheckpoint: Saves the model during training at specific intervals or when performance improves.
3.tf.keras.callbacks.TensorBoard: Logs data for visualization using TensorBoard.





"""

import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Define callbacks
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, verbose=1),  # Stop if no improvement
    ModelCheckpoint('best_model.h5', save_best_only=True, verbose=1)  # Save best model
]

# Train the model with callbacks
history = model.fit(train_data, train_labels,
                    validation_data=(val_data, val_labels),
                    epochs=50,
                    callbacks=callbacks)

"""19. How does the Keras API fit into TensorFlow 2.0?

ANS

Keras is an integral part of TensorFlow 2.0, serving as its high-level API for building and training deep learning models. It simplifies the development process by providing a user-friendly interface while still offering the flexibility and performance of TensorFlow's backend

How Keras Fits into TensorFlow 2.0

1.Integrated API:

*   Keras is included as tf.keras in TensorFlow 2.0.
*   There's no need for separate installation or imports; it works seamlessly within TensorFlow.







"""

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

"""20.What is an example of a deep learning project that can be implemented using TensorFlow 2.02?

ANS

Deep Learning Project: Handwritten Digit Recognition Using TensorFlow 2.0

Project Overview

This project involves building, training, and evaluating a Convolutional Neural Network (CNN) to classify handwritten digits using the popular MNIST dataset. It’s a beginner-friendly project that introduces deep learning concepts like:



*   Data preprocessing
*   Building a CNN
*   Model training and evaluation
*   Visualization of predecitions
"""

#Step-by-Step Implementation

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape data to add a channel dimension (for CNNs)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# One-hot encode the labels (optional for sparse categorical loss)
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # Output layer for 10 classes
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=64,
                    validation_data=(x_test, y_test))


plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Predict on test data
predictions = model.predict(x_test)

# Display some predictions
for i in range(5):
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted: {predictions[i].argmax()}, True: {y_test[i].argmax()}")
    plt.axis('off')
    plt.show()

"""21.)What is the main advantage of using pre-trained models in TensorFlow and PyTorch?

ANS

Advantages of Using Pre-Trained Models in TensorFlow and PyTorch

Pre-trained models are deep learning models that have already been trained on large datasets, such as ImageNet, for tasks like image classification, object detection, or natural language processing. These models are highly valuable for transfer learning.

Main Advantages

1.1. Faster Development and Reduced Training Time
*   Pre-trained models eliminate the need to train from scratch, which can be computationally expensive and time-consuming.
*   You only need to fine-tune the model on your dataset, significantly reducing training time.
2.2. Better Performance with Limited Data
*   Pre-trained models already have learned generalized features (e.g., edges, textures) that can be fine-tuned for specific tasks.
*   This is particularly useful when your dataset is small or lacks diversity.




"""

from tensorflow.keras.applications import MobileNetV2

# Load the pre-trained MobileNetV2 model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze base model layers
base_model.trainable = False

# Add custom layers for fine-tuning
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(10, activation='softmax')  # Adjust output layer for your task
])

"""1.)How do you install and verify that TensorFlow 2.0 was installed successfully?

ANS

Installing TensorFlow 2.0

You can install TensorFlow 2.0 using pip, the Python package manager. Here’s how to do it step-by-step.

1. Prerequisites

Ensure the following are installed:
*   Python (version 3.7 or later)
*   pip (updated to the latest version)





"""

pip install --upgrade pip

pip install tensorflow  # install tensorflow

pip install tensorflow-gpu

import tensorflow as tf

# Print TensorFlow version
print(f"TensorFlow version: {tf.__version__}")

# Check if GPU is available
print("GPU Available: ", tf.config.list_physical_devices('GPU'))

TensorFlow version: 2.x.x
GPU Available: []

TensorFlow version: 2.x.x
GPU Available: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

"""2.)How can you define a simple function in TensorFlow 2.0 to perform addition?

ANS

In TensorFlow 2.0, you can define a simple function to perform addition using either the standard Python function or by leveraging the TensorFlow @tf.function decorator for optimized computation.


"""

# Using a Simple Python Function


import tensorflow as tf

def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(3, 5)
print("Addition Result:", result)

# Using TensorFlow Tensors

import tensorflow as tf

def add_tensors(a, b):
    return tf.add(a, b)

# Example usage with TensorFlow tensors
a = tf.constant(3)
b = tf.constant(5)
result = add_tensors(a, b)
print("Addition Result:", result.numpy())  # Use .numpy() to get the value

"""3.)  How can you create a simple neural network in TensorFlow 2.0 with one hidden layer?

ANS

Here’s how to create a simple neural network in TensorFlow 2.0 with one hidden layer using the Keras API, which is integrated into TensorFlow.


"""

#Step-by-Step Implementation
# import libaries

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Define the model
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),  # Hidden layer with 16 neurons
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

import numpy as np

# Example input data (4 features per sample)
X = np.random.rand(100, 4)  # 100 samples, 4 features
y = np.random.randint(0, 2, 100)  # 100 binary labels (0 or 1)

# Train the model
model.fit(X, y, epochs=10, batch_size=8)

# Example test data
X_test = np.random.rand(20, 4)  # 20 samples, 4 features
y_test = np.random.randint(0, 2, 20)  # 20 binary labels

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")


# Example new data
X_new = np.random.rand(5, 4)  # 5 samples, 4 features

# Predict probabilities
predictions = model.predict(X_new)
print("Predictions:", predictions)

"""4.)How can you visualize the training progress using TensorFlow and Matplotlib?

ANS

You can visualize the training progress in TensorFlow by capturing the metrics (e.g., loss and accuracy) during training and plotting them using Matplotlib. The training progress is logged in the History object returned by the fit method of a TensorFlow model.


"""

# import libaries

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

import numpy as np

# Example input data
X_train = np.random.rand(100, 4)  # 100 samples, 4 features
y_train = np.random.randint(0, 2, 100)  # 100 binary labels

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=8, validation_split=0.2)

print(history.history.keys())  # Outputs: dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

"""5.)How do you install PyTorch and verify the PyTorch installation?

ANS

PyTorch can be installed via pip, conda, or from source. Follow these steps for installation and verification.


"""

# check python version

python --version

# install PYTorch

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

#verify installation

import torch

# Check PyTorch version
print("PyTorch Version:", torch.__version__)

# Check if GPU is available
print("CUDA Available:", torch.cuda.is_available())

# If GPU is available, check the device name
if torch.cuda.is_available():
    print("Device Name:", torch.cuda.get_device_name(0))

"""7.) How do you define a loss function and optimizer in PyTorch?


ANS

In PyTorch, defining a loss function and an optimizer is a key step in training a neural network. Below is a guide on how to define and use them.

1. Define a Loss Function

PyTorch provides several built-in loss functions in the torch.nn module. Some common ones are:

*  Mean Squared Error (MSE): For regression tasks.

*  Cross-Entropy Loss: For classification tasks.

*   Binary Cross-Entropy Loss: For binary classification.
"""

# definig and loss function

import torch.nn as nn

# For regression tasks
loss_function = nn.MSELoss()

# For multi-class classification tasks
loss_function = nn.CrossEntropyLoss()

# For binary classification tasks
loss_function = nn.BCELoss()

import torch.optim as optim

# Assume `model` is your neural network
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Learning rate = 0.01

# Using Adam optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

import torch.optim as optim

# Assume `model` is your neural network
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Learning rate = 0.01

# Using Adam optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)

"""8.) How do you implement a custom loss function in PyTorch?

ANS

Creating a custom loss function in PyTorch can be done in two main ways:

1.Using a Standalone Python Function
2.Subclassing torch.nn.Module

1. Using a Standalone Python Function

If your custom loss function is simple, you can define it as a standard Python function. The function should take the model's outputs and the target labels as inputs and return a scalar tensor representing the loss.


"""

# Mean Absolute Percentage Error (MAPE)

import torch

def custom_loss_function(outputs, targets):
    # Avoid division by zero by adding a small value (epsilon)
    epsilon = 1e-8
    loss = torch.mean(torch.abs((targets - outputs) / (targets + epsilon)))
    return loss

# Example usage
outputs = torch.tensor([2.5, 0.0, 2.1, 8.0])
targets = torch.tensor([3.0, -0.5, 2.0, 7.5])
loss = custom_loss_function(outputs, targets)
print(f"Custom Loss: {loss.item():.4f}")

#Custom Loss Function (Weighted MSE Loss)

import torch.nn as nn

class WeightedMSELoss(nn.Module):
    def __init__(self, weight):
        super(WeightedMSELoss, self).__init__()
        self.weight = weight

    def forward(self, outputs, targets):
        # Weighted MSE loss calculation
        loss = torch.mean(self.weight * (outputs - targets) ** 2)
        return loss

# Example usage
weight = torch.tensor([1.0, 0.5, 2.0, 1.5])
outputs = torch.tensor([2.5, 0.0, 2.1, 8.0])
targets = torch.tensor([3.0, -0.5, 2.0, 7.5])
loss_function = WeightedMSELoss(weight)
loss = loss_function(outputs, targets)
print(f"Custom Loss: {loss.item():.4f}")

"""9)How do you save and load a TensorFlow model?

ANS

Saving and loading models in TensorFlow is crucial for reusing trained models or deploying them. TensorFlow provides multiple ways to save and load models: SavedModel format and HDF5 format. Here's a detailed explanation with examples.

1. SavedModel Format (Recommended)

The SavedModel format is TensorFlow's standard format, which is platform-independent and works across different programming environments.


"""

import tensorflow as tf

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save the model
model.save('saved_model/my_model')

# Load the model
loaded_model = tf.keras.models.load_model('saved_model/my_model')

# Check the model summary
loaded_model.summary()

# Create a sample dataset
import numpy as np

X_train = np.random.rand(100, 4)  # 100 samples, 4 features
y_train = np.random.randint(0, 2, 100)  # Binary labels

# Define a model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=8)

# Save the model
model.save('final_model')

# Load the model
loaded_model = tf.keras.models.load_model('final_model')
print("Model loaded successfully!")