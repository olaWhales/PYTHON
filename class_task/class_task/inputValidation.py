import re
from re import match


def validation(*user):
    validation = r'\d[A-Z][a-z]*'
    for checking in user:
        if checking == re.fullmatch(validation, checking):
            # if match(validation, checking):
            return True
        else:
            return "invalid input value"


user_input = str("2Lawale")
print(validation(user_input))
