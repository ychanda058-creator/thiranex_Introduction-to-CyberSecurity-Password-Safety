# thiranex_Introduction-to-CyberSecurity and Password-Safety
 ## Overview
 
 The Thiranex Introduction to CyberSecurity – Password Safety module highlights the critical role passwords play in protecting digital assets. It explains common threats like brute-force attacks, phishing, and password reuse. The course emphasizes using strong, unique passwords and encourages tools like password managers. It also promotes multi-factor authentication (MFA) for added security. Best practices such as avoiding personal info, using long passphrases, and staying aware of data breaches are covered to improve password hygiene.
 
 ## Features

🚀 Lightweight - no external dependencies
⚡ Fast password evaluation
📊 Clear strength indicators
🔍 Regex-based pattern matching
💯 Simple scoring system

 ## Installation
 Step-by-Step Installation-
1. Clone the Repository
bashgit clone https://github.com/ychanda058-creator/thiranex_Introduction-to-CyberSecurity-Password-Safety.git
cd password-strength-checker
2. Create Virtual Environment (Recommended)
   # Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
3. No Additional Dependencies Required
This script uses only Python's built-in re module - no external packages needed!
4. Run the Password Strength Checker
bashpython password_checker.py

 ## Usage
 # Test different passwords
passwords = [
    "password123",           # Weak
    "Password123!",          # Medium  
    "MySecureP@ssw0rd2024"  # Strong
]

for pwd in passwords:
    print(f"'{pwd}' -> {check_password_strength(pwd)}")
    
 ## Security Considerations
Security Considerations:

-Length Is Weighted Lightly
While 12+ characters adds 1 point, longer passwords (e.g. 16+) should ideally be more heavily rewarded for added entropy.

Entropy vs Pattern
Your method checks for the presence of character types, but not their distribution or predictability. A password like Aaaaaaaa1! would score high but is weak due to patterns.

No Dictionary Word Check
The function doesn’t detect common dictionary words or leaked passwords, which attackers often exploit in real-world attacks.

False Sense of Security
Scoring might label a password “Strong 💪” that would be weak in real-world scenarios (e.g. Password123!), so clear disclaimers are important.

Regex Efficiency
The regular expressions are simple and efficient, but may miss edge cases (e.g. Unicode characters, whitespace, emojis).

 ## Author
Name : Chanda Kumari Yadav
Contact: ychanda058@gmail.com
