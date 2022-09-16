import pickle
import re
import dill


class User:

    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id}: {self.first_name} {self.last_name} <{self.phone}>"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


def add_to_file(user_list, file, mode):
    file_output = open(file, mode)
    for user in user_list:
        file_output.write(repr(user))
        file_output.write("\n")
    file_output.close()


user_files = open("users.pickled", "rb")
users = pickle.load(user_files)
user_files.close()

pattern_re = "^0919\d{7}$"

users_list = []
for user in users:
    users_list.append(user)
    x = re.match(pattern_re, user.phone)

output1_list = sorted(users_list, key=lambda x: x.id)
output2_list = list(filter(lambda x: re.match(pattern_re, x.phone) is not None, users_list))

add_to_file(output1_list, "output-q-3-1.txt", "w")
add_to_file(output2_list, "output-q-3-2.txt", "w")

file_output3 = open("output-q-3-3.dill", "wb")
for user in users_list:
    dill.dump(user, file_output3)
file_output3.close()


