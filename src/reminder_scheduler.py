
import pandas as pd
import time

from pathlib import Path
from datetime import datetime

from src.email_generator import generate_email
from src.email_sender import send_email


BASE_DIR = Path(__file__).resolve().parent.parent

REMINDER_FILE = BASE_DIR / "data" / "reminders.csv"


def load_reminders():

    df = pd.read_csv(REMINDER_FILE)

    required_columns = [
        "name",
        "email",
        "department",
        "category",
        "reminder_time"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    df["reminder_time"] = pd.to_datetime(
        df["reminder_time"],
        errors="coerce"
    )

    df = df.dropna(subset=required_columns)

    return df


def process_due_reminders(test_mode=False):

    reminders = load_reminders()

    current_time = datetime.now()

    processed = 0

    print("\n========== REMINDER SCHEDULER ==========")

    for index, reminder in reminders.iterrows():

        reminder_time = reminder["reminder_time"]

        if test_mode or reminder_time <= current_time:

            name = reminder["name"]
            email = reminder["email"]
            department = reminder["department"]
            category = reminder["category"]

            subject, body = generate_email(
                name,
                category,
                department
            )

            send_email(email, subject, body)

            processed += 1

            print(f"Reminder processed for: {name}")

    print("\nTotal reminders processed:", processed)

    return processed


def start_scheduler():

    print("Scheduler started. Checking every 30 seconds.")

    while True:

        process_due_reminders()

        time.sleep(30)


if __name__ == "__main__":

    process_due_reminders(test_mode=True)
