# 🔐 Personal Password Manager

A secure desktop password manager built with Python that lets you store, view, and manage your credentials safely — all data is encrypted before being saved to disk.

## Features

- **Add passwords** — Save website/app credentials (username + password)
- **View saved passwords** — See all stored credentials in a clean table view
- **Copy to clipboard** — Quickly copy a password without exposing it on screen
- **Delete entries** — Remove credentials you no longer need
- **Generate strong passwords** — Create random 16-character secure passwords
- **Encryption at rest** — All passwords are encrypted using the `cryptography` library (Fernet/AES) before being written to disk

## Tech Stack

- **Python 3**
- **Tkinter** — GUI
- **cryptography (Fernet)** — Encryption
- **pyperclip** — Clipboard support

## How It Works

1. On first run, a unique encryption key (`secret.key`) is generated and stored locally
2. All passwords are encrypted using this key before being saved to `passwords.json`
3. Passwords are only decrypted in memory when you view them — never stored as plain text

## How to Run

```bash
# Clone the repository
git clone https://github.com/kulkarniprathamesh97/password-manager.git
cd password-manager

# Install dependencies
pip install cryptography pyperclip

# Run the app
python password_manager.py
```

## Security Note

⚠️ `secret.key` and `passwords.json` are excluded from this repository via `.gitignore` since they contain encryption keys and user-specific encrypted data. These files are generated automatically when you run the app locally.

## Screenshots

*(Add a screenshot of the app here — main window, add password dialog, view passwords table)*

## Future Improvements

- Master password / login screen to access the app
- Password strength indicator while typing
- Search/filter saved passwords
- Export/import encrypted backups

---

Built by [Prathamesh Kulkarni](https://github.com/kulkarniprathamesh97)