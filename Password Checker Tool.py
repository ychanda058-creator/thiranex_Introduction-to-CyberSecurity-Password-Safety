

import re

def check_password_strength(password):
    score = 0
    
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    
    if score == 5:
        return "Strong Password 💪"
    elif score >= 3:
        return "Medium Password ⚠"
    else:
        return "Weak Password ❌"
