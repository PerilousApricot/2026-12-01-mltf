---
title: "Authentication"
teaching: 10
exercises: 0
questions:
- "How do I log in to the MLTF Gateway?"
- "How does token refresh work?"
objectives:
- "Authenticate using the device flow OAuth"
- "Verify authentication status"
- "Understand token storage and refresh"
keypoints:
- "Use `mltf login` to start the device flow authentication"
- "Tokens are stored securely and refreshed automatically"
- "Use `mltf auth-status` to check your credentials"
---

## Step 1: Initiate Authentication

Log in to the MLTF Gateway using the `mltf login` command:

```bash
mltf login
```

This initiates the OAuth2 **device authorization flow**, which is designed for command-line applications.

## Step 2: Complete the Browser Login

After running `mltf login`, you'll see output similar to this:

```
Initiating OAuth2 authentication...
Visit this link to authorize access to MLTF:
https://keycloak.k8s.accre.vanderbilt.edu/realms/mltf-dual-login/device?user_code=XXXX-XXXX
```

1. **Copy the URL** and paste it into your web browser
2. **Log in** with your institutional credentials (Vanderbilt or CERN)
3. **Approve** the access request
4. Return to your terminal - the `mltf login` command will detect when you've completed the flow

The terminal will show:

```
Waiting for authorization...
Login successful!
```

## Step 3: Verify Authentication

Confirm your authentication status:

```bash
mltf auth-status
```

Expected output:

```
Credentials found, expired? False
Token Subject: <your-user-id>
Token Issuer: https://keycloak.k8s.accre.vanderbilt.edu/realms/mltf-dual-login
Access Token:
       Issued: 2025-10-06 22:23:05+00:00
      Expires: 2025-10-11 22:23:05+00:00
    Remaining: 1 day, 2:43:28
Refresh Token:
       Issued: 2025-10-01 21:15:11+00:00
      Expires: 2025-10-26 20:56:06+00:00
    Remaining: 16 days, 1:16:29
```

## How Token Management Works

### Token Storage
Credentials are stored securely using Python's `keyring` package:
- **macOS**: Keychain
- **Linux**: Secret Service (GNOME Keyring or KWallet)
- **Windows**: Windows Credential Manager
- **Fallback**: Encrypted file with a password

### Automatic Refresh
The client automatically refreshes access tokens when they expire:
- Access tokens are short-lived (typically 5 minutes to 1 hour)
- Refresh tokens are long-lived (typically 7-30 days)
- When an API call fails with an expired token, the client silently refreshes

### Manual Refresh
If you need to re-authenticate (e.g., after logout or token expiry):

```bash
mltf login
```

### Logout
To log out and clear stored credentials:

```bash
mltf logout
```

## Troubleshooting

**"No credentials found" error:**
You haven't logged in yet, or your session expired. Run:
```bash
mltf login
```

**Browser doesn't open automatically:**
Copy the URL manually to your browser. The URL will be displayed in your terminal.

**"Authentication required" when running commands:**
Your token has expired and couldn't be refreshed. Re-authenticate:
```bash
mltf logout
mltf login
```

**Keyring errors:**
If your system's keyring isn't available, the client uses an encrypted file. You may need to enter a password once, or set the `MLTF_KEYRING_PASSWORD` environment variable.

## What's Next?

In the next episode, you'll create your first MLflow Project and prepare it for submission.

{% include links.md %}