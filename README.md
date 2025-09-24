# 🔐 Password Generator (GUI)

This is the English version of the documentation.

👉 [Read the German version](./README.de.md)

A simple and user-friendly tool to generate secure passwords – developed with **Python** and **Tkinter**.

![Preview of the Password Generator](assets/Preview.png)

---

## 📖 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Security Notice](#security-notice)
- [Author](#author)
- [License](#license)

---

## ✨ Features

✅ Customizable password length  
✅ Selection of various character types:
- 🔠 Uppercase letters (A–Z)
- 🔡 Lowercase letters (a–z)
- 🔢 Numbers (0–9)
- 🔣 Special characters (!"§$%&_.,:;)
- ➕ Mathematical symbols (+ - * /)
- 🧮 Brackets ((){}[])  
✅ Automatic copying to clipboard  
✅ Separators (e.g. for serial keys)  
✅ Compact and intuitive interface using **Tkinter**

---

## 🚀 Quick Start

### 🔧 Requirements

- Python **3.8 or higher**
- No external libraries required (only Python standard library)

### ▶️ Run the application

```bash
python main.py
```

Or, if compiled with **PyInstaller**:

```bash
./main.exe
```

---

## 💡 Usage

1. Choose the desired **password length**
2. Enable at least **one character type**
3. (Optional) Specify after how many characters a separator `-` should be inserted
4. Click **Start** to generate the password
5. Use **Copy** to copy the password to the clipboard
6. Use **Close** to exit the program

---

## 📁 File Structure

```plaintext
passwort_generator/
├── assets/
│   ├── favicon.ico        # Window icon
│   └── preview.png        # Program preview
├── main.py                # Main script
└── README.md              # This file
```

---

## 🔒 Security Notice

This tool generates passwords **locally on your device**. It does not store, transmit, or log **any data**. However, it is still recommended to regularly change passwords and protect critical systems with additional security measures (e.g. two-factor authentication).

---

## 👤 Author

**Andreas Huning**  
🔗 [GitHub: Andreas-Huning](https://github.com/Andreas-Huning)

---

## 🧊 License

Released under the **MIT License**. See [LICENSE](LICENSE) for details.
