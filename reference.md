---
layout: page
root: .
---

# Reference

## MLflow MLTF Gateway API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/projects` | `GET` | List available projects |
| `/projects/{id}` | `GET` | Get project details |
| `/runs` | `POST` | Submit a new training run |
| `/runs/{id}` | `GET` | Get run status and results |
| `/runs/{id}/logs` | `GET` | Stream logs for a run |
| `/clusters` | `GET` | List available HPC clusters |
| `/resources` | `GET` | List available resource configurations |

## Common `mltf` client commands

```bash
# Submit a training job
mltf run submit --project my-project --cluster slurm --gpus 1

# Check the status of a run
mltf run status --id <run-id>

# Stream logs from a running job
mltf run logs --id <run-id> --follow

# List available clusters
mltf cluster list

# Cancel a run
mltf run cancel --id <run-id>
```

## Environment variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MLTF_GATEWAY_URL` | Base URL of the gateway server | `https://gateway.example.com` |
| `MLTF_API_TOKEN` | Authentication token | `abc123...` |
| `MLTF_DEFAULT_CLUSTER` | Default cluster to target | `slurm` |

## Further reading

- [MLflow documentation](https://mlflow.org/docs/)
- [SLURM workload manager](https://slurm.schedmd.com/)
