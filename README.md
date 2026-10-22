# PHISHPROT - Phishing URL Detector 🛡️

A BCA Cyber Security Project to detect suspicious and phishing URLs.

### 🚀 Live Demo (Local)
Run locally: http://127.0.0.1:5000

### 🔍 How it Works
Checks 7 phishing factors:
1. Long URL
2. Uses HTTP instead of HTTPS
3. Contains @ symbol
4. Contains IP address
5. Suspicious keywords (login, verify, free, secure)
6. Too many subdomains
7. URL Shortener

If Risk Score (c) > 2, it flags as Phishing.

### 💻 Tech Stack
- Python 3
- Flask
- HTML/CSS

### ▶️ How to Run
pip install flask
python app.py

### 👨‍🎓 Author
BCA(Cybersecurity and Forensics) Student, University of  Lucknow
