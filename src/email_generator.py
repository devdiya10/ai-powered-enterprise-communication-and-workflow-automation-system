
from datetime import datetime


def generate_email(name, category, department):

    if category.lower() == "interview":

        subject = "Interview Invitation"

        body = f"""
Hello {name},

We are pleased to inform you that you have been
invited for an interview.

Department: {department}

Please confirm your availability.

Regards,
HR Department
        """

    elif category.lower() == "meeting":

        subject = "Meeting Notification"

        body = f"""
Hello {name},

This is a reminder about your upcoming meeting.

Department: {department}

Please ensure your availability.

Regards,
Administration Team
        """

    elif category.lower() == "deadline":

        subject = "Important Deadline Reminder"

        body = f"""
Hello {name},

This is a reminder regarding your upcoming deadline.

Department: {department}

Please complete your assigned task on time.

Regards,
Operations Team
        """

    else:

        subject = "General Notification"

        body = f"""
Hello {name},

This is an automated notification.

Regards,
Automation System
        """

    return subject, body


def preview_email(name, category, department):

    subject, body = generate_email(
        name, category, department
    )

    print("\n========== EMAIL PREVIEW ==========")
    print("Recipient:", name)
    print("Subject:", subject)
    print("Generated At:", datetime.now())
    print("\nEmail Body:")
    print(body)
    print("===================================")


if __name__ == "__main__":

    preview_email(
        "Rahul Sharma",
        "Interview",
        "HR"
    )
