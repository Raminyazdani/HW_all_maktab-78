import re
import inspect


class Person:
    count = 0
    persons = {}

    def __init__(self, name, gender=None, email=None):
        self.name = name
        if check_gender(gender) == True:
            self.gender = gender
        else:
            self.gender = get_gender(name)
        if check_email(email) == True:
            self.email = email
        else:
            self.email = get_email(name)
        Person.count += 1
        Person.persons[name] = self
    @classmethod
    def object_keys(cls):
        return props(cls)
    def __str__(self):
        x = str(type(self))
        x=x[x.index("."):x.index(">")][1:-1]
        return f"{x}:{self.name}"
class Writer(Person):
    count = 0

    def __init__(self, name, gender, email, writer_ID, genre):
        self.writer_id = writer_ID
        self.genre = genre
        super(Writer, self).__init__(name, gender, email)
        Writer.count += 1


class Poet(Person):
    count = 0

    def __init__(self, name, gender, email, style):
        self.style = style
        super(Poet, self).__init__(name, gender, email)
        Poet.count += 1


class Researcher(Person):
    count = 0

    def __init__(self, name, gender, email, field, university):
        self.field = field
        self.university = university
        super(Researcher, self).__init__(name, gender, email)
        Researcher.count += 1


class Literature:
    count = 0
    literatures = {}

    def __init__(self, title, authors):
        self.title = title
        if check_authors(authors, title) == True:
            self.authors = list(set(authors))
        else:
            self.authors = list(set(get_authors(title)))
        Literature.count += 1
        Literature.literatures[title] = self
    @classmethod
    def object_keys(cls):
        return props(cls)
    def __str__(self):
        x = str(type(self))
        x = x[x.index("."):x.index(">")][1:-1]
        return f"{x}:{self.title}"

class author_get:

    def __init__(self, authors):
        self.authors = authors

    def authors_list_ret(self):
        return self.authors


class Book(Literature, author_get):
    count = 0

    def __init__(self, title, authors, ISBN, publisher):
        self.ISBN = check_ISBN(ISBN)
        self.publisher = publisher
        super(Book, self).__init__(title, authors)
        Book.count += 1


class Poem(Literature):
    count = 0

    def __init__(self, title, authors, form):
        if check_authors(authors, title,"poem") == True:
            author = authors
        else:
            author = get_authors(title,cond="poem")
        self.form = form
        super(Poem, self).__init__(title, author)
        Poem.count += 1


class Article(Literature, author_get):
    count = 0

    def __init__(self, title, authors, magazine, year):
        self.magazine = magazine
        self.year = get_year(year, title)
        super(Article, self).__init__(title, authors)
        Article.count += 1


def check_year(year):
    regex = "^\d{4}$"
    if re.search(regex, year):
        return True
    return False


def get_year(year, title):
    while True:
        if check_year(year) == True:
            return year
        else:
            print(f"wrong year type for {title}\n enter a valid one")
            year = input("year :\n-->\t")


def check_ISBN(ISBN):
    # regex = "^(?:ISBN(?:-1[03])?:?●)?(?=[-0-9●]{17}$|[-0-9X●]{13}$|[0-9X]{10}$)(?:97[89][-●]?)?[0-9]{1,5}[-●]?(?:[0-9]+[-●]?){2}[0-9X]$"
    # regex = "^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$"
    regex = "^[0-9\- ]{10,17}X?$"
    while True:
        if re.search(regex, ISBN):
            return ISBN
        else:
            print("wrong ISBN format.only CFF  ISBN format is correct")
            print("ISBN example : '978-3-16-148410-0'")
            ISBN = input("ISBN : \n-->\t")



def check_authors(list_authors, title,cond=None):
    if cond =="poem":
        if len(list_authors)>1:
            return False
    corrects = []
    incorrects = []
    if not isinstance(list_authors, list):
        list_authors = [list_authors]
    for people in list_authors:
        if isinstance(people, Person):
            corrects.append(people)
        elif isinstance(people, str):
            if people in Person.persons.keys():
                corrects.append(Person.persons[people])
            else:
                incorrects.append(people)
        else:
            incorrects.append(people)
    if len(incorrects) > 0:
        print(f"there are {len(corrects)+len(incorrects)} authors for {title}")
        print("these peoples are incorrects thou they are not listed in persons : ",end="")
        print(*incorrects, "\t")
        if len(corrects)>0:
            print("these peoples are incorrects thou they are not listed in persons : ",end="")
            print(*corrects, "\t")
        return False
    return True


def get_authors(title, cond=None, author=None):
    while True:
        if cond == None:
            test = input(f"please enter '{title}' authors count:\n-->\t")
            test = int_maker(test, title)
            authors = []
            for iterates in range(test):
                while True:
                    author = input(f"please enter {iterates + 1} author name : ")
                    if author in Person.persons.keys():
                        authors.append(Person.persons[author])
                        break
                    else:
                        print("author not in people list below : ")
                        print(*Person.persons.keys())
                        test = input("do you wish to add it as a person to list ?(y/n)")
                        if test == "y":

                            dump = Person(author)
                            authors.append(dump)
                            break
                        else:
                            continue
        else:
            if cond == "poem":
                test = 1
                authors = []
                for iterates in range(test):
                    while True:
                        author = input(f"please enter {iterates + 1} author name : ")
                        if author in Person.persons.keys():
                            authors.append(Person.persons[author])
                            break
                        else:
                            print("author not in people list below : ")
                            print(*Person.persons.keys())
                            test = input("do you wish to add it as a person to list ?(y/n)")
                            if test == "y":
                                dump = Person(author)
                                authors.append(dump)
                                break
                            else:
                                continue

            else:
                cond = None
                continue
        if check_authors(authors, title):
            result = []
            for pep in authors:
                if isinstance(pep, Person):
                    result.append(pep)
                else:
                    result.append(Person.persons[pep])
            return result
        else:
            print("restarting getting authors name...")
            continue


def check_gender(gender):
    if gender in ["male", "female"]:
        return True
    else:
        return False


def get_gender(name):
    while True:
        gender = input(f"please enter a valid gender for {name}:\n-->\t")
        if check_gender(gender) == True:
            return gender
        else:
            print("wrong gender only 'male/female'")


def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if email == None:
        return False
    if re.search(regex, email):
        return True
    else:
        return False


def int_maker(test, input_type, criteria=None):
    while True:
        try:
            test = int(test)
            if criteria == None:
                return test
            else:
                if criteria:
                    return test
                else:
                    raise
        except:
            test = input(f"wrong input for {input_type} please enter a valid one:\n-->\t")
            try:
                return int_maker(test, input_type, (int(test) > 0))
            except:
                continue


def get_email(name):
    while True:
        email = input(f"please enter a valid email for {name}:\n-->\t")
        if check_email(email) == True:
            return email
        else:
            print("wrong email format")


def props(cls):
    return str(inspect.signature(cls.__init__))[1:-1].replace(" ", "").replace("=None","").split(",")[1:]

def clear():
    print("*"*20)
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')

if __name__ == '__main__':
    creates_person = []
    creates_Litratures =[]
    add_count = 0
    while True:
        for items in Person.persons.values():
            if items not in creates_person:
                creates_person.append(items)

        for items in Literature.literatures.values():
            if items not in creates_Litratures:
                creates_Litratures.append(items)
        clear()
        print("peoples : \n\t", end="")
        print(*creates_person, sep="\t")
        print("******")
        print("Literatures : \n\t", end="")
        print(*creates_Litratures, sep="\t")
        print("******")
        print("what do you want to add ?:")
        items = ["person", "writer", "poet", "researcher", "Literature", "Book", "Poem", "Article"]
        objects = [Person, Writer, Poet, Researcher,Literature, Book, Poem, Article]
        indicators = list(range(1, len(items) + 1))
        print(*map(lambda x: f"{x[1]}:{x[0]}", zip(items, indicators)), sep="\t")
        x = input("number of above:\n-->\t")
        try:
            clear()
            print("peoples : \n\t",end="")
            print(*creates_person, sep="\t")
            print("******")
            print("Literatures : \n\t",end="")
            print(*creates_Litratures, sep="\t")
            print("******")
            x = int(x) - 1
            if x not in range(len(objects)):
                raise ValueError
            obj = objects[x]
        except:
            print("wrong number,please enter a valid number")
            continue
        else:
            get_keys = (obj.object_keys())
            keys = []
            for key in get_keys:
                if key == "authors":
                    if isinstance(obj,Poem):
                        keys.append([input(f"enter {items[x]} key: {key}:\n-->\t").strip()])
                        continue
                    else:
                        keys.append(input(f"enter {items[x]} key: {key}:\n-->\t").split())
                        continue
                keys.append(input(f"enter {items[x]} key: {key}:\n-->\t"))
            if x in [0,1,2,3]:
                creates_person.append(obj(*keys))

            else:
                creates_Litratures.append(obj(*keys))


            add_count+=1