import kagglehub

# Download the Credit Card Fraud dataset
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

print("Path to dataset files:", path)
