
import streamlit as st
import pandas as pd
from pathlib import Path

from src.contact_manager import load_contacts
from src.email_generator import generate_email
from src.email_sender import send_email

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "logs" / "email_logs.csv"

st.set_page_config(
    page_title="Email Automation System",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Email Automation & Reminder System")
st.write("Manage contacts, generate personalized emails and track automation activity.")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section",
    ["Dashboard", "Contacts", "Generate Emails", "Email Reports"]
)

# Dashboard
if page == "Dashboard":
    st.subheader("Project Dashboard")

    total_contacts = len(load_contacts())

    if LOG_FILE.exists():
        logs = pd.read_csv(LOG_FILE)
        total_emails = len(logs)
        successful = len(logs[logs["status"] == "SIMULATED SUCCESS"])
    else:
        total_emails = 0
        successful = 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Contacts", total_contacts)
    col2.metric("Emails Processed", total_emails)
    col3.metric("Successful Simulations", successful)

# Contacts
elif page == "Contacts":
    st.subheader("Contact Management")

    contacts = load_contacts()
    st.dataframe(contacts, use_container_width=True)

# Generate Emails
elif page == "Generate Emails":
    st.subheader("Generate Personalized Emails")

    contacts = load_contacts()

    selected_email = st.selectbox(
        "Select Recipient",
        contacts["email"].tolist()
    )

    if st.button("Generate and Simulate Email"):
        contact = contacts[contacts["email"] == selected_email].iloc[0]

        subject, body = generate_email(
            contact["name"],
            contact["category"],
            contact["department"]
        )

        st.write("### Email Preview")
        st.write("**To:**", selected_email)
        st.write("**Subject:**", subject)
        st.text(body)

        send_email(selected_email, subject, body)

        st.success("Email simulation completed and logged!")

# Email Reports
elif page == "Email Reports":
    st.subheader("Email Activity Report")

    if LOG_FILE.exists():
        logs = pd.read_csv(LOG_FILE)
        st.dataframe(logs, use_container_width=True)
    else:
        st.info("No email activity found yet. Generate an email first.")
