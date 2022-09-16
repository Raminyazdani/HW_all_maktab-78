from uuid import uuid4
import psycopg2
import getpass


def connecting_to_postgresql(instance_list):
    def not_exist(cursor, instance):
        try:
            query = f"SELECT * FROM {instance.__class__.__name__};"
            print(query)
            cursor.execute(query)
        except:
            create_table(cursor, instance)

    def create_table(cursor, instance):
        postgresql_table_data_names_types = list(
            zip(list(vars(instance).keys()), instance.postgresql_table_data_types))

        query = f"Create Table {instance.__class__.__name__} ("
        for column, data_types in postgresql_table_data_names_types:
            query += f" {column} {data_types} ,"
        query = query[:-1]
        query += ");"
        print(query)
        cursor.execute(query)

    def insert_instance(cursor, instance):
        query = f"INSERT INTO {instance.__class__.__name__} ("
        test_keys = list(vars(instance).keys())

        test_values = list(vars(instance).values())

        for keys in test_keys:
            query += keys + ","
        query = query[:-1]
        query += ") values ("
        for values in test_values:
            if isinstance(values, int):
                query += f"{values}" + ","
                continue
            query += f"'{values}'" + ","
        query = query[:-1]
        query += ")"
        print(query)
        cursor.execute(query)

    def insert_into(cursor, instance):
        not_exist(cursor, instance)
        insert_instance(cursor, instance)

        # cursor.execute(query)

    password = getpass.getpass(prompt='Enter your password : \n--> ')
    con = psycopg2.connect(dbname="models_test", user="postgres", password=f"{password}")
    con.autocommit = True

    with con.cursor() as cursor:
        for instances in instance_list:
            insert_into(cursor, instances)



def generate_uuid():
    temp = uuid4().hex
    return temp


class Student:
    postgresql_table_data_types = ["VARCHAR(32)", "VARCHAR(32)", "INTEGER", "VARCHAR(64)", "VARCHAR(64)",
                                   "UUID NOT NULL" ]

    def __init__(self, name, surname, age, national_id, degree):
        self.name = name
        self.surname = surname
        self.age = age
        self.national_id = national_id
        self.degree = degree
        self.id = generate_uuid()


class Teacher:
    postgresql_table_data_types = ["VARCHAR(32)", "VARCHAR(32)", "UUID NOT NULL"]

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = generate_uuid()


class Course:
    postgresql_table_data_types = ["VARCHAR(32)", "UUID NOT NULL", "UUID NOT NULL"]

    def __init__(self, study, teacher_id):
        self.study = study
        self.teacher_id = teacher_id
        self.id = generate_uuid()


class CourseStudent:
    postgresql_table_data_types = ["UUID NOT NULL", "UUID NOT NULL", "UUID NOT NULL"]

    def __init__(self, course_id, Student_id):
        self.course_id = course_id
        self.Student_id = Student_id
        self.id = generate_uuid()


instance_student = Student("ramin", "yazdani", 12, "0020349629", "masters")
instance_teacher = Teacher("seyed", "jeff")
instance_course = Course("math", generate_uuid())
instance_course_student = CourseStudent(generate_uuid(), generate_uuid())
istance_student_2= Student("radin","yazdani",35,"0020020000","bachelor")
list_instances=[instance_student,instance_teacher,instance_course,instance_course_student,istance_student_2]

connecting_to_postgresql(list_instances)
# print(uuid4().int)
# print(Student.__name__)
#
# print(type(uuid4().int))
# print(len(str(uuid4().int)))
