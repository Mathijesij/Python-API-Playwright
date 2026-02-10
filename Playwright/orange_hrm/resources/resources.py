import random
from faker import Faker
from datetime import datetime, timedelta

class resources:
    """
    Utility class to generate random and fake test data for automation tests.

    Provides methods for generating:
    - Names and usernames
    - Employee IDs and license numbers
    - Dates (past and future)
    - Marital status, gender, and blood type
    - Contact numbers and email addresses
    - Job-related details (title, category, location)
    - Salary grades and amounts
    """

    def __init__(self):
        """Initialize Faker instance for generating realistic names and data."""
        self.fake = Faker()

    def generate_first_name(self):
        """Return a random first name."""
        return self.fake.first_name()

    def generate_last_name(self):
        """Return a random last name."""
        return self.fake.last_name()

    def generate_name(self):
        """Return a full name (first + last)."""
        return self.fake.name()

    def generate_username(self):
        """
        Generate a unique username combining first name, last name,
        and a random number.
        """
        number = random.randint(1, 999)
        return f"{self.generate_first_name()}.{self.generate_last_name()}{number}"

    @staticmethod
    def random_emp_id():
        """Generate a random employee ID (5-digit string)."""
        return str(random.randint(10000, 99999))

    @staticmethod
    def random_other_id():
        """Generate a random other ID (6-digit string)."""
        return str(random.randint(100000, 999999))

    @staticmethod
    def random_license_number():
        """Generate a random driving license number (10-digit string)."""
        return str(random.randint(1000000000, 9999999999))

    @staticmethod
    def generate_license_expiry():
        """Return a random future date (1 month to 5 years) in YYYY-DD-MM format."""
        days_in_future = random.randint(30, 365 * 5)
        future_date = datetime.now() + timedelta(days=days_in_future)
        return future_date.strftime("%Y-%d-%m")

    @staticmethod
    def generate_random_past_date():
        """Return a random past date (within last year) in YYYY-DD-MM format."""
        days_back = random.randint(1, 365)
        past_date = datetime.today() - timedelta(days=days_back)
        return past_date.strftime("%Y-%d-%m")

    @staticmethod
    def marital_status():
        """Return a random marital status ('Single' or 'Married')."""
        return random.choice(["Single", "Married"])

    @staticmethod
    def gender():
        """Return a random gender ('Male' or 'Female')."""
        return random.choice(["Male", "Female"])

    @staticmethod
    def blood_type():
        """Return a random blood type."""
        return random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])

    @staticmethod
    def test_field():
        """Return a random 6-digit number as string."""
        return str(random.randint(100000, 999999))

    @staticmethod
    def contact_number():
        """Return a random 10-digit contact number starting from 6-9."""
        return str(random.randint(6000000000, 9999999999))

    @staticmethod
    def relationship():
        """
        Return a random relationship based on gender.
        Male -> ['Wife', 'Mother', 'Daughter']
        Female -> ['Husband', 'Father', 'Son']
        """
        gender = resources.gender()
        if gender == "Male":
            return random.choice(["Wife", "Mother", "Daughter"])
        else:
            return random.choice(["Husband", "Father", "Son"])

    def generate_work_email(self):
        """Return a randomly generated company email address."""
        random_num = random.randint(100, 999)
        email = (
            f"{self.generate_first_name().lower()}."
            f"{self.generate_first_name().lower()}{random_num}@company.com"
        )
        return email

    def generate_other_email(self):
        """Return a randomly generated personal email address (Gmail)."""
        random_num = random.randint(100, 999)
        email = (
            f"{self.generate_first_name().lower()}."
            f"{self.generate_first_name().lower()}{random_num}@gmail.com"
        )
        return email

    @staticmethod
    def dependents_relationship():
        """Return a random dependents relationship ('Child' or 'Other')."""
        return random.choice(["Child", "Other"])

    @staticmethod
    def job_title():
        """Return a random job title."""
        return random.choice(["Account Assistant", "Automaton Tester", "HR Manager"])

    @staticmethod
    def job_category():
        """Return a random job category."""
        return random.choice(["Craft Workers", "Professionals", "Officials and Managers"])

    @staticmethod
    def sub_unit():
        """Return a random sub_unit of the organization."""
        return random.choice(["Administration", "Quality Assurance", "Marketing"])

    @staticmethod
    def location():
        """Return a random office location."""
        return random.choice(["HQ - CA, USA", "New York Sales Office", "Texas R&D"])

    @staticmethod
    def emp_status():
        """Return a random employment status."""
        return random.choice([
            "Freelance",
            "Full-Time Contract",
            "Full-Time Permanent",
            "Full-Time Probation",
            "Part-Time Contract"
        ])

    @staticmethod
    def pay_grade():
        """Return a random pay grade."""
        return random.choice(["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5"])

    @staticmethod
    def pay_frequency():
        """Return a random pay frequency."""
        return random.choice(["Bi Weekly", "Hourly", "Monthly", "Weekly"])

    @staticmethod
    def grade1_amount():
        """Return a random salary amount for Grade 1."""
        return str(random.randint(50000, 60000))

    @staticmethod
    def grade2_amount():
        """Return a random salary amount for Grade 2."""
        return str(random.randint(40000, 50000))

    @staticmethod
    def grade3_amount():
        """Return a random salary amount for Grade 3."""
        return str(random.randint(30000, 40000))

    @staticmethod
    def grade4_amount():
        """Return a random salary amount for Grade 4."""
        return str(random.randint(20000, 30000))

    @staticmethod
    def grade5_amount():
        """Return a random salary amount for Grade 5."""
        return str(random.randint(10000, 20000))
