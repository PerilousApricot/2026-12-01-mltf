---
title: "Viewing Results"
teaching: 10
exercises: 0
questions:
- "How do I access my job's artifacts?"
- "How do I use the MLflow UI?"
- "How do I compare multiple runs?"
objectives:
- "Retrieve artifacts using `mltf artifacts`"
- "Navigate the MLflow UI"
- "Compare runs and inspect parameters, metrics, and artifacts"
keypoints:
- "Use `mltf artifacts <task-id>` to download job outputs"
- "MLflow UI provides detailed run information"
- "Compare runs to evaluate different configurations"
---

## View Artifacts via CLI

Once your job completes, retrieve its artifacts:

```bash
mltf artifacts <task-id>
```

Output:
```
Artifacts for run <task-id> (MLflow ID: <run-id>):
  model_info.txt (Download URL: https://...)
```

The command provides download URLs for all logged artifacts.

## Access the MLflow UI

The MLflow tracking UI provides a visual interface for exploring your experiments.

### From Submission Output

When you submit a job, you receive an MLflow URL:

```
Find your MLFlow run at https://mlflow-test.mltf.k8s.accre.vanderbilt.edu/#/experiments/0/runs/1d0c6538...
```

Click this URL to view your specific run.

### From MLflow Token

To access the MLflow API directly, get your tracking token:

```bash
eval $(mltf token)
```

This exports the `MLFLOW_TRACKING_TOKEN` environment variable.

## MLflow UI Features

### Experiment Dashboard
- Overview of all runs in an experiment
- Compare runs side-by-side
- Filter by tags, parameters, or metrics

### Run Details
- **Parameters**: Input settings used
- **Metrics**: Numerical results over time
- **Artifacts**: Files generated during the run

### Parameters Tab
View all logged parameters:
```
learning_rate: 0.001
epochs: 10
batch_size: 32
```

### Metrics Tab
Interactive charts of metrics over time:
- Loss curve
- Accuracy curve
- Custom metrics you logged

### Artifacts Tab
Browse and download logged artifacts:
- Model files
- Log files
- Images
- Any other files you logged

## Compare Multiple Runs

Run multiple experiments with different configurations:

```bash
# Run 1: Learning rate 0.001
mltf submit --name "lr-0.001"

# Run 2: Learning rate 0.01
cd experiments/lr-0.01
mltf submit --name "lr-0.01"
```

Then compare results in the MLflow UI:
- Select multiple runs
- View parameter differences
- Compare metric charts

## Best Practices

### Log Comprehensive Information
```python
# Log all relevant parameters
mlflow.log_param("model_type", "resnet50")
mlflow.log_param("dataset", "imagenet")
mlflow.log_param("optimizer", "adam")

# Log metrics at each step
for epoch in range(epochs):
    train_loss = train(model)
    val_loss = evaluate(model)
    mlflow.log_metrics({
        "train_loss": train_loss,
        "val_loss": val_loss
    }, step=epoch)

# Log important artifacts
mlflow.log_artifact("model_final.pth")
mlflow.log_artifact("training_config.json")
```

### Use Tags for Organization
```python
mlflow.set_tag("team", "research")
mlflow.set_tag("project", "image-classification")
mlflow.set_tag("status", "production")
```

### Track Hyperparameter Searches
```python
# Log the search configuration
mlflow.log_param("search_method", "grid_search")
mlflow.log_param("n_trials", 100)

# Log results of each trial
for trial in range(n_trials):
    results = run_experiment(trial_config)
    mlflow.log_metric(f"trial_{trial}_accuracy", results["accuracy"])
```

## What's Next?

You've learned the core workflow of the MLTF Gateway. In the next episode, you'll explore advanced topics including multiple experiments, the MLflow API, and troubleshooting.

{% include links.md %}