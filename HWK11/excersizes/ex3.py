import datetime
import jdatetime


def create_datetime(string: str) -> datetime:
    print(string)
    return datetime.datetime.strptime(string, "%Y/%m/%d %H:%M:%S")


def get_time(types: str) -> datetime:
    while True:
        test = input(f"please enter **{types}** date and time in this format\n"
                     "%Y/%m/%d %H:%M:%S\n-->")
        try:
            result = create_datetime(test)
            return result
        except:
            print("Invalid date format")
            continue


def seconds_between(date1, date2) -> float:
    return abs((date1 - date2).total_seconds())


def is_leap(year: int) -> int:
    if ((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))):
        return True
    return False


def leap_years(date1: datetime, date2: datetime) -> int:
    year_start = date1.year
    year_end = date2.year
    leaps = 0
    print(year_start, " years", year_end)
    for year in range(year_start, year_end):
        if is_leap(year):
            leaps += 1

    return leaps


def clock_change(date1: datetime, date2: datetime) -> int:
    clock_change_freq = 0

    temp = date1
    while temp < date2:
        if is_leap(temp.year):
            if temp.day == 20 and temp.month == 3:
                clock_change_freq += 1
            elif temp.day == 21 and temp.month == 9:
                clock_change_freq += 1
        else:
            if temp.day == 21 and temp.month == 3:
                clock_change_freq += 1
            elif temp.day == 22 and temp.month == 9:
                clock_change_freq += 1
        temp += datetime.timedelta(days=1)
    return clock_change_freq


def to_jalali(date):
    return jdatetime.datetime.fromgregorian(year=date.year, month=date.month, day=date.day, hour=date.hour,
                                            minute=date.minute, second=date.second)


if __name__ == '__main__':
    start_time:datetime = get_time("first")
    end_time:datetime = get_time("second")

    #tests
    # start_time = create_datetime("2010/08/12 12:12:12")
    # end_time = create_datetime("2022/08/17 12:12:13")

    if start_time > end_time:
        start_time, end_time = end_time, start_time
    seconds: datetime.datetime.second = seconds_between(start_time, end_time)
    leaps: int = leap_years(start_time, end_time)
    freq: int = clock_change(start_time, end_time)
    start_time_j = to_jalali(start_time)
    end_time_j = to_jalali(end_time)
    print("seconds between start and endtime : ",seconds)
    print("number of leap years : ",leaps)
    print("clock change frequency : " , freq)
    print(start_time ," <-georgian  :  jalali-> " ,start_time_j)
    print(end_time ," <-georgian  :  jalali-> " ,end_time_j)
