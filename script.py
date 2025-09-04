import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the datasets
train_data = pd.read_csv('exoTrain.csv')  # Training dataset
test_data = pd.read_csv('exoTest.csv')   # Testing dataset

# Separate features and labels for training data
X_train = train_data.iloc[:, 1:]  # FLUX.1-FLUX.3197 are in columns 1 to end
y_train = train_data.iloc[:, 0]   # LABEL is in column 0

# Separate features and labels for testing data
X_test = test_data.iloc[:, 1:]  # FLUX.1-FLUX.3197 are in columns 1 to end
y_test = test_data.iloc[:, 0]   # LABEL is in column 0

# Normalize the features
scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

# Train the logistic regression model with increased max_iter
model = LogisticRegression(max_iter=1000) 
model.fit(X_train_normalized, y_train)

# Predict on the test set
y_pred = model.predict(X_test_normalized)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")