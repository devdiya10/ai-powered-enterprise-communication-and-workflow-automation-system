
from src.logger import log_email
from pathlib import Path
from email.message import EmailMessage
from datetime import datetime


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
OUTBOX_DIR = BASE_DIR / "logs" / "outbox"


def send_email(recipient, subject, body):

    # Create outbox folder if it doesn't exist
    OUTBOX_DIR.mkdir(parents=True, exist_ok=True)

    # Create email message
    message = EmailMessage()

    message["From"] = "automation@example.com"
    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"email_{timestamp}.eml"

    file_path = OUTBOX_DIR / filename

    # Save email instead of sending it
    file_path.write_bytes(message.as_bytes())
    log_email(
    recipient,
    subject,
    "SIMULATED SUCCESS",
    "Email saved locally; no real email was sent."
)

    print("\n========== EMAIL STATUS ==========")
    print("Recipient:", recipient)
    print("Subject:", subject)
    print("Status: SIMULATED SUCCESS")
    print("Saved at:", file_path)
    print("==================================")


if __name__ == "__main__":

    send_email(
        "rahul@example.com",
        "Test Email",
        "This is a test email from our automation system."
    )
