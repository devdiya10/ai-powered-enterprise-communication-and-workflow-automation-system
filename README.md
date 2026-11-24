# 📧 AI-Powered Enterprise Communication and Workflow Automation System

A Python-based Email Automation and Reminder System designed to simplify communication workflows through contact management, personalized email generation, simulated email delivery, reminder scheduling, and activity tracking.

## 🚀 Project Overview

Managing emails and reminders manually can be time-consuming and repetitive. This project provides an automated solution that manages contact information, generates personalized email messages based on categories, processes reminders, and maintains activity logs.

It also includes a Streamlit dashboard that provides an interactive interface for managing contacts, generating emails, and viewing email activity reports.

**Note:** Email delivery is currently simulated. Generated emails are saved locally rather than sent to real email inboxes.

## ✨ Key Features

- **Contact Management:** Reads and validates contact information using CSV files.
- **Email Generation:** Creates personalized email messages based on categories such as Interview, Meeting, and Deadline.
- **Email Simulation:** Saves generated emails locally in `.eml` format.
- **Reminder Scheduling:** Checks reminder dates and processes due reminders.
- **Activity Logging:** Records timestamps, recipients, subjects, and email statuses.
- **Report Generation:** Generates email activity summaries using Pandas.
- **Interactive Dashboard:** Provides a Streamlit-based interface for viewing contacts, generating emails, and tracking activity.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | CSV processing and data analysis |
| Streamlit | Interactive web dashboard |
| CSV | Contact and reminder data storage |
| APScheduler | Scheduling library included in the project environment |
| Python Logging / CSV Logging | Activity tracking |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
AI-Powered-Enterprise-Communication/
│
├── data/
│   ├── contacts.csv
│   └── reminders.csv
│
├── logs/
│   └── outbox/
│
├── screenshots/
│
├── src/
│   ├── __init__.py
│   ├── contact_manager.py
│   ├── email_generator.py
│   ├── email_sender.py
│   ├── reminder_scheduler.py
│   ├── logger.py
│   └── report_generator.py
│
├── templates/
├── tests/
│   ├── test_contacts.py
│   └── test_email.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/devdiya10/ai-powered-enterprise-communication-and-workflow-automation-system.git
```

### 2. Navigate to the project directory

```bash
cd ai-powered-enterprise-communication-and-workflow-automation-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

### Run the main automation system

```bash
python main.py
```

### Launch the Streamlit dashboard

```bash
streamlit run app.py
```

### Run the reminder scheduler module

```bash
python -m src.reminder_scheduler
```

### Generate the email activity report

```bash
python -m src.report_generator
```

## 📊 Dashboard Modules

1. **Dashboard:** Displays contact and email activity statistics.
2. **Contacts:** Displays available contact information.
3. **Generate Emails:** Generates personalized email content and simulates delivery.
4. **Email Reports:** Displays recorded email activity.

## 🧠 Concepts Learned

- Python functions and modular programming
- File handling and CSV operations
- Data cleaning and validation
- Regular expressions for email validation
- Exception handling
- Python virtual environments
- Email message generation using `email.message`
- Date and time handling
- Basic automation and scheduling concepts
- Data analysis using Pandas
- Interactive application development using Streamlit
- Version control using Git and GitHub

## 🔮 Future Enhancements

- Integration with Gmail SMTP for actual email delivery.
- Automated recurring reminders.
- Database integration using SQLite or PostgreSQL.
- Improved reminder tracking and duplicate prevention.
- Email delivery status monitoring.
- Advanced analytics and reporting.
- User authentication and role-based access.

## 👩‍💻 Author

**Diya Khurana**

Electronics and Communication Engineering Student

GitHub: [@devdiya10](https://github.com/devdiya10)

---

⭐ If you find this project interesting, feel free to explore the repository and its implementation.

**Project Status:** Developed as a Python-based learning and automation project.
