---
title: "Submit and Monitor Jobs"
teaching: 10
exercises: 0
questions:
- "How do I submit an MLflow Project to the gateway?"
- "How do I monitor job status?"
- "How do I view job logs?"
objectives:
- "Submit a job using `mltf submit`"
- "Monitor job status with `mltf list` and `mltf show`"
- "View job logs"
keypoints:
- "Submit from your project directory with `mltf submit`"
- "Jobs receive a unique task ID for tracking"
- "Use `mltf list` to see all jobs, `mltf show` for details"
---

## Submit Your Job

Navigate to your project directory and submit the job:

```bash
cd my-ml-project
mltf submit --name "my-first-job"
```

### Expected Output

```
Submitted project to MLTF: 962e168e-a61c-11f0-b4b0-bc2411853964
Find your MLFlow run at https://mlflow-test.mltf.k8s.accre.vanderbilt.edu/#/experiments/0/runs/1d0c653826144357aa90a7de2c6f6bf8
```

The output includes:
- **Task ID**: A unique identifier for your job (used for monitoring)
- **MLflow URL**: Link to the tracking page for this run

### Submit Options

```bash
# Give your job a name (appears in mltf list)
mltf submit --name "baseline-model"

# Specify a different project directory
mltf submit --dir ./experiments/improved --name "improved-model"

# Override the tracking URI (rarely needed)
mltf submit --tracking-uri https://custom-tracker.example.com
```

## Monitor Your Job

### List All Jobs

```bash
mltf list
```

Output:
```
Tasks:
  2025-10-10@16:03:35 - 962e168e-a61c-11f0-b4b0-bc2411853964 (my-first-job)
```

List options:
```bash
# Show all jobs (including completed/failed)
mltf list --all

# Show a specific range
mltf list --start 1 --end 5
```

### Check Job Status

```bash
mltf show <task-id>
```

Or check the most recent job without specifying an ID:

```bash
mltf show
```

Output:
```
Status: RUNNING
```

Possible statuses:
- `PENDING` - Job is waiting in the queue
- `RUNNING` - Job is currently executing
- `COMPLETED` - Job finished successfully
- `FAILED` - Job encountered an error

### View Job Logs

```bash
mltf show <task-id> --show-logs
```

Output:
```
Status: COMPLETED
Name: my-first-job
--- Logs ---
Hello from MLTF Gateway!
Epoch 1: loss=1.0000, accuracy=0.0000
Epoch 2: loss=0.5000, accuracy=0.5000
...
Training complete!
```

## Job Lifecycle

1. **Submit**: You run `mltf submit`
2. **PENDING**: Job is queued on the cluster
3. **RUNNING**: Job starts executing
4. **COMPLETED/FAILED**: Job finishes

Typical wait times:
- Small jobs: Seconds to minutes in queue
- Large jobs: Hours (depends on cluster load)

## Troubleshooting

**"Authentication required" error:**
```bash
mltf login
```

**Job stuck in PENDING for a long time:**
- Cluster may be busy
- Check resource requests in `gateway_config.json`

**Job FAILED:**
```bash
mltf show <task-id> --show-logs
```
Check logs for error messages.

**Can't find task ID:**
```bash
mltf list
```
Use the most recent entry.

## What's Next?

Once your job completes, you'll want to view the results. In the next episode, you'll learn how to access artifacts and use the MLflow UI.

{% include links.md %}