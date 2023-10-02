# Diabetes Prediction Using Random Forest

## Overview

This project aims to predict the likelihood of a person having diabetes using a Random Forest machine learning model. The Random Forest algorithm is used to analyze a dataset containing various health-related features to make predictions about diabetes status.

see my Diabetes Prediction website : https://diabetesprediction-rsk40.streamlit.app

## Technologies used      

1. Python

2. Numpy

3. Pandas

4. scikit-learn

5. Streamlit

## Table of Contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)

## Dataset

The dataset used for this project is downloaded from kaggle , which contains 100000 samples with 9 features. The target variable is whether the individual has diabetes (1 for yes, 0 for no).

You can download the dataset from https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset or use your own dataset by following the format mentioned in the data preprocessing section of the code.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook or Python script:

   ```bash
   jupyter notebook diabetes_prediction.ipynb
   ```

   or

   ```bash
   python diabetes_prediction.py
   ```

## Usage

- **Training the Model:** You can train the Random Forest model by running the provided Jupyter notebook or Python script. Make sure to provide the dataset or update the data loading code if you're using a different dataset.

- **Predicting Diabetes Status:** After training the model, you can make predictions on new data by calling the appropriate functions or methods. Check the code comments and documentation for guidance on using the model for predictions.

## Methodology

In this project, we used the following steps:

1. Data Preprocessing: Cleaned and preprocessed the dataset, handling missing values and feature scaling as needed.

2. Model Selection: Chose the Random Forest algorithm as it is well-suited for classification tasks like predicting diabetes.

3. Model Training: Split the dataset into training and testing sets, and trained the Random Forest model on the training data.

4. Model Evaluation: Evaluated the model's performance using various metrics such as accuracy, precision, recall, and F1-score.

5. Hyperparameter Tuning (optional): Fine-tuned the model by optimizing hyperparameters for better performance.

## Results

Our Random Forest model achieved the following results on the test dataset:
- Accuracy is : 97.0003

These results indicate that the model performs well in predicting diabetes status.

## Contact

If you have any questions or suggestions, please feel free to contact us at rsudheerkumar40@gmail.com 

