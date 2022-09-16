import re
import time


class BirthDay:
    def __init__(self, year, month, day, clock):

        self.year = BirthDay.check_year(year)
        self.leap = False
        if self.year % 100 != 0 and self.year % 4 == 0:
            self.leap = True
        self.month = BirthDay.check_month(month)
        self.day = BirthDay.check_day(day, self.month, self.leap)
        self.clock, self.hour, self.minute, self.second = BirthDay.check_clock(clock)
        self.Birthdate = time.strptime(f"{self.year}/{self.month}/{self.day} {self.clock}", '%Y/%m/%d %H:%M:%S')

    @property
    def to_birthday(self):
        now = time.localtime(time.time())
        # month-
        if now.tm_mon < self.month:
            month = self.month - now.tm_mon
        else:
            month = 12 - (now.tm_mon - self.month)
        if now.tm_mday < self.day:
            day = self.day - now.tm_mday
        else:
            month -= 1
            if self.month - 1 in [1, 3, 5, 7, 8, 10, 0]:
                day = 31 - now.tm_mday + self.day
            elif self.month - 1 in [2]:
                if self.leap:
                    day = 29 - now.tm_mday + self.day
                else:
                    day = 28 - now.tm_mday + self.day
            else:
                day = 30 - now.tm_mday + self.day
        if now.tm_hour < self.hour:
            hour = self.hour - now.tm_hour
        else:
            day -= 1
            hour = 24 - (now.tm_hour - self.hour)
        if now.tm_min < self.minute:
            minute = self.minute - now.tm_min
        else:
            hour -= 1
            minute = 60 - (now.tm_min - self.minute)
        if now.tm_sec < self.second:
            second = self.second - now.tm_sec
        else:
            minute -= 1
            second = 60 - (now.tm_sec - self.second)
        return [str(month), str(day), str(hour), str(minute), str(second) ]

    @property
    def year_old(self):
        # year month day hour minute second
        now = time.localtime(time.time())
        year = now.tm_year - self.year
        month = now.tm_mon - self.month
        if now.tm_mon < self.month:
            year -= 1
            month += 12
        day = now.tm_mday - self.day
        if now.tm_mday < self.day:
            month -= 1
            if self.month - 1 in [1, 3, 5, 7, 8, 10, 0]:
                day += 31
            elif self.month - 1 in [2]:
                if self.leap:
                    day += 29
                else:
                    day += 28
            else:
                day += 30
        if self.hour > now.tm_hour:
            day -= 1
            hour = 24 - abs(self.hour - now.tm_hour)
        else:

            hour = now.tm_hour - self.hour
        if self.minute > now.tm_min:
            hour -= 1
            minute = 60 - abs(self.minute - now.tm_min)
        else:

            minute = now.tm_min - self.minute
        if self.second > now.tm_sec:
            minute -= 1
            second = 60 - abs(self.second - now.tm_sec)
        else:

            second = now.tm_sec - self.second
        return [str(year), str(month), str(day),str(hour), str(minute), str(second)]

    def __str__(self):
        return f"{self.year}  {self.month}  {self.day}  {self.clock}"

    @classmethod
    def check_year(cls, year):
        regex = r"^\d{4}$"
        while True:
            if re.search(regex, year):
                year = int(year)
                if year >= (Y_now := time.localtime(time.time()).tm_year):
                    year = input(
                        f"you enter '{year}' which is '{int(year) - Y_now}' year from now\nenter a valid year\n--> ")
                    continue
                else:
                    return int(year)
            else:
                year = input(
                    f"Wrong year format you entered '{year}' as year : please enter a 4 digit year number : \n--> ")

    @classmethod
    def check_month(cls, month):
        regex = r"^\d{2}$|^\d{1}$"
        while True:
            if re.search(regex, month):
                month = int(month)
                if 13 > month > 0:
                    return month
                else:
                    month = input(
                        f"Wrong month you entered '{month}' as month , please enter month number 01 to 12 :\n--> ")
            else:
                month = input(
                    f"wrong month format you entered '{month}' as month , please enter a valid month number : \n--> ")

    @classmethod
    def check_day(cls, day, month, leap):
        regex1 = r"^\d{2}$|^\d{1}$"
        margin = 0
        month_list = [4, 6, 9, 11]
        if month in month_list:
            margin += 1
        if month == 2:
            margin = 3
            if leap:
                margin -= 1
        while True:
            if re.search(regex1, day):
                day = int(day)

                if 32 - margin > day > 0:
                    return day
                else:
                    day = input(f"Wrong day you entered '{day}' as day, please enter a day number 01 to 31 :\n--> ")
            else:
                day = input(f"wrong day format entered '{day}' as day , please enter a valid day number : \n--> ")

    @classmethod
    def check_clock(cls, clock: str):
        regex = r"^(\d{2}|\d{1}):(\d{2}|\d{1}):(\d{2}|\d{1})$"
        while True:
            if re.search(regex, clock):
                hour, minute, second = tuple(map(lambda y: int(y), clock.split(":")))
                hour = BirthDay.return_int(hour, "hour", 0, 24)
                minute = BirthDay.return_int(minute, "minute", 0, 59)
                second = BirthDay.return_int(second, "second", 0, 59)
                return ":".join([str(hour), str(minute), str(second)]), hour, minute, second
            else:
                clock = input(
                    f"wrong clock format you entered '{clock}' as clock,enter a valid one like example: 12:12:12\n--> ")

    @classmethod
    def return_int(cls, check, test_string, range_min, range_max):
        while True:
            try:
                check = int(check)
                if range_min <= check <= range_max:
                    return check
                else:
                    check = input(
                        f"enter a valid '{test_string}' number which is between '{range_min}' and '{range_max}'\n--> ")
                    continue
            except:
                print(f"wrong input for '{test_string}' \nenter a valid '{test_string}'")
                check = input(
                    f"number should be between '{range_min}' and '{range_max}'\n--> ")
def clear():
    print("*" * 10)
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')

if __name__ == '__main__':
    while True:
        year_user = input("please enter your Birth year in full 4 digit numbers : \n--> ")
        month_user = input("please enter your Birth month in numbers : \n--> ")
        day_user = input("please enter your Birth day in number : \n--> ")
        clock_user = input("please enter your Birth clock like (xx:xx:xx) : \n--> ")

        x = BirthDay(year_user, month_user, day_user, clock_user)
        while True:
            start = time.time()
            old ="\t".join(map(lambda y: (f"{y[1]:3s} {y[0]:10s}"), zip(["year", "month", "day", " hours", "minute" ,"second" ], x.year_old)))
            until_bday="\t".join(map(lambda y: (f"{y[1]:3s} {y[0]:10s}"), zip(["month", "day", " hours", "minute" ,"second" ], x.to_birthday)))
            clear()
            print("birth date : ",x)
            print(old, " old ")
            print(until_bday,"\tuntil birthday")
            end = time.time()-start
            time.sleep(1-end)
