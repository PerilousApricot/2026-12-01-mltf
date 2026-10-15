---
title: "Your First MLflow Project"
teaching: 15
exercises: 0
questions:
- "What is an MLflow Project?"
- "How do I create a project directory structure?"
- "What files are required?"
objectives:
- "Understand the MLflow Project structure"
- "Create the required MLproject and python_env.yaml files"
- "Write a simple training script with MLflow logging"
keypoints:
- "MLflow Projects define how to run your ML code"
- "Three required files: MLproject, python_env.yaml, and your training script"
- "MLflow logs parameters, metrics, and artifacts automatically"
---

## What is an MLflow Project?

An MLflow Project is a directory containing:
- Your ML training code
- Dependencies specification
- Entry point definitions

The project is packaged and sent to the cluster, where MLflow handles environment setup and execution.

## Step 1: Create the Project Directory

Create a new directory for your project:

```bash
mkdir my-ml-project
cd my-ml-project
```

## Step 2: Create the MLproject File

Create a file called `MLproject` (note: no file extension):

```yaml
name: My First ML Project

python_env: python_env.yaml

entry_points:
  main:
    command: "python train.py"
```

**What this does:**
- `name`: Human-readable project name
- `python_env`: Points to your dependencies file
- `entry_points`: Defines how to run your code (`main` is the default entry point)

## Step 3: Create the Python Environment File

Create `python_env.yaml`:

```yaml
python: "3.10.4"
dependencies:
  - mlflow-skinny
  - numpy
  - pandas
```

**Important notes:**
- Use a Python version available on the cluster (3.8, 3.10, or 3.11 are common)
- `mlflow-skinny` provides MLflow functionality without the full tracking UI
- List all dependencies your training script requires

## Step 4: Write Your Training Script

Create `train.py`:

```python
#!/usr/bin/env python3
import numpy as np
import mlflow

print("Hello from MLTF Gateway!")

# Log parameters (input settings)
mlflow.log_param("learning_rate", 0.001)
mlflow.log_param("epochs", 10)
mlflow.log_param("batch_size", 32)

# Simulate training loop
for epoch in range(10):
    # Fake training computation
    loss = 1.0 / (epoch + 1)
    accuracy = 1.0 - loss

    # Log metrics at each epoch
    mlflow.log_metric("loss", loss, step=epoch)
    mlflow.log_metric("accuracy", accuracy, step=epoch)

    print(f"Epoch {epoch+1}: loss={loss:.4f}, accuracy={accuracy:.4f}")

# Save some "model" data as an artifact
with open("model_info.txt", "w") as f:
    f.write("Training complete!\n")
    f.write(f"Final accuracy: {accuracy:.4f}\n")

# Log the artifact
mlflow.log_artifact("model_info.txt")

print("Training complete!")
```

## Understanding MLflow Logging

Your training script uses three types of MLflow logging:

### Parameters (`log_param`)
Input settings you want to track:
```python
mlflow.log_param("learning_rate", 0.001)
mlflow.log_param("batch_size", 32)
```

### Metrics (`log_metric`)
Numerical results you want to compare across runs:
```python
mlflow.log_metric("loss", 0.45, step=epoch)
mlflow.log_metric("accuracy", 0.92, step=epoch)
```

### Artifacts (`log_artifact`)
Files you want to store (models, images, logs):
```python
mlflow.log_artifact("model.pth")
mlflow.log_artifact("training.log")
```

## Verify Your Project Structure

Your project directory should look like this:

```
my-ml-project/
├── MLproject
├── python_env.yaml
└── train.py
```

Check with:

```bash
ls -la
```

## Using the Demo Project (Alternative)

Instead of creating your own project, you can use the demo project included with the MLTF Gateway repository:

```bash
# Clone or navigate to the repository
cd path/to/mltf-gateway
cd demo/demo-cpu
```

This project is already configured and ready to submit.

## Next Steps

Your MLflow Project is now ready to submit! In the next episode, you'll learn about resource configuration, which allows you to specify the compute resources your job needs.

{% include links.md %}