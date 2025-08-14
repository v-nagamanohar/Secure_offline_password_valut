

---
# 🔒 Credential Manager

A simple Python-based Credential Manager that securely stores website login credentials in a local file using Base64 encoding.  
The program allows you to add, view, and (partially) update stored credentials while also checking password strength.

---

## 📌 Features
- Add Credentials: Store website name, username, and password (encoded in Base64).
- View Credentials: Decode and display stored credentials.
- Password Strength Checker: Rates passwords as Weak, Medium, Strong, or Very Strong.
- Update Credentials: (In progress) Will allow modifying saved username or password.
- Secure Storage: Credentials are stored in `vault.txt` in encoded format.

---

## 🛠 How It Works
1. Encoding & Decoding
   - Passwords and credentials are encoded using Base64 before saving.
   - On viewing, they are decoded and displayed in plain text.

2. Password Strength Algorithm
   - Checks for:
     - Minimum length (≥ 8 characters)
     - Uppercase letters
     - Lowercase letters
     - Numbers
     - Special characters (`!@#$%^&().,<>`)
   - Returns: `Weak`, `Medium`, `Strong`, or `Very Strong`.

---

## 📂 File Structure
```

vault.txt        # Stores encoded credentials (auto-created when you save first entry)
your\_script.py   # Main Credential Manager script

````

---

## ▶️ How to Run
1. Save the script as `credential_manager.py`.
2. Open a terminal in the script’s folder.
3. Run:
```bash
python credential_manager.py
````

---

## 📋 Menu Options

When running, the menu shows:

```
🔒 Credential Manager
1. Add Credentials
2. View Credentials
3. Update Credentials
4. Exit
```

---

## 🧩 Example Usage

Adding a credential:

```
Website: gmail.com
Username: myemail@gmail.com
Password: My$ecret123
✅ Credential Saved
```

Viewing credentials:

```
gmail.com | myemail@gmail.com | My$ecret123
```

---

## ⚠️ Notes & Limitations

 The `Update Credentials` feature is partially implemented.
 Base64 encoding is not encryption—it is only an obfuscation method.
 For real-world password security, use encryption libraries like `cryptography`.

---
