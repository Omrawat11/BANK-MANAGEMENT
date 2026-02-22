
import streamlit as st
import json
from pathlib import Path
import random
import string

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="NeoBank", page_icon="💳", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Headings */
h1, h2, h3, h4, label {
    color: white !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    font-weight: bold;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

/* Input Fields */
input {
    border-radius: 10px !important;
}

.balance-card {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------
DATABASE = "data.json"

if Path(DATABASE).exists():
    with open(DATABASE, "r") as file:
        data = json.load(file)
else:
    data = []

def save_data():
    with open(DATABASE, "w") as file:
        json.dump(data, file)

def generate_account():
    digits = random.choices(string.digits, k=4)
    letters = random.choices(string.ascii_letters, k=4)
    acc = digits + letters
    random.shuffle(acc)
    return "".join(acc)

# ---------------- SIDEBAR ----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=80)
st.sidebar.title("NeoBank")
st.sidebar.markdown("Digital Banking Redefined 🚀")
st.sidebar.markdown("---")

menu = st.sidebar.radio("Navigation", [
    "Create Account",
    "Deposit",
    "Withdraw",
    "View Account",
    "Delete Account",
    "View All Accounts"
])

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>💳 Banco de España</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    # ---------------- CREATE ----------------
    if menu == "Create Account":
        st.subheader("🆕 Create New Account")

        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1)
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        pin = st.text_input("4 Digit PIN", type="password")

        if st.button("Create Account"):
            if age >= 18 and len(pin) == 4 and pin.isdigit():
                account_no = generate_account()

                user = {
                    "Name": name,
                    "Age": age,
                    "PhoneNumber": phone,
                    "Email": email,
                    "Pin": pin,
                    "Account_no.": account_no,
                    "Balance": 0
                }

                data.append(user)
                save_data()

                st.success("Account Created Successfully 🎉")
                st.info(f"Your Account Number: {account_no}")
            else:
                st.error("Age must be 18+ and PIN must be exactly 4 digits")

    # ---------------- DEPOSIT ----------------
    elif menu == "Deposit":
        st.subheader("💰 Deposit Money")

        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount", min_value=1)

        if st.button("Deposit"):
            user = next((i for i in data if i["Account_no."] == acc and i["Pin"] == pin), None)

            if user:
                user["Balance"] += amount
                save_data()
                st.success("Money Deposited Successfully 💸")
            else:
                st.error("Invalid Account or PIN")

    # ---------------- WITHDRAW ----------------
    elif menu == "Withdraw":
        st.subheader("🏧 Withdraw Money")

        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")
        amount = st.number_input("Amount", min_value=1)

        if st.button("Withdraw"):
            user = next((i for i in data if i["Account_no."] == acc and i["Pin"] == pin), None)

            if user:
                if user["Balance"] >= amount:
                    user["Balance"] -= amount
                    save_data()
                    st.success("Money Withdrawn Successfully 💳")
                else:
                    st.error("Insufficient Balance")
            else:
                st.error("Invalid Account or PIN")

    # ---------------- VIEW ACCOUNT ----------------
    elif menu == "View Account":
        st.subheader("👤 Account Details")

        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")

        if st.button("View Details"):
            user = next((i for i in data if i["Account_no."] == acc and i["Pin"] == pin), None)

            if user:
                st.markdown(f"""
                <div class='balance-card'>
                💰 Current Balance: ₹ {user["Balance"]}
                </div>
                """, unsafe_allow_html=True)

                st.write("👤 Name:", user["Name"])
                st.write("📧 Email:", user["Email"])
                st.write("📱 Phone:", user["PhoneNumber"])
            else:
                st.error("Invalid Account or PIN")

    # ---------------- DELETE ACCOUNT ----------------
    elif menu == "Delete Account":
        st.subheader("🗑️ Delete Account")

        acc = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password")

        if st.button("Delete Account"):
            user = next((i for i in data if i["Account_no."] == acc and i["Pin"] == pin), None)

            if user:
                data.remove(user)
                save_data()
                st.success("Account Deleted Successfully ❌")
            else:
                st.error("Invalid Account or PIN")

    # ---------------- VIEW ALL ACCOUNTS ----------------
    elif menu == "View All Accounts":
        st.subheader("📊 All Account Details")

        if data:
            for user in data:
                st.markdown(f"""
                <div class='balance-card'>
                💰 Balance: ₹ {user["Balance"]}
                </div>
                """, unsafe_allow_html=True)

                st.write("👤 Name:", user["Name"])
                st.write("📧 Email:", user["Email"])
                st.write("📱 Phone:", user["PhoneNumber"])
                st.write("🏦 Account Number:", user["Account_no."])
                st.markdown("---")
        else:
            st.warning("No accounts found.")

    st.markdown("</div>", unsafe_allow_html=True)