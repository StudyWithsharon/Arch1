import re


def ask_name(type):
    while True:
        name = input(f"Enter a {type} name: ")
        if re.match(r"^[A-Z][a-zA-Z]{1,9}$", name):
            return name
        print("Input error")


def ask_job_title():
    while True:
        title = input("Enter a job title: ")
        if re.match(r"^[a-zA-Z+ ]{10,}$", title):
            return title
        print("Input error")


def ask_salary():
    while True:
        salary = input("Enter annual salary (between 20,000.00 and 80,000.00): ")
        pattern = r"^([2-7]\d{1}\.\d{3},\d{2}|80\.000,00)$"
        if re.match(pattern, salary):
            return salary
        print("Input error")


def ask_date():
    while True:
        pattern = r"^202[1-2]-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
        date = input("Enter start date (YYYY-MM-DD): ")
        if re.match(pattern, date):
            return date
        print("Input error")


def ask_feedback():
    while True:
        has_feedback = input("Feedback?").lower() == "yes"
        if has_feedback:
            return input("Enter your Feedback (One Statement)")
        return ""


def ask_offer_or_rejection():
    while True:
        letter_type = input("Job Offer or Rejection: ").lower()

        if letter_type in ["job offer", "rejection"]:
            return letter_type

        print("Input error")


def ask_more_letters():
    # while True:
    more_letters = input("More letters yes or no: ").lower() == "yes"

    if not more_letters:
        return

    job_offer_or_rejection = ask_offer_or_rejection()
    first_name = ask_name("first")
    last_name = ask_name("last")
    job_title = ask_job_title()

    email = ""

    match job_offer_or_rejection:
        case "job offer":
            salary = ask_salary()
            start_date = ask_date()
            feedback = ask_feedback()
            email = job_offer(
                first_name, last_name, job_title, salary, start_date, feedback
            )
        case "rejection":
            feedback = ask_feedback()
            email = rejection(first_name, last_name, job_title, feedback)
    print("Here is the final letter to send:")
    print(email)


def job_offer(first_name, last_name, job_title, salary, start_date, feedback):
    mail = f"Dear {first_name} {last_name},\n"
    mail += f"After careful evaluation of your application for the position of {job_title},\n"
    mail += f"we are glad to offer you the job. Your salary will be {salary} euro annually.\n"
    mail += f"Your start date will be on {start_date}. "
    mail += "Please do not hesitate to contact us with any questions.\n"
    if len(feedback) >= 1:
        mail += f"{feedback}\n"
    mail += "Sincerely,\n"
    mail += "HR Department of XYZ"

    return mail


def rejection(first_name, last_name, job_title, feedback):
    mail = f"Dear {first_name} {last_name},\n"
    mail += f"After careful evaluation of your application for the position of {job_title},\n"
    mail += "at this moment we have decided to proceed with another candidate.\n"
    if len(feedback) >= 1:
        mail += "Here we would like to provide you our feedback about the interview.\n"
        mail += f"{feedback}\n"
    mail += "We wish you the best in finding your future desired career. "
    mail += "Please do not hesitate to contact us with any questions.\n"
    mail += "Sincerely,\n"
    mail += "HR Department of XYZ"

    return mail


ask_more_letters()
