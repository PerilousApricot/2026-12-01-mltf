---
title: "Advanced Topics"
teaching: 10
exercises: 0
questions:
- "How do I manage multiple experiments?"
- "What advanced mltf commands are available?"
- "How do I troubleshoot common issues?"
objectives:
- "Manage multiple MLflow experiments"
- "Use advanced CLI commands"
- "Troubleshoot common issues"
keypoints:
- "Organize experiments with directories and naming"
- "Use `mltf delete`, `mltf logout`, and other advanced commands"
- "Check `mltf auth-status` and review job logs for troubleshooting"
---

## Managing Multiple Experiments

### Directory Organization
```bash
experiments/
├── baseline/
│   ├── MLproject
│   ├── python_env.yaml
│   ├── train.py
│   └── gateway_config.json
├── improved-architecture/
│   ├── MLproject
│   ├── python_env.yaml
│   ├── train.py
│   └── gateway_config.json
└── hyperparameter-search/
    ├── MLproject
    ├── python_env.yaml
    ├── train.py
    └── gateway_config.json
```

### Submit Multiple Configurations
```bash
# Run baseline
cd experiments/baseline
mltf submit --name "baseline-v1"

# Run improved architecture
cd ../improved-architecture
mltf submit --name "improved-arch-v1"

# Run different learning rates
for lr in 0.001 0.01 0.1; do
    cd experiments/lr-search
    echo "Submitting with lr=$lr"
    python train.py --lr $lr  # Pass lr as argument
    mltf submit --name "lr-$lr"
done
```

## Advanced CLI Commands

### Delete a Job
```bash
mltf delete <task-id>
```

### Check Authentication
```bash
mltf auth-status
```

### Get MLflow Token
```bash
# For API access
eval $(mltf token)
```

### List All Jobs (Including Completed)
```bash
mltf list --all
```

### View Job Logs
```bash
mltf show <task-id> --show-logs
```

## MLflow API Access

```python
from mlflow.tracking import MlflowClient

# Set tracking URI and token
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://mlflow-test.mltf.k8s.accre.vanderbilt.edu"
os.environ["MLFLOW_TRACKING_TOKEN"] = "<your-token>"

client = MlflowClient()

# List runs
runs = client.search_runs(["0"])
for run in runs:
    print(f"Run ID: {run.info.run_id}")
    print(f"Status: {run.info.status}")
    print(f"Params: {run.data.params}")
    print(f"Metrics: {run.data.metrics}")
```

## Troubleshooting

### Authentication Issues
```bash
# Check status
mltf auth-status

# Re-authenticate
mltf logout
mltf login
```

### Job Stuck in Queue
- Check cluster load
- Reduce resource requests
- Try different partition

### Job Fails to Start
```bash
mltf show <task-id> --show-logs
```
Common issues:
- Invalid Python version in `python_env.yaml`
- Missing dependencies
- Incorrect entry point command

### Cannot Access MLflow UI
- Verify you're using the correct tracking URI
- Check your MLflow token is valid
- Ensure your institutional account has access

### Python Environment Issues
- Use Python versions available on the cluster (3.8, 3.10, 3.11)
- Avoid overly specific dependency versions
- Test environment setup locally first

## Best Practices

1. **Version control your projects** with Git
2. **Log comprehensive metadata** for reproducibility
3. **Use meaningful job names** for identification
4. **Monitor jobs regularly** for errors
5. **Document your experiments** with tags and descriptions
6. **Compare runs systematically** in MLflow UI

## Additional Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [MLflow Projects](https://mlflow.org/docs/latest/ml/projects.html)
- [MLflow Experiment Tracking](https://mlflow.org/docs/latest/tracking.html)
- [SLURM Documentation](https://slurm.schedmd.com/documentation.html)

## Congratulations!

You've completed the MLflow MLTF Gateway tutorial. You can now:
- Install and configure the client
- Authenticate with institutional credentials
- Create MLflow Projects
- Configure compute resources
- Submit and monitor training jobs
- View results and artifacts

Happy machine learning! 🚀

{% include links.md %}