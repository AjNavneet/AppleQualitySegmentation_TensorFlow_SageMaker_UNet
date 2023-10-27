# Fruit Quality Check using Image Segmentation with Amazon SageMaker deployment

## Overview

Amazon SageMaker is a machine learning service that empowers data scientists to train and deploy machine learning models efficiently. It offers an integrated Jupyter authoring notebook instance for data exploration and analysis, as well as streamlined model deployment in a hosted environment, reducing reliance on software engineers.

SageMaker supports data preprocessing, post-processing, feature engineering, and model evaluation. 

---

## Aim

In this project, we will build an image segmentation model using TensorFlow on Amazon SageMaker, utilizing the UNet model architecture.

---

## Tech Stack

- Language: `Python`
- Libraries: `TensorFlow`, `Pandas`, `NumPy`, `Scikit-learn`, `Patchify`, `Matplotlib`, `Segmentation Models`, `Boto3`

---

## Data Description

The dataset contains images of rotten apples with annotated areas of rot. These images will be used to train the model.

---

## Approach

1. Data Loading
2. Data Preprocessing
   - Image Patching
3. Model Building and Training
   - Segmentation model in TensorFlow

4. Model Deployment on Amazon SageMaker

---

## Modular Code Overview

1. **Input**: Contains the data for analysis, including images of rotten apples.
2. **Notebook**: Contains the Jupyter notebook file for the project.
3. **MLPipeline**: A folder with functions placed in different Python files, appropriately named. These functions are called inside the "Engine.py" file.
4. **Sagemaker_Deployment**: Contains files related to deployment.
5. **requirements.txt**: Lists all required libraries with respective versions. Install them using the command `pip install -r requirements.txt`.
6. **Readme.md**: Provides instructions for running the code.

---

## Key Concepts Explored

1. Image segmentation
2. Semantic segmentation and instance segmentation
3. UNet model architecture
4. Notebook instance in SageMaker
5. S3 bucket
6. Patchify the images for segmentation
7. Deploying a model on SageMaker.

---
