import logging

logger = logging.getLogger("person_logger")
log_format = logging.Formatter("%(asctime)s-(%(name)-10s) -%(levelname)-16s -%(message)s")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("person.log", "a", encoding="utf-8")
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)

class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger.log(logging.WARNING,"Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logger.log(logging.CRITICAL,"Invalid age!")
        self._age = 0
