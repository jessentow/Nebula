import csv
import random
from faker import Faker

fake = Faker()


def generate_unique_emails(num_students):
    emails = set()
    while len(emails) < num_students:
        email = fake.email()
        if email not in emails:
            emails.add(email)
            yield email


def generate_students_data(num_students):
    students_data = []
    emails = generate_unique_emails(num_students)
    for i in range(1, num_students + 1):
        email = next(emails)
        name = fake.name()
        attendance_average = round(random.uniform(70, 100), 1)
        assignment_completion = random.randint(8, 20)
        ranking = random.randint(1, num_students)
        cohort = random.choice(["cohort 1", "cohort 2"])
        students_data.append(
            [i, email, name, attendance_average, assignment_completion, ranking, cohort]
        )
    return students_data


def write_to_csv(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "id",
                "email",
                "name",
                "attendance_average",
                "assignment_completion",
                "ranking",
                "cohort",
            ]
        )
        writer.writerows(data)


if __name__ == "__main__":
    num_students = 100
    students_data = generate_students_data(num_students)
    write_to_csv(students_data, "students_data.csv")
    print("CSV file generated successfully!")
