# -*- coding: utf-8 -*-
"""CW Q2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A3cS9UCyFh4Ix1DdvluVm-qdWtzNTRN4

## Neural Network Approach
In this notebook, we implement a neural network method to detect fraudulent transactions in the dataset.  

### Objectives:
1. Build and train a feed-forward neural network using TensorFlow/Keras.
2. Evaluate the model using key metrics accuracy, precision, recall, F1-score, and ROC-AUC.

The dataset is mixed, so we address this issue by using SMOTE to oversample the minority class.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import kagglehub
import os

#Download Dataset
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
print("Dataset downloaded to:", path)

# File path to the dataset
file_path = f"{path}/creditcard.csv"

# Verify that the file exists
if not os.path.exists(file_path):
    print(f"Data not found at: {file_path}")
else:
    print("Data found")

#  Define our data processing function
def get_data(file_path):
    """
    Load and preprocess the Credit Card Fraud dataset.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        X_train, X_test, y_train, y_test: Preprocessed training and testing data.
    """
    # Load the dataset
    data = pd.read_csv(file_path)
    print(data['Class'].value_counts())  # Check class imbalance


    # Drop irrelivant column and separate features (X) and target (y)
    X = data.drop(columns=['Time', 'Class'])
    y = data['Class']


    # Normalize the 'Amount' column
    scaler = StandardScaler()
    X['Amount'] = scaler.fit_transform(X[['Amount']])


    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


    # Handle class imbalance using SMOTE
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = get_data(file_path)

# Build our Neural Network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Input layer with 64 neurons and ReLU activation
    Dense(32, activation='relu'),  # Hidden layer with 32 neurons and ReLU activation
    Dense(1, activation='sigmoid')  # Output layer with 1 neuron and sigmoid activation (binary classification)
])


# Optimizer Adam is for adaptive learning rate optimization
# loss, Binary Crossentropy is for binary classification problems
# metrics, Accuracy is to track performance during training
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model on the training data split
# epochs, The number of times the model will read the entire
# batch_size, The number of samples processed before updating weights
# verbose, 1 for detailed training progress output
history = model.fit(X_train, y_train, validation_split=0.2, epochs=10, batch_size=32, verbose=1)


#Make our predictions about the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
y_pred_proba = model.predict(X_test).flatten()  # Probabilities
y_pred = (y_pred_proba > 0.5).astype(int)  # Binary predictions

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC Score: {roc_auc:.4f}")

"""## visual reprentation of our graph"""

# Confusion Matrix heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Non-Fraud", "Fraud"], yticklabels=["Non-Fraud", "Fraud"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"Neural Network (AUC = {roc_auc:.4f})")
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# Accuracy Curves
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()


#Loss Curves
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.tight_layout()
plt.show()

"""## Observations and Insights
1. The model achieves high accuracy and ROC-AUC, indicating good performance in diffrencting between fraudulan and non-fraudulan cases.
2. The training accuracy and validation accuracy converge well, suggesting the model is not overfitting.
3. The use of SMOTE improves recall, ensuring more fraudulent transactions are picked up.
4. Precision remains reasonable, ahowing a manageable number of false positives.

## Comparison with Logistic Regression
1. The neural network outperforms Logistic Regression in terms of:
   - **Recall**: The neural network detects more fraud cases.
   - **ROC-AUC**: The neural network shows better class separation.
2. However, the neural network takes longer to train compared to Logistic Regression.
3. Logistic Regression may still be preferable in cases where simplicity and speed are critical.
"""