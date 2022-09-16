from string import ascii_letters
import re


# classes for validation exceptions:
class ValidationError(Exception):
    # base exception for validation errors
    def __init__(self, message, value=None):
        self.message = message
        self.value = value

    def __str__(self):
        print("ValidationError: %s %s" % (self.message, self.value))
        return f"{self.value} ERROR:-> {self.message}"


class NameValidationError(ValidationError):
    def __init__(self, name, message):
        self.name = name
        self.message = message
        super(NameValidationError, self).__init__(message, name)


class PhoneValidationError(ValidationError):
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message
        super(PhoneValidationError, self).__init__(message, phone)


class EmailValidationError(ValidationError):
    def __init__(self, email, message):
        self.email = email
        self.message = message
        super(EmailValidationError, self).__init__(message, email)


# name validation function
# criteria : 4<=len<=14 & only ascii_letters or '_' allowed
def name_validation_no_regex(name):
    test = list(ascii_letters)
    test.append("_")
    if isinstance(name, str):
        if 4 <= len(name) <= 14:
            if all([x for x in name if x in test]):
                return True
    return False


# name validation function using RegEX
# criteria : 4<=len<=14 & only ascii_letters or '_' allowed
def name_validation(name):
    pattern = r"^[a-zA-Z]{4,14}$"
    pattern = re.compile(pattern)
    result = pattern.match(name)
    if result:
        return True
    else:
        return False

    # email validator function using RegEX:


def email_validation(email):
    # pattern example : name@email.com
    pattern = r"^\w+@{1}\w+.com$"
    pattern = re.compile(pattern)
    result = pattern.match(email)
    if result:
        return True
    else:
        return False

    # phone validator function using RegEX:

def phone_validation(phone):
    pattern = r"^(09\d{9}$)|(\+989\d{9}$)"
    if re.match(pattern, phone):
        return True
    return False


# first type of validation method:
# {
class Fullname:
    def __get__(self, obj, obj_type=None):
        return self.value

    def __set__(self, obj, value):
        if name_validation(value):
            self.value = value
        else:
            raise ValidationError("Invalid fullname format", value)
    # }


# }

# second type of validation method:
# {
class Phone:
    def __get__(self, obj, obj_type=None):
        return self.value

    def __set__(self, obj, value):
        if phone_validation(value):
            self.value = value
        else:
            raise ValidationError("Invalid phone format", value)


# }

# third type of validation method:
# {
class Email:
    def __get__(self, obj, obj_type=None):
        return self.value

    def __set__(self, obj, value):
        if email_validation(value):
            self.value = value
        else:
            raise ValidationError("Invalid email format", value)


# }
class User:
    # validation method continue:
    # {
    fullname = Fullname()
    phone = Phone()
    email = Email()
    vars_clas=["fullname","phone","email"]
    # }
    def __init__(self, fullname, phone, email):
        self.fullname = fullname
        self.phone = phone
        self.email = email

    def dict_instance(self):
        return {"fullname":self.fullname, "phone":self.phone, "email":self.email}


if __name__ == '__main__':

    x = User("ramin", "09124981090", "yazdani@gmail.com")
    print(x.fullname)
    print(x.phone)
    print(x.email)
    print(x.dict_instance())
    x = User("ramin", "+989124981090", "yazdani@gmail.com")
    print(x.fullname)
    print(x.phone)
    print(x.email)
    print(x.dict_instance())