# Credit Card Fraud Detection Using Machine Learning

## Overview
This project explores credit card fraud data sets using machine learning techniques. The coursework involves the use of logistic regression, neural networks, and other models, with a focus on feature engineering, data preprocessing, and evaluation metrics.

## Objectives
1. **Preprocess and analyze the dataset** to handle imbalances and normalize features.
2. **Implement and evaluate machine learning models**, including Logistic Regression and Neural Networks.
3. **Explore the impact of training data size and class balancing techniques** (e.g., SMOTE).
4. **Provide detailed documentation and reproducible results**.

## Dataset
- **Source**: [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  

## Experiments
### Q1: Logistic Regression with SMOTE
- **Goal** Use of non-neural netwworking approach to sort the data:
  - Implemented SMOTE to address class imbalance.
  - Evaluated model using classification report, confusion matrix, and ROC-AUC score.

### Q2: Neural Network for Fraud Detection
- **Goal** Use of neural netwworking approach to sort the data:
  - Used Adam optimizer and binary cross-entropy loss.
  - Examined the effect of varying training data sizes.

### Q3: Comparison of Techniques
- **Goal** How does data affect our model:
  - Assessed models based on performance metrics (accuracy, ROC-AUC, etc.).
  - Analyzed the benefits of class balancing using SMOTE.

## Results
- **Logistic Regression**: Good performance but struggled with imbalanced data.
- **Neural Network**: Shown high accuracy and ROC-AUC scores when trained with sufficient data.
- **SMOTE**: Significantly improved model performance for both methods.

## References

1. **Logistic-Regression-with-SMOTE-and-Random-Forest-with-Hyperparameter-Tuning - RPW-11**:  
     [https://github.com/RPW-11/Logistic-Regression-with-SMOTE-and-Random-Forest-with-Hyperparameter-Tuning/tree/main)

2. **Machine Learning using Tensorflow - Aqib Saeed**:
     [https://github.com/aqibsaeed/Tensorflow-ML/tree/master)  

3. **Neural Network Binary Classification - Sesank M **:  
     [https://github.com/sesankm/neural-network-binary-classification)  

4. **Imbalanced Data with SMOTE Techniques - Swastik-25   **:  
     [https://github.com/Swastik-25/Imbalanced-Data-with-SMOTE-Techniques/tree/main?tab=readme-ov-file)

5. **Neural Network for Binary Classification - AusBoone   **:  
     [https://github.com/AusBoone/Neural-Network-Python)

6. **Chatgbt***:  
     [Hwlping with the optimization of code and the use of github)

## Repository Structure
```plaintext
.
├── data/
│   └── creditcard.csv         # Dataset (downloaded from Kaggle)
├── notebooks/
│   ├── q1_logistic_regression.ipynb  # Q1 implementation
│   ├── q2_neural_network.ipynb       # Q2 implementation
│   └── q3_comparison.ipynb           # Q3 analysis
├── src/
│   └── utils.py              # Helper functions for preprocessing and modeling
├── README.md                 # Project documentation
└── CITATIONS.md              # References and acknowledgments

