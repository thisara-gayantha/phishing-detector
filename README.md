# 🔒 Phishing Detector

A web-based application that analyzes URLs to detect phishing and suspicious links. It uses multiple security checks to protect users from malicious websites.

## 📋 Features

- **IP Address Detection** - Identifies URLs using IP addresses instead of domain names
- **@ Symbol Detection** - Detects phishing attempts using the @ symbol trick
- **Domain Analysis** - Checks for excessive dots and suspicious keywords
- **HTTPS Verification** - Ensures secure HTTPS connection
- **SSL Certificate Check** - Validates SSL certificate validity and expiration
- **Domain Age Analysis** - Flags newly registered domains (less than 6 months old)
- **Redirection Detection** - Identifies URLs with suspicious redirects
- **Real-time Results** - Instant analysis with detailed reasoning
- **Modern UI** - Clean, responsive, and user-friendly interface

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd phishing-detector
```

2. **Create a virtual environment:**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the application:**
```bash
python app.py
```

6. **Open your browser and visit:**
```
http://localhost:5000
```

## 📦 Dependencies

- **Flask** - Web framework for building the application
- **requests** - HTTP library for making web requests
- **whois** - Domain registration information lookup

All dependencies are listed in `requirements.txt`

## 🔧 Project Structure

```
phishing-detector/
├── app.py                 # Flask application entry point
├── detector.py            # Core phishing detection logic
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   └── style.css         # CSS styling
└── templates/
    └── index.html        # HTML template
```

## 🛡️ How It Works

The detector analyzes URLs across multiple security dimensions:

### Detection Methods:

1. **IP Address Check** - Returns +2 score if URL contains IP instead of domain
2. **@ Symbol Detection** - Returns +2 score (common phishing tactic)
3. **Excessive Dots** - Returns +1 score if URL has more than 3 dots
4. **Suspicious Keywords** - Returns +1 score if URL contains keywords like "login", "verify", "bank", "secure", "update"
5. **HTTPS Check** - Returns +1 score if not using secure HTTPS
6. **SSL Certificate** - Returns +2 score if SSL is invalid or expired
7. **Domain Age** - Returns +2 score if domain is less than 6 months old
8. **Redirection** - Returns +1 score if URL redirects

### Risk Scoring:

- **Score ≥ 5**: 🚨 **PHISHING** - High risk, likely malicious
- **Score 3-4**: ⚠️ **SUSPICIOUS** - Medium risk, exercise caution
- **Score < 3**: ✅ **SAFE** - Low risk, appears legitimate

## 💡 Usage Example

1. Open the application in your browser
2. Paste a URL in the input field
3. Click "🔍 Check URL"
4. Review the result and detection reasons
5. Take appropriate action based on the assessment

## ⚠️ Important Notes

- This tool provides analysis but is not 100% foolproof
- Always verify suspicious URLs independently
- Use this as one layer of your security strategy
- Keep your browser and antivirus software updated
- Never enter personal information on suspicious sites

## 🔐 Security Best Practices

- Be cautious with URLs from unknown sources
- Hover over links to see actual destination
- Check SSL certificate validity (lock icon in browser)
- Verify sender of email links
- Use multi-factor authentication on important accounts

## 🐛 Troubleshooting

**ModuleNotFoundError: No module named 'flask'**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt`

**Connection Error when checking URLs**
- Check your internet connection
- Some URLs may be blocked or unreachable
- The application has a 3-second timeout per request

**Port 5000 already in use**
- Change the port in `app.py` line 18: `app.run(debug=True, port=5001)`

## 📝 Future Enhancements

- [ ] Machine learning-based detection
- [ ] URL reputation database integration
- [ ] Browser extension
- [ ] API endpoint for programmatic access
- [ ] Database to log checked URLs
- [ ] Email scanning integration

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Development

To contribute or modify:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit improvements

## 📞 Support

For issues or questions, review the code comments or test with known phishing URLs:
- Example: `http://192.168.1.1@google.com` (phishing)
- Example: `https://www.google.com` (safe)

---

**Stay safe online! Always verify URLs before clicking.** 🔒
