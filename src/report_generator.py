
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "email_logs.csv"

def generate_report():
    if not LOG_FILE.exists():
        print("No email logs found. Run the automation first.")
        return

    df = pd.read_csv(LOG_FILE)

    print("\n========== EMAIL AUTOMATION REPORT ==========")
    print("Total emails processed:", len(df))

    print("\nStatus Summary:")
    print(df["status"].value_counts().to_string())

    print("\nRecipient Details:")
    print(
        df[["timestamp", "recipient", "subject", "status"]]
        .to_string(index=False)
    )

    print("=============================================")

if __name__ == "__main__":
    generate_report()
