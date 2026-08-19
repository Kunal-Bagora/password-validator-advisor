# 🔐 Password Validator & Advisor

A Python-based password validation and security advisory project that checks whether a password meets essential security requirements, evaluates its strength, detects excessive character repetition, and provides practical security recommendations.

The project focuses on Python logic and is presented through an interactive Streamlit interface so that non-technical users can easily understand and test how the password analysis works.

## 🔗 Live Web Demo

🚀 [Click Here to Try the Password Validator & Advisor](https://password-validator-advisor.streamlit.app/)

## 📂 Repository Structure

This repository contains two versions of the project:

### 1. `Password_Validator_Advisor.py` — Core Python Logic

This is my original Python implementation developed from scratch.

It contains the core logic for:

- Password validation
- Password strength evaluation
- Repeated-character detection
- Security recommendations
- User input handling

The original Python implementation can be run directly from the terminal without the Streamlit interface.

### 2. `Password_Validator_Advisor_Streamlit.py` — AI-Assisted Streamlit Interface

Since my primary focus is on Python logic, backend development, and data analytics rather than frontend development, I used an AI assistant to help wrap my original Python implementation into an interactive Streamlit interface.

The original Python logic remains unchanged. The Streamlit interface makes the project easier for non-technical users to explore by allowing them to enter a password, view the validation result, check its strength, and receive security recommendations through a web interface.

## 🚀 Features

- **Password Validation**  
  Checks whether the password contains at least 8 characters, an uppercase letter, a lowercase letter, a digit, and a special character.

- **Password Strength Evaluation**  
  Classifies passwords into:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
  - Excellent

- **Repeated Character Detection**  
  Detects excessive repetition of the same character.

- **Security Recommendations**  
  Provides practical advice such as avoiding common passwords, predictable sequences, keyboard patterns, and easily guessable personal information.

- **Interactive Web Interface**  
  Provides a visual interface for users to test and understand the password analysis.

## 🛠️ Tech Stack

- **Language:** Python
- **Web Interface:** Streamlit
- **Python Standard Library:** `string`

## 💻 How to Run Locally

Run the following commands in your terminal to test the project:

```bash
# 1. Clone the repository
git clone https://github.com/Kunal-Bagora/password-validator-advisor.git

# 2. Navigate to the directory
cd password-validator-advisor

# 3. To run the core Python logic
python Password_Validator_Advisor.py

# 4. Install requirements for the Web UI
pip install -r requirements.txt

# 5. Run the Streamlit Web UI
streamlit run Password_Validator_Advisor_Streamlit.py
