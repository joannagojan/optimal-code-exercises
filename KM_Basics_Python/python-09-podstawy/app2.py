"""
Write a function that takes a string representing a PESEL number as an argument.
The function returns a message in the form of a string, which includes information about whether
the owner of he PESEL number is male or female, and the year in which the person was born.

pesel structure:
YYMMDDNNNXC

    YY - Year of birth
    MM - Month of birth (with an added number for centuries,
                        people born in 2000 - 2099: added 20, 21-32
                        2100 - 2199: added 40 , 41-52
                        2200 - 2299: added 60.) 61-72
    DD - Day of birth
    NNN - Individual serial number
    X - Gender (even for female, odd for male)
    C - Control digit (calculated using a specific algorithm)
"""

import datetime


def get_month_from_number(month_number: int) -> str:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if 12 >= month_number >= 1:
        return months[month_number - 1]
    else:
        raise ValueError("Not between 1 and 12 to be a month")


# #cases:
# January: 31 days
# February: 28 days (29 days in a leap year)
# March: 31 days
# April: 30 days
# May: 31 days
# June: 30 days
# July: 31 days
# August: 31 days
# September: 30 days
# October: 31 days
# November: 30 days
# December: 31 days

def pesel_date_of_birth(pesel: str) -> str:

    #TODO validate pesel format

    month_number = int(pesel[2] + pesel[3])
    month = 0
    year_number  = int(pesel[0] + pesel[1])
    year = 0

    if 21 <= month_number <= 32:
        year = year_number + 2000
        month = month_number - 20
    elif 41 <= month_number <= 52:
        year = year_number + 2100
        month = month_number - 40
    elif 61 <= month_number <= 72:
        year = year_number + 2200
        month = month_number - 60
    elif 1 <= month_number <= 12:
        year = year_number + 1900
        month = month_number
    else:
        raise ValueError('Not a correct month number in pesel')

    print(year, month)

    day = int(pesel[4] + pesel[5])
    print(day)
    if month in [1,3, 5, 7, 8, 10, 12] and day > 31:
        raise ValueError('These months do have more days than 31')
    elif month in [4, 6, 9, 11] and day > 30:
        raise ValueError('These months do have more days than 30')
    elif month == 2:
        if year % 4 == 0 and day > 29:
            raise ValueError('Days in February in a leap year are not bigger than 29')
        elif day > 28:
            raise ValueError('Days in February in a non leap year are not bigger than 28')
    elif month > 12:
        raise ValueError('The month number is not correct in pesel')
    else:
        month_name = get_month_from_number(month)
        return f'Date of birth is: {day} {month_name} {year}. '


def pesel_gender(pesel: str) -> str:
    if int(pesel[-2]) % 2 == 0:
        return "It is a woman. "
    else:
        return "It is a man. "


def main() -> None:
    try:
        pesel = '9803247860'
        print(pesel_date_of_birth(pesel) + pesel_gender(pesel))
        print(pesel_date_of_birth('98010909680'))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()










