# Heart Failure Prediction

## Project Objective

This project was created as a final project to develop a prediction model of heart failure risk in patients based on existing clinical data. The main purpose of this project is to assist medical personnel and doctors in identifying patients who are at high risk of developing heart failure so that early intervention and treatment can be carried out.

## Background of the Problem

Heart failure is a condition in which the heart cannot pump enough blood to meet the body's needs. It can be caused by a variety of factors, including heart disease, high blood pressure, and kidney disease. Early detection of heart failure risk is essential to reduce mortality and improve patients' quality of life.

## Project Output

The output of this project is a prediction model that can accept a patient's clinical data as input and output a prediction regarding the patient's risk of heart failure. The model will provide a label indicating whether the patient is in a high or low risk category for heart failure.

## Brief Description of Data Used

The data used in this project is taken from BigQuery (SELECT * FROM ftds-hacktiv8-project.phase1_ftds_004_hck.heart-failure) and can be accessed via the following link from Kaggle : [Heart Failure Clinical Data](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data). This dataset contains clinical data from patients who have developed heart failure. Each entry in the dataset includes several features, such as age, gender, blood pressure, serum creatinine level, serum sodium level, and others.

## Methods Used

This project will use machine learning approaches to build prediction models. The methods to be used include:

1. Data preprocessing: Cleaning the data from null and duplicate values, and addressing class imbalance where necessary.
2. Feature extraction: Selecting the most relevant features in heart failure risk prediction.
3. Prediction model: Using machine learning algorithms such as Random Forest, or Ada Boost Classifier (Adaptive Boosting) to train the model with training data and perform prediction on test data.

## Stack Used

In this project, we will use some of the following technologies and tools:

- Programming Language: Python
- Libraries and Frameworks: scikit-learn, pandas, numpy, matplotlib, feature_engine, stats, phik
- Development Environment: Jupyter Notebook

## Brief Explanation of Contents and Purpose of Each File

This project has the following directory and file structure:

- `h8dsft_P1G3_dayuima.csv`: contains the Heart Failure Clinical Data dataset.
- `h8dsft_P1G3_dayuima.ipynb`: A directory containing Jupyter Notebooks with the complete project code, including data pre-processing, feature extraction, and prediction models.

## Project Pros and Cons

The advantages of this project are:

- Can assist medical personnel in identifying patients at risk of heart failure so that early intervention can be carried out.
- Using machine learning techniques to predict the risk of heart failure based on patient clinical data.

The disadvantages of this project are:

- The accuracy of the model can be affected by the characteristics of the data and the complexity of the model used.

### [Deployment](https://huggingface.co/spaces/dayuima01/GC3/tree/main)