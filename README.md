💳 NeoBank – Digital Banking System (Streamlit App)

A modern digital banking web application built using Streamlit that allows users to create accounts, deposit money, withdraw money, and manage banking details with a beautiful glassmorphism UI.

🚀 Features

🆕 Create New Account

💰 Deposit Money

🏧 Withdraw Money

👤 View Account Details

🗑️ Delete Account

📊 View All Accounts

🔐 PIN-based Authentication

💾 JSON-based Local Database

🎨 Modern Glass UI with Gradient Background

🛠️ Technologies Used

🐍 Python

🌐 Streamlit

📁 JSON (for database storage)

🎨 Custom CSS Styling

📂 Project Structure
NeoBank/
│
├── app.py          # Main Streamlit application
├── data.json       # Local database (auto-created)
└── README.md       # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/neobank.git
cd neobank
2️⃣ Install Required Libraries
pip install streamlit
3️⃣ Run the Application
streamlit run app.py
🏦 How It Works
🔹 Create Account

User must be 18+ years old

PIN must be exactly 4 digits

Unique account number is auto-generated

Initial balance is ₹0

🔹 Deposit / Withdraw

Requires:

Account Number

PIN

Withdrawal checks for sufficient balance

🔹 View Account

Displays:

Current Balance

Name

Email

Phone Number

🔹 Delete Account

Permanently removes account from database

🔐 Data Storage

All user data is stored locally in:

data.json

⚠️ This is a simple local storage system. Not suitable for production use.

🎨 UI Highlights

Glassmorphism card design

Gradient background

Styled buttons with hover effects

Sidebar navigation

Responsive layout

📸 Preview

(You can add screenshots here)

🚨 Limitations

No password encryption

Data stored locally (JSON file)

No admin authentication for viewing all accounts

Not secure for real-world banking use

🌟 Future Improvements

Add password hashing

Add transaction history

Add login/signup system

Connect to real database (MySQL / MongoDB)

Add OTP verification

Deploy on Streamlit Cloud

👨‍💻 Author

Om Rawat
B.Tech AIML Student

📌 License

This project is for educational purposes only.

