---
title: "Introduction to MLTF Gateway"
teaching: 5
exercises: 0
questions:
- "What is the MLflow MLTF Gateway?"
- "What problem does it solve?"
- "How does the architecture work?"
objectives:
- "Understand the purpose of MLTF Gateway"
- "Describe the architecture: Client → Gateway Server → SSAM → SLURM"
- "Know when to use MLTF Gateway vs. local execution"
keypoints:
- "MLTF Gateway enables remote ML training on HPC clusters"
- "The architecture separates client submission from cluster execution"
- "MLflow provides experiment tracking across the entire workflow"
---

## What is MLTF Gateway?

The **MLflow MLTF Gateway** is a remote job submission service that lets you submit machine learning training code to high-performance computing (HPC) clusters. Instead of training on your laptop, your code runs on powerful servers with GPUs, more memory, and faster processors.

### Key Capabilities

- **Remote execution**: Submit MLflow Projects that run on a cluster, not your machine
- **Resource management**: Request specific CPU, GPU, and memory resources
- **Experiment tracking**: All runs are automatically tracked with MLflow
- **Secure authentication**: Uses OIDC with institutional credentials
- **Job monitoring**: Track job status, view logs, and access artifacts

## Architecture Overview

MLTF Gateway uses a three-tier architecture:

```
[Your Machine]        [Gateway Server]       [Cluster]
   Client  ──►          Server           ──►    SSAM    ──►   SLURM
   (mltf)     WAN      (REST API)          LAN   (API)       (Scheduler)
```

1. **MLTF Client** (`mltf` CLI): Runs on your machine. Packages your project and sends it to the gateway.
2. **Gateway Server**: Accepts submissions, validates them, and forwards jobs to the cluster.
3. **SSAM**: A REST API layer that adds logging and authorization on top of SLURM.
4. **SLURM**: The cluster job scheduler that runs your training code.

## Why Use MLTF Gateway?

| Scenario | Without Gateway | With Gateway |
|----------|-----------------|--------------|
| Training large models | Limited by local hardware | Scale to cluster resources |
| Long-running experiments | Tied up your machine | Run in the background remotely |
| Reproducibility | Manual setup each time | MLflow tracks everything |
| Resource allocation | Manual scheduling | Automated via SLURM |
| GPU access | Need local GPU | Request GPU from cluster |

## MLflow Integration

MLflow is an open-source platform for the ML lifecycle. MLTF Gateway integrates with MLflow for:

- **Experiment tracking**: Log parameters, metrics, and artifacts
- **Run comparison**: Compare multiple training runs
- **Artifact management**: Store and retrieve model artifacts
- **Reproducibility**: Reproduce exact training configurations

## What's Next?

In the next episode, you'll install the MLTF Gateway client and configure it for your environment.

{% include links.md %}