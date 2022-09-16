from person import Person
import logging

logger = logging.getLogger("sample_logger")

log_format = logging.Formatter("%(asctime)s-(%(name)-10s) -%(levelname)-16s -%(msecs)s:-%(message)s")
file_handler = logging.FileHandler("sample.log", "a")
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
#--------------------------------
#create stream_handler
stream_format = logging.Formatter("%(asctime)s-%(levelname)-16s-%(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_format)
stream_handler.setLevel(logging.ERROR)
logger.addHandler(stream_handler)
def sub(a, b):
    if b != 0:
        logger.log(logging.DEBUG,"a/b=" + str(a / b))  # move to this line
        return a / b
        # logging.debug("a/b=" + str(a / b)) 
        # """
        #  line 11 : thichvaght ejra nemishada chon return ghable khate 20 bood.
        # bekhatere level e ejra e dibug va info ham khate 20 ejra nemishe
        # """
    logger.log(logging.ERROR,"Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)


def show_logs(file_path : str,log_level : str):
    log_levels = ["DEBUG","INFO","WARNING","ERROR","FATAL","CRITICAL"]
    base_level = log_levels[(log_levels.index(f"{log_level}")):]
    result_list = []
    my_file = open(f"{file_path}",mode="r")
    my_file_read = my_file.readlines()
    for item in base_level:
        for line in my_file_read:
            if item in line:
                result_list.append(line)
    return result_list

for item in show_logs("person.log","INFO"):
    print(item)