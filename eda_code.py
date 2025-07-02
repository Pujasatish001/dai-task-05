import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
%matplotlib inline
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
gender_submission = pd.read_csv('gender_submission.csv')
print("Train Data:")
display(train.head())
print("Test Data:")
display(test.head())
print("Gender Submission Data:")
display(gender_submission.head())
