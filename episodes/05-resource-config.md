---
title: "Resource Configuration"
teaching: 10
exercises: 0
questions:
- "How do I request specific compute resources?"
- "What fields can I configure?"
- "How do I configure GPU resources?"
objectives:
- "Understand the gateway_config.json file"
- "Configure CPU-only resource requests"
- "Configure GPU resource requests"
keypoints:
- "Use gateway_config.json to specify resource requirements"
- "Fields include cpus-per-task, mem, time, nodes, partition"
- "GPU requests use the gres field"
---

## Why Configure Resources?

By default, jobs run with modest resource allocations. If your training requires more CPU, memory, or GPU resources, you need to specify this in a `gateway_config.json` file in your project directory.

## Basic Configuration

Create a `gateway_config.json` file in your project directory:

```json
{
  "nodes": 1,
  "cpus-per-task": 2,
  "mem": "4096",
  "time": 120
}
```

## Configuration Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `nodes` | integer | Number of compute nodes | `1` |
| `cpus-per-task` | integer | CPUs per task | `4` |
| `mem` | string | Memory in MB | `"8192"` |
| `time` | integer | Time limit in minutes | `60` |
| `partition` | string | Cluster partition | `"batch"` |
| `account` | string | Chargeback account | `"mltf_acc"` |
| `gres` | string | Generic resources (GPU) | `"gpu:nvidia_rtx_a6000:1"` |

## CPU-Only Configuration

For a CPU-only job with moderate resources:

```json
{
  "nodes": 1,
  "cpus-per-task": 4,
  "mem": "8192",
  "time": 120
}
```

This requests:
- 1 node
- 4 CPU cores
- 8 GB of memory
- Up to 2 hours of runtime

## GPU Configuration

To request GPU resources, use the `gres` field:

```json
{
  "nodes": 1,
  "cpus-per-task": 1,
  "mem": "16384",
  "time": 180,
  "partition": "batch_gpu",
  "account": "mltf_acc",
  "gres": "gpu:nvidia_rtx_a6000:1"
}
```

This requests:
- 1 NVIDIA RTX A6000 GPU
- 1 CPU core
- 16 GB of memory
- Up to 3 hours
- On the `batch_gpu` partition

### GPU Types Available

Common GPU types (varies by cluster):
- `nvidia_rtx_a6000` - High-end workstation GPU
- `nvidia_a100` - Datacenter GPU with 40/80 GB HBM
- `nvidia_v100` - Previous-gen datacenter GPU

Check with your cluster administrator for available GPU types.

## Partition Configuration

Partitions are different queues on the cluster:
- `batch` - Standard batch jobs
- `batch_gpu` - Jobs requiring GPU resources
- `interactive` - Interactive sessions

Your `account` and `partition` values depend on your institution. Contact your cluster admin if you're unsure.

## Time Limits

The `time` field specifies the maximum runtime in minutes:
- Short experiments: 15-30 minutes
- Standard training: 60-240 minutes (1-4 hours)
- Large-scale training: 480+ minutes (8+ hours)

Jobs exceeding the time limit are killed by the scheduler.

## Complete Project with Resources

Your project directory should now look like:

```
my-ml-project/
├── MLproject
├── python_env.yaml
├── train.py
└── gateway_config.json
```

## Troubleshooting

**Job waits in queue for a long time:**
- You may be requesting more resources than available
- Try reducing `cpus-per-task` or `mem`

**Job killed due to OOM (Out of Memory):**
- Increase the `mem` value

**Job killed due to timeout:**
- Increase the `time` value

**"gres" field rejected:**
- Verify the GPU type name with your cluster admin
- Ensure you're using the correct partition

## What's Next?

Your project is fully configured with resource requirements. In the next episode, you'll submit your job to the gateway and learn how to monitor its progress.

{% include links.md %}