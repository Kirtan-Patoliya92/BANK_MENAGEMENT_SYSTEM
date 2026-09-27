import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management", page_icon="🏦")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Menu",
    (
        "Create Account",
        "Deposit",
        "Withdraw",
        "Account Details",
        "Update Details",
        "Delete Account",
    ),
)

# ---------------- CREATE ----------------

if menu == "Create Account":

    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):

        ok, msg = bank.create_account(name, age, email, pin)

        if ok:
            st.success("Account Created Successfully")
            st.info(f"Your Account Number : {msg}")
        else:
            st.error(msg)

# ---------------- DEPOSIT ----------------

elif menu == "Deposit":

    st.header("Deposit Money")

    account = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):

        ok, msg = bank.deposit(account, pin, amount)

        if ok:
            st.success(msg)
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------

elif menu == "Withdraw":

    st.header("Withdraw Money")

    account = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):

        ok, msg = bank.withdraw(account, pin, amount)

        if ok:
            st.success(msg)
        else:
            st.error(msg)

# ---------------- DETAILS ----------------

elif menu == "Account Details":

    st.header("Account Details")

    account = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):

        user = bank.login(account, pin)

        if user:

            st.success("Account Found")

            st.write("### Name:", user["name"])
            st.write("### Email:", user["email"])
            st.write("### Age:", user["age"])
            st.write("### Account:", user["account"])
            st.write("### Balance: ₹", user["balance"])

        else:
            st.error("Invalid Account")

# ---------------- UPDATE ----------------

elif menu == "Update Details":

    st.header("Update Details")

    account = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    name = st.text_input("New Name")
    email = st.text_input("New Email")

    if st.button("Update"):

        if bank.update(account, pin, name, email):
            st.success("Updated Successfully")
        else:
            st.error("Invalid Account")

# ---------------- DELETE ----------------

elif menu == "Delete Account":

    st.header("Delete Account")

    account = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        if bank.delete(account, pin):
            st.success("Account Deleted Successfully")
        else:
            st.error("Invalid Account")