#!/usr/bin/env python3
"""
GPU-accelerated training example for MLTF Gateway.
Trains a simple neural network on MNIST.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms
import mlflow

# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")

# Log parameters
mlflow.log_param("device", str(device))
mlflow.log_param("lr", 0.001)
mlflow.log_param("epochs", 3)
mlflow.log_param("batch_size", 64)

# Model
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(28 * 28, 10)

    def forward(self, x):
        x = self.flatten(x)
        return self.linear(x)

model = SimpleNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Data
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
train_set = MNIST(root="./data", train=True, download=True, transform=transform)
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)

# Train
model.train()
for epoch in range(3):
    running_loss = 0.0
    correct = 0
    total = 0

    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    accuracy = 100.0 * correct / total
    mlflow.log_metric("loss", running_loss / len(train_loader), step=epoch)
    mlflow.log_metric("accuracy", accuracy, step=epoch)
    print(f"Epoch {epoch+1}: loss={running_loss/len(train_loader):.4f}, acc={accuracy:.2f}%")

# Save model
torch.save(model.state_dict(), "model.pth")
mlflow.log_artifact("model.pth")

print("Training complete!")