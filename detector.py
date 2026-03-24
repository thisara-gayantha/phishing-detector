import re
import requests
import socket
import ssl
import whois
from urllib.parse import urlparse
from datetime import datetime

def has_ip(url):
    return re.match(r"^http[s]?://\d+\.\d+\.\d+\.\d+", url) is not None

def has_at_symbol(url):
    return "@" in url

def too_many_dots(url):
    return url.count('.') > 3

def suspicious_words(url):
    words = ["login", "verify", "bank", "secure", "update"]
    return any(word in url.lower() for word in words)

def is_https(url):
    return url.startswith("https")

# 🔒 SSL Certificate Check
def check_ssl(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
            cert = s.getpeercert()

            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            if expiry_date < datetime.utcnow():
                return False, "Expired SSL"
            return True, "Valid SSL"

    except Exception as e:
        return False, "No SSL / Invalid SSL"

# 🌐 Domain Age Check
def domain_age(domain):
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        age_days = (datetime.now() - creation_date).days
        return age_days
    except:
        return -1

# 🌐 Redirection Check
def has_redirect(url):
    try:
        response = requests.get(url, timeout=3)
        return len(response.history) > 0
    except:
        return False

# 🚀 Main Detection Function
def analyze(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc

    if has_ip(url):
        score += 2
        reasons.append("Uses IP address")

    if has_at_symbol(url):
        score += 2
        reasons.append("Contains @ symbol")

    if too_many_dots(url):
        score += 1
        reasons.append("Too many dots")

    if suspicious_words(url):
        score += 1
        reasons.append("Suspicious keywords")

    if not is_https(url):
        score += 1
        reasons.append("Not using HTTPS")

    # 🔒 SSL Check
    ssl_valid, ssl_msg = check_ssl(domain)
    if not ssl_valid:
        score += 2
        reasons.append(ssl_msg)

    # 🌐 Domain Age
    age = domain_age(domain)
    if age != -1 and age < 180:
        score += 2
        reasons.append("New domain (less than 6 months)")

    # 🌐 Redirect
    if has_redirect(url):
        score += 1
        reasons.append("Has redirection")

    # Final decision
    if score >= 5:
        result = "🚨 PHISHING"
    elif score >= 3:
        result = "⚠️ SUSPICIOUS"
    else:
        result = "✅ SAFE"

    return result, reasons