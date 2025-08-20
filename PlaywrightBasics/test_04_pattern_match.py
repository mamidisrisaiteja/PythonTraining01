import re

def test_pattern_match1():
 text = """
 Hi Anusha, please contact us at support@example.com for further assistance.
 You can also reach out to admin123@mydomain.co.in if needed.
 """

 # Regex pattern for email
 email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

 # Find all matches
 emails = re.findall(email_pattern, text)

 print("Found emails:", emails)

def test_pattern_match2():
 text = """
 Hi Anusha, please contact us at support@example.com for further assistance.
 You can also reach out to 9449944129 if needed.
 All Rights reserved. 2025
 """


    # Regex pattern for email
 email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

 phone_pattern = r'\b\d{10}\b'
 year_pattern = r'\b\d{4}\b'

 # Find all matches
 emails = re.findall(email_pattern, text)
 phones = re.findall(phone_pattern, text)
 years = re.findall(year_pattern, text)

 print(" Emails found:", emails)
 print(" Phone numbers found:", phones)
 print(" Years found:", years)
