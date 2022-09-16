from ex1 import User as user_temp, User
import json

class User(user_temp):
    def __init__(self,fullname,phone,email):
        super(User, self).__init__(fullname, phone, email)

    def to_json(self):
        filename=self.fullname+".json"
        with open(filename,"w") as f:
            s= json.dumps(self.dict_instance())
            f.write(s)

    @classmethod
    def from_json(cls,filename):
        try:
            with open(filename,"r") as f:
                s = dict(json.load(f))
                return User(*s.values())
        except FileNotFoundError:
            print(f"Could not find filename: {filename}")

if __name__ == '__main__':
    #
    # x = User("asghar","09124981090","yazdani@gmail.com")
    # x.to_json()
    y=User.from_json("asghar.json")

    print(y.dict_instance())