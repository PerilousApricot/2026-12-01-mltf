---
title: "Installation and Configuration"
teaching: 10
exercises: 0
questions:
- "How do I install the MLTF Gateway client?"
- "How do I configure the gateway URI?"
objectives:
- "Install the MLTF Gateway Python package"
- "Configure the MLTF_GATEWAY_URI environment variable"
- "Verify the installation"
keypoints:
- "Install via pip: `pip install mltf-gateway`"
- "Set `MLTF_GATEWAY_URI` to point to your gateway"
- "The CLI tool `mltf` becomes available after installation"
---

## Step 1: Install Python Dependencies

First, ensure you have Python 3.8 or later installed:

```bash
python3 --version
# Should show Python 3.8.x or higher
```

Create a virtual environment (recommended):

```bash
python3 -m venv mltf-env
source mltf-env/bin/activate
```

## Step 2: Install the MLTF Gateway Client

Install the client package via pip:

```bash
pip install mltf-gateway
```

This installs the `mltf` command-line tool. Verify it's available:

```bash
which mltf
# Should show a path like /usr/local/bin/mltf or /path/to/venv/bin/mltf
```

## Step 3: Configure the Gateway URI

Set the environment variable that tells the client where your gateway server is located:

```bash
export MLTF_GATEWAY_URI=https://gw.mltf.vu
```

**For local development only**, if you're running the gateway server locally:

```bash
export MLTF_GATEWAY_URI=http://localhost:5000
```

### Making the Configuration Persistent

To avoid setting this every time you open a terminal, add it to your shell profile:

```bash
# For bash
echo 'export MLTF_GATEWAY_URI=https://gw.mltf.vu' >> ~/.bashrc

# For zsh (default on macOS)
echo 'export MLTF_GATEWAY_URI=https://gw.mltf.vu' >> ~/.zshrc
```

Then reload:

```bash
source ~/.bashrc   # or source ~/.zshrc
```

### Optional Configuration Variables

The following are optional and only needed if you want to override the automatic OIDC discovery:

| Variable | Default | Description |
|----------|---------|-------------|
| `MLTF_CLIENT_ID` | Auto-discovered | OAuth client ID |
| `MLTF_AUTH_URL` | Auto-discovered | Authorization endpoint |
| `MLTF_TOKEN_URL` | Auto-discovered | Token endpoint |
| `MLTF_SCOPES` | `openid email profile` | OAuth scopes |
| `MLTF_KEYRING_PASSWORD` | Prompt | Cache password for keyring |

For most users, only `MLTF_GATEWAY_URI` is needed.

## Step 4: Verify Installation

Check that the client is properly installed and configured:

```bash
mltf --help
```

You should see the CLI help text listing all available commands.

### Test the Connection

Before authenticating, verify the gateway is reachable:

```bash
curl -s -o /dev/null -w "%{http_code}" $MLTF_GATEWAY_URI/api/config
# Should return 200
```

## Troubleshooting

**`pip` not found:** Install pip first:
```bash
# On Ubuntu/Debian
sudo apt-get install python3-pip

# On macOS with Homebrew
brew install pipx
pipx install mltf-gateway
```

**Permission errors:** Use `--user` flag:
```bash
pip install --user mltf-gateway
```

**`mltf` command not found after installation:** Add the user bin directory to your PATH:
```bash
export PATH=$PATH:~/.local/bin
```

## What's Next?

In the next episode, you'll authenticate with the gateway using your institutional credentials.

{% include links.md %}