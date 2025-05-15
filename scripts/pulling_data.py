import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("radheshyamkollipara/bank-customer-churn")

print("Path to dataset files:", path)

print(type(path))

# download the dataset to csv file
