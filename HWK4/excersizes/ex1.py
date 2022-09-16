import uuid
import hashlib
import getpass
import re


class User:
    __users = {}

    def __init__(self, input_username, password_input, phone_number=None):
        self.username = input_username
        self.phone_number = phone_number
        self.__password = User.__password_to_hash(password_input)
        self.id = User.uuid_generator()
        User.__users[self.username] = self

    def __str__(self):
        if self.phone_number is None:
            return f"username : {self.username}"
        else:
            return f"username : {self.username} phone : {self.phone_number}"

    @property
    def _getter_password(self):
        return self.__password

    @classmethod
    def uuid_generator(cls):  # 1 in every 2.71 quintillion collision detection
        if len(cls.__users) == 0:
            return uuid.uuid4()
        else:
            users_id = [x.id for x in User.__users.values()]
            while True:
                test = uuid.uuid4()
                if test not in users_id:
                    return test

    @classmethod
    def getting_users(cls):
        return list(cls.__users.keys())

    def setter_password(self, password=None):
        if User.check_password(password) is True:
            self.__password = User.__password_to_hash(password)
        else:
            self.__password = User.set_password()
        User.user_update(self)

    @staticmethod
    def check_password(password):
        if password is None:
            return False
        elif len(password) < 4:
            return False
        else:
            return True

    @staticmethod
    def set_password():
        while True:
            test_p = input("Enter your password:\n-->\t")
            if User.check_password(test_p):
                return User.__password_to_hash(test_p)
            else:
                print("Password most be at least 4 length")

    @staticmethod
    def __password_to_hash(password):
        salt = "ramin 12345"
        password_r = password + salt
        new_password = hashlib.sha256(password_r.encode("utf-8")).hexdigest()
        return new_password

    @classmethod
    def user_update(cls, user):
        cls.__users[user.username] = user

    @classmethod
    def sign_up(cls):
        print("creating user...")
        username = cls.input_username()
        password = cls.input_password(username)
        if cls.check_username(username) is False:
            print(f"{username} already exists")
            return None
        phone = cls.input_phone(username)
        if cls.check_password(password) is True:
            User(username, password, phone)
        else:
            print("cant create username.password must be >4 length")

    @classmethod
    def delete_user(cls, old_username):
        del cls.__users[old_username]

    @classmethod
    def sign_in(cls):
        print("signing in user...")
        username = cls.input_username()
        password = cls.__password_to_hash(cls.input_password(username))
        if cls.check_username(username) is True:
            return None
        if cls.__users[username].__password == password:
            print(f"signing in completed\nwelcome {username}")
            user = cls.signed_user(username)
            return user
        else:
            print("cant signing in, username or password is incorrect")
            return None

    @classmethod
    def signed_user(cls, username):
        user = cls.__users[username]
        return user

    def signed_api(self):
        user_signed_api_dict = {"1": ("info", self.info_api), "2": ("change_info", self.change_info_api),
                                "3": ("change_password", self.change_password_api), "4": ("quit", self.quit_api)}
        while True:
            [print(f"{y[0], y[1][0]}") for y in user_signed_api_dict.items()]
            y = input("please enter a number from above:\n-->\t")
            if y in user_signed_api_dict.keys():
                result_test = user_signed_api_dict[y][1]()
                if result_test == 4:
                    print(f"\nsigning out from {self.username}")
                    break
            else:
                print("\nwrong input only 1,2,3,4")
                continue

    def info_api(self):
        print(str(self))

    def change_info_api(self):
        while True:
            new_username = input("new username :\t-->\n")
            if new_username == self.username:
                print("username not changed")
                break
            elif self.__class__.check_username(new_username):
                old_username = self.username
                self.username = new_username
                User.delete_user(old_username)
                User.user_update(self)
                break
            else:
                print("duplicated username name")
                continue

        while True:
            new_phone = input("phone number ?(could be empty)\n-->\t")
            if new_phone:
                if self.__class__.phone_verification(new_phone):
                    self.phone_number = new_phone
                    User.user_update(self)
                    break
                else:
                    print("wrong phone format")
                    continue
            else:
                break

        return 2

    def change_password_api(self):
        p1 = getpass.getpass("please enter old password")
        p2 = getpass.getpass("please enter new password")
        p3 = getpass.getpass("please enter old password again")
        if (p3 == p2) and (User.__password_to_hash(p1) == self.__password) and (User.check_password(p2)):
            self.__password = User.__password_to_hash(p2)
            User.user_update(self)
            print("password changed successfully")
        else:
            print("wrong password format or new passwords not the same")

        return 3

    @staticmethod
    def quit_api():
        return 4

    @classmethod
    def check_username(cls, username):
        if username not in cls.__users.keys():
            return True
        else:
            return False

    @property
    def info(self):
        return str(self)

    @staticmethod
    def input_username():
        username = input("Enter your username:\n-->\t")
        return username

    @staticmethod
    def input_password(username):
        password_input_create = getpass.getpass(f"please enter {username} password:\t-->\t")
        return password_input_create

    @staticmethod
    def phone_verification(phone):
        regex = r"^\d{11}$"
        if re.search(regex, phone):
            return True
        else:
            return False

    @staticmethod
    def input_phone(username):
        while True:
            cond = input("do you wish to add phone number?(y/n)\n-->\t").strip()
            if cond == "y":
                while True:
                    phone = input(f"please enter {username} phone number :\n-->\t").strip()
                    if User.phone_verification(phone):
                        return phone
                    else:
                        print("wrong phone format e.g:09123456789")
                        continue
            elif cond == "n":
                return None
            else:
                print("wrong entry.please enter (y/n) only")
                continue


def quit_func():
    return 0


def sign_up():
    User.sign_up()
    return 1


def sign_in():
    user = User.sign_in()
    if isinstance(user, User):
        user.signed_api()
    elif user is False:
        print("no such user found")
    else:
        pass
    return 2


if __name__ == '__main__':
    user_api_dict = {"0": ("quit", quit_func), "1": ("sign up user", sign_up), "2": ("sign in user", sign_in)}
    while True:
        print(*User.getting_users(), sep="\t")
        [print(f"{x[0], x[1][0]}") for x in user_api_dict.items()]
        x = input("please enter a number from above:\n-->\t")
        if x in user_api_dict.keys():
            result = user_api_dict[x][1]()
            if result == 0:
                print("\ngoodbye")
                break
        else:
            print("\nwrong input only 0,1,2")
            continue
