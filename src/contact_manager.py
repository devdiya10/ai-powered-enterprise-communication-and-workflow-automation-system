
import pandas as pd
import re
from pathlib import Path


# Locate the project data folder
BASE_DIR = Path(__file__).resolve().parent.parent
CONTACT_FILE = BASE_DIR / "data" / "contacts.csv"


def load_contacts():

    # Read CSV file
    df = pd.read_csv(CONTACT_FILE)

    # Check required columns
    required_columns = ["name", "email", "department", "category"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Remove unnecessary spaces
    for column in required_columns:
        df[column] = df[column].astype("string").str.strip()

    # Check empty values
    df = df.dropna(subset=required_columns)
    df = df[(df[required_columns] != "").all(axis=1)]

    # Remove duplicate email addresses
    df = df.drop_duplicates(subset=["email"], keep="first")

    return df


def validate_email(email):

    pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

    return bool(re.match(pattern, str(email)))


def process_contacts():

    contacts = load_contacts()

    # Validate email addresses
    contacts["valid_email"] = contacts["email"].apply(
        validate_email
    )

    valid_contacts = contacts[contacts["valid_email"] == True]
    invalid_contacts = contacts[contacts["valid_email"] == False]

    print("\n========== CONTACT REPORT ==========")

    print("Total contacts:", len(contacts))
    print("Valid contacts:", len(valid_contacts))
    print("Invalid contacts:", len(invalid_contacts))

    print("\nValid Contact List:")
    print(valid_contacts[["name", "email"]].to_string(index=False))

    if not invalid_contacts.empty:
        print("\nInvalid Contact List:")
        print(invalid_contacts[["name", "email"]].to_string(index=False))

    return valid_contacts


if __name__ == "__main__":
    process_contacts()
