# Secure Admin Login Demo

## Sensitive Data
The application uses:
- Admin username
- Admin password

These are sensitive because unauthorized access could allow control of the system.

## Security Improvements
- Credentials are stored in a separate config file instead of main.py
- This prevents exposing sensitive data in the main logic
- Basic input validation is added

## Why Hard-Coding is Risky
Hard-coding secrets in the main file makes them easy to see and steal, especially if uploaded to GitHub.

## Limitations
- Credentials are still in plain text
- No encryption or hashing is used
- This is only for demonstration purposes

#Purpose
- This application is a simple admin login system that checks username and password. It demonstrates secure handling of sensitive data by loading credentials from a configuration file instead of hard-coding them.