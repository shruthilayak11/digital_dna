# 🔐 Lightweight Digital DNA Authentication using Keystroke Dynamics

A behavioral biometric authentication system that enhances traditional password-based login by analyzing how a user types.

---

## 🚀 Project Overview

Traditional authentication systems rely only on passwords, which can be stolen, guessed, or shared.

This project introduces an additional security layer using **keystroke dynamics**, where each user’s typing behavior acts as a unique **Digital DNA**.

Instead of verifying just *what* is typed, the system verifies *how* it is typed.

---

## 🎯 Key Features

- ⌨️ Keystroke data capture (key press & release timings)
- 📊 Feature extraction:
  - Average Hold Time
  - Standard Deviation of Hold Time
  - Average Flight Time
  - Standard Deviation of Flight Time
  - Typing Speed
  - Total Typing Duration
- 🧠 Multi-sample enrollment (5 samples averaged)
- 🔍 Threshold-based authentication
- 🤖 Anomaly detection using Isolation Forest
- 📈 Confidence score generation

---

## 🏗️ System Architecture

The system is divided into the following modules:

1. **Capture Module**
   - Records key press and release timestamps

2. **Feature Extraction Module**
   - Converts raw keystroke data into meaningful features

3. **Authentication Module**
   - Compares current typing pattern with stored profile

4. **ML Module**
   - Detects anomalies in typing behavior

5. **UI Layer**
   - Provides an interactive interface for users

---

## 🔄 Working Flow

1. User enters password  
2. Keystroke data is captured  
3. Features are extracted  
4. During registration:
   - Multiple samples are collected and averaged  
5. During login:
   - New sample is compared with stored profile  
6. Decision is made using:
   - Threshold-based comparison  
   - Machine learning anomaly detection  
7. Output displayed:
   - Genuine User / Imposter  
   - Confidence Score  
   - Typing Metrics  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- NumPy  
- pynput  

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Navigate to project folder
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
