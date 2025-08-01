# Predicted_package_based_on_your_cgpa

🎓 This project uses machine learning to predict a student's placement package based on their CGPA. It demonstrates the use of `numpy`, `pandas`, `matplotlib`, and `scikit-learn` in a simple regression pipeline.

📌 Project Overview

This project predicts a student's placement package (LPA) based on their CGPA using a simple machine learning model. It demonstrates the use of NumPy, Pandas, Matplotlib, and Scikit-learn.

📊 Pandas: Used to load and process the dataset

🔢 NumPy: Used for numerical operations

📈 Matplotlib: Used to visualize the relationship between CGPA and package

🤖 Scikit-learn: Used to train a regression model that predicts the package

📁 Features

📊 Data Loading and Cleaning (Pandas)

Load the dataset (CSV file) containing CGPA and Package data.
Handle missing values or outliers if any.
Prepare data for analysis and modeling.

🔢Numerical Operations (NumPy)

Use NumPy arrays for efficient data handling.
Perform reshaping and type conversion where needed for model training.
Useful for calculations like mean, variance, etc.

📈Data Visualization (Matplotlib)

Plot CGPA vs. Package using scatter plots.
Add regression lines to visualize prediction trends.
Helps understand the correlation between CGPA and package.

🤖Model Training (Scikit-learn)

Use LinearRegression model to learn the relationship between CGPA and package.
Split data into training and test sets using train_test_split.
Fit the model to training data and predict on test data.

📈Model Evaluation (Scikit-learn)

Evaluate model performance using metrics like:
MAE (Mean Absolute Error)
MSE (Mean Squared Error)
R² Score (to measure how well the model fits the data)

🔢Prediction (Scikit-learn)
Input a CGPA value and get a predicted package.
