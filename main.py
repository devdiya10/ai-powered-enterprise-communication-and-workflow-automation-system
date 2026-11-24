
from src.email_sender import send_email
from src.contact_manager import process_contacts
from src.email_generator import generate_email


def run_automation():

    print("\n================================")
    print("   EMAIL AUTOMATION SYSTEM")
    print("================================")

    # Step 1: Load valid contacts
    contacts = process_contacts()

    print("\nGenerating personalized emails...")

    # Step 2: Generate email for every contact
    for index, contact in contacts.iterrows():

        name = contact["name"]
        category = contact["category"]
        department = contact["department"]
        email = contact["email"]

        subject, body = generate_email(
            name,
            category,
            department
        )

        # Step 3: Display email preview
        # Step 3: Simulate email sending
        print("\n--------------------------------")
        print("Recipient:", email)
        print("Name:", name)
        print("Subject:", subject)
        print("Email Body:")
        print(body)

        send_email(email, subject, body)

        print("--------------------------------")

    print("\nAutomation process completed!")


if __name__ == "__main__":
    run_automation()
