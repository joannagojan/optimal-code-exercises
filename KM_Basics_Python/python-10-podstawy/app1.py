"""
Write a regular expression that checks if a string contains a valid email address, e.g., km@gmail.com.
Write a regular expression that checks if a string contains a valid URL, e.g., https://km-programs.pl.
Write a regular expression that checks if a string contains a valid phone number in the format +48 600 300 300.
Write a regular expression that checks if a string contains a valid date (only the format matters), e.g., 12-01-2024.
"""

import re

email_pattern = re.compile(r'^[\w-]+@[\w-]+.[\w-]+$')
url_pattern = re.compile(r'^https://[\w-]+.[\w-]+$')
phone_pattern = re.compile(r'^\+\d{2,3} \d{3} \d{3} \d{3}$')
date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')


def main() -> None:
    print(email_pattern.search('km@gmail.com'))
    print(url_pattern.search('https://km-programs.pl'))
    print(phone_pattern.search('+48 600 300 300'))
    print(date_pattern.search('12-01-2024'))


if __name__ == '__main__':
    main()