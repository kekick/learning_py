from string import ascii_lowercase, digits, ascii_uppercase
import random
import re


class EmailValidator:
    CHARS = ascii_lowercase + digits + ascii_uppercase + "_."

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        lst = random.choices(cls.CHARS, k=random.randint(10, 20))
        lst.append('@gmail.com')
        return ''.join(lst)

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            lst_email = email.split('@')
            if re.match(r'^[a-zA-Z0-9_.]{1,100}@[a-zA-Z0-9_.]{1,50}$', email) and '..' not in email and '.' in \
                    lst_email[1]:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


e = EmailValidator.get_random_email()
print(e)
