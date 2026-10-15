#!/usr/bin/env python3
"""
Simple ML training example for MLTF Gateway.
Trains a linear regression model on synthetic data.
"""

import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Log parameters
mlflow.log_param("n_samples", 1000)
mlflow.log_param("n_features", 5)
mlflow.log_param("noise", 1.0)
mlflow.log_param("test_size", 0.2)

# Generate synthetic data
np.random.seed(42)
X = np.random.randn(1000, 5)
y = X[:, 0] + 2 * X[:, 1] + np.random.randn(1000)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

mlflow.log_metric("mse", mse)
mlflow.log_metric("r2", r2)

# Log model
mlflow.sklearn.log_model(model, "model")

print(f"MSE: {mse:.4f}")
print(f"R2: {r2:.4f}")
print("Training complete!")