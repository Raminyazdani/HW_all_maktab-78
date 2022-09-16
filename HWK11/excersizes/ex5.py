import datetime
from ex3 import create_datetime , get_time

# def create_datetime(string: str) -> datetime:
#     return datetime.datetime.strptime(string, "%Y/%m/%d %H:%M:%S")
#
#
# def get_time(types: str) -> datetime:
#     while True:
#         test = input(f"please enter **{types}** date and time in this format\n"
#                      "%Y/%m/%d %H:%M:%S\n-->")
#         try:
#             result = create_datetime(test)
#             return result
#         except:
#             print("Invalid date format")
#             continue


def generate_days(start_time, end_time, day):
    temp = start_time
    while temp <= end_time:
        if temp.weekday() == day:

            yield temp

        temp += datetime.timedelta(days=1)


if __name__ == '__main__':
    # start_time: datetime = get_time("first")
    # end_time: datetime = get_time("second")

    # tests
    start_time = create_datetime("2010/08/12 12:12:12")
    end_time = create_datetime("2022/08/28 12:12:13")
    if start_time > end_time:
        start_time, end_time = end_time, start_time
    weekday_n=[0,1,2,3,4,5,6]
    weekdays=["saturday" ,"sunday","monday","tuesday","wednesday","thursday","friday"]
    weekday_n_change=[5,6,0,1,2,3,4]
    dictionary_weekday=list(zip(weekday_n,weekdays))
    new_zip = list(zip(weekday_n,weekday_n_change))
    while True:
        [print(x[0],":",x[1]) for x in dictionary_weekday]
        day = input("please enter a number between 0 to 6\nsaturday to friday in numbers\n-->")
        try:
            day = int(day)
        except:
            print("invalid input only numbers")
            continue
        if 0 <= day <= 6:
            print(f"you choose {dictionary_weekday[day][1]}")
            day = new_zip[day][1]
            break
        else:
            print("only 0 to 6")
            continue

    days = generate_days(start_time, end_time, day)
    temp = next(days)
    print(temp.strftime("%Y-%m-%d %A"))
    while True:
        try:
            temp = next(days)
            cond = input("for continuing generating days only enter ")
            if cond:
                break
            print(temp.strftime("%Y-%m-%d %A"))
        except StopIteration:
            break

    print("end of the generator")
