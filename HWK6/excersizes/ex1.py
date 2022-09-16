from abc import ABC, abstractmethod


class BaseMatrix(ABC):
    """base abstract class for matrix operations"""

    @abstractmethod
    def present_matrix(self) -> None:
        return None

    @abstractmethod
    def get_matrix(self) -> None:
        return None

    @abstractmethod
    def get_pos_values(self, height, width) -> None:
        return None

    @abstractmethod
    def set_pos_values(self, height, width, value) -> None:
        return None


class Matrix_(BaseMatrix):
    """"class for matrix operations"""

    def __init__(self, height: int, width: int, number_list=None):
        """"init method for Matrix"""
        if number_list is None:
            number_list = []
        self.matrix_dict = {}
        self.height = height
        self.width = width
        for h in range(height):
            for w in range(width):
                self.matrix_dict[(h, w)] = float(0)
        if len(number_list) > 0:
            prop = number_list
            while len(prop) <= height * width:
                prop.append(0)
            prop = prop[::-1]
            for i in range(height):
                for j in range(width):
                    buff = prop.pop()
                    self.set_pos_values(i, j, buff)

    def present_matrix(self) -> None:
        """method for presenting_matrix"""
        print(str(self))

    def get_matrix(self) -> dict:
        """"method for returning matrix dictionary with position and values"""
        return self.matrix_dict

    def get_pos_values(self, height: int, width: int) -> float:
        """
        method which by parsing height and width of favor ,
        if the height and width was in true dimension of Matrix,
         it will return the position value"""

        if (height, width) in self.get_matrix().keys():
            return self.get_matrix()[(height, width)]
        else:
            raise ValueError

    def set_pos_values(self, height: int, width: int, value: float) -> None:
        """this method can set the value to the position of the matrix"""
        if (height, width) in self.get_matrix().keys():
            self.matrix_dict[(height, width)] = float(value)
        else:
            raise ValueError

    def __repr__(self):
        return str(self)

    def __str__(self):
        """"returning the string representation of the matrix"""
        test_str = self.get_matrix()
        test_str = list(test_str.values())
        test_str = test_str[::-1]
        result = ""
        for h in range(self.height):
            for w in range(self.width):
                result += f"{str(test_str.pop()):10.10s}"
            result += "\n"

        return result

    @property
    def dimension(self):
        """returning the dimension of the matrix"""
        return self.height, self.width

    @property
    def has_determinant(self):
        """returning whether if matrix has determinant"""
        if self.height == self.width:
            return True
        return False

    @property
    def determinant(self):
        """returning determinant of the matrix"""
        if self.has_determinant:


            if self.height == 2:
                deter = (self.get_pos_values(0, 0) * self.get_pos_values(1, 1)) - (
                        self.get_pos_values(0, 1) * self.get_pos_values(1, 0))

                return deter
            # 1  2  3  4  5
            first_row = [x for x in self.matrix_dict.items() if x[0][0] == 0]
            sum_deter = 0
            counter = 1
            for head in first_row:
                new_head = head[1]
                others = [x[1] for x in self.matrix_dict.items() if x[0][1] != head[0][1] and x[0][0] != head[0][0]]
                others = others[::-1]

                new_matrix = Matrix_(self.height - 1, self.width - 1)
                for h in range(new_matrix.height):
                    for w in range(new_matrix.width):
                        new_matrix.set_pos_values(h, w, others.pop())
                if counter % 2 != 0:
                    flag = -1
                else:
                    flag = 1
                result_deter_new_matrix = new_head * (flag * new_matrix.determinant)
                sum_deter += result_deter_new_matrix
                counter += 1

            return sum_deter

        else:
            return None

    def __len__(self):
        """returning number of positions in matrix"""
        return len(self.matrix_dict.values())

    def __abs__(self):
        """abs of matrix is determinant of matrix"""
        return self.determinant

    def __add__(self, other):
        """add two matrices or one with int or float """
        if isinstance(other, Matrix_):
            if self.dimension == other.dimension:
                new = Matrix_(self.height, self.width)
                for h in range(self.height):
                    for w in range(self.width):
                        this = self.get_pos_values(h, w)
                        o_this = other.get_pos_values(h, w)
                        new.set_pos_values(h, w, float(this + o_this))
                return new
            else:
                raise ValueError("matrices must be in the same dimension")
        elif isinstance(other, float) or isinstance(other, int):
            for h in range(self.height):
                for w in range(self.width):
                    new = self.get_pos_values(h, w) + other
                    self.set_pos_values(h, w, float(new))
            return self
        else:
            raise ValueError("Other must be a Matrix or int or float")

    def __sub__(self, other):
        """sub two matrices or one with int or float """
        if isinstance(other, Matrix_):
            if self.dimension == other.dimension:
                new = Matrix_(self.height, self.width)
                for h in range(self.height):
                    for w in range(self.width):
                        this = self.get_pos_values(h, w)
                        o_this = other.get_pos_values(h, w)
                        new.set_pos_values(h, w, float(this - o_this))
                return new
            else:
                raise ValueError("matrices must be in the same dimension")

        elif isinstance(other, float) or isinstance(other, int):
            for h in range(self.height):
                for w in range(self.width):
                    new = self.get_pos_values(h, w) - other
                    self.set_pos_values(h, w, float(new))
            return self
        else:
            raise ValueError("Other must be a Matrix or int or float")

    def __truediv__(self, other):
        """divide matrix by int or float """
        if isinstance(other, Matrix_):
            raise ValueError("two matrices cant be divided by each other")
        elif isinstance(other, float) or isinstance(other, int):
            for h in range(self.height):
                for w in range(self.width):
                    new = self.get_pos_values(h, w) / other
                    self.set_pos_values(h, w, float(new))
            return self
        else:
            raise ValueError("Other must be int or float")

    def __mul__(self, other):
        """multiply matrices by each other or int or float"""
        if isinstance(other, Matrix_):
            if self.height == other.width:
                new = Matrix_(self.height, other.width)
                for h in range(new.height):
                    for w in range(new.width):
                        row_self = [row_element[1] for row_element in self.matrix_dict.items() if
                                    row_element[0][0] == h]
                        col_other = [col_element[1] for col_element in other.matrix_dict.items() if
                                     col_element[0][1] == w]
                        new_element = sum([x * y for x, y in zip(row_self, col_other)])
                        new.set_pos_values(h, w, new_element)
                return new
            else:
                raise ValueError("first matrix row dimension must be same other matrix col dimension")
        elif isinstance(other, float) or isinstance(other, int):
            for h in range(self.height):
                for w in range(self.width):
                    new = self.get_pos_values(h, w) * other
                    self.set_pos_values(h, w, float(new))
            return self
        else:
            raise ValueError("Other must be int or float")

    def __gt__(self, other):
        """return whether the matrix is greater than or equal to another matrix"""
        if self - other > 0:
            return True
        else:
            return False

    def __lt__(self, other):
        """return whether the matrix is smaller than or equal to another matrix"""
        if self - other < 0:
            return True
        else:
            return False

    def __eq__(self, other):
        """return whether the matrix is  equal to another matrix"""

        if self - other == 0:
            return True
        else:
            return False


class SquareMatrix(Matrix_):
    """defining squareMatrix which its has equal width and height"""

    def __init__(self, dim):
        """initializing the squareMatrix"""
        super(SquareMatrix, self).__init__(dim, dim)

    def main_diagonal(self):
        """main diagonal is elements which are incrementing in both width and height"""
        test_diagonal_main = []
        for x in range(self.height):
            test_diagonal_main.append(self.matrix_dict[(x, x)])
        return test_diagonal_main

    def sub_diagonal(self):
        """sub diagonal is elements which are incrementing in height and decrementing in width"""

        test_diagonal_main = []
        counter = self.height - 1
        for x in self.matrix_dict.items():
            if x[0][1] == counter:
                test_diagonal_main.append(x[1])
                counter -= 1
        return test_diagonal_main


def Matrix(height, width=None):
    """function which returns a matrix and checks if it is Square or normal matrix"""
    if width is None or height == width:
        return SquareMatrix(height)
    else:
        return Matrix_(height, width)


test1 = Matrix(2, 5)
# test1.present_matrix()
# print()
test1.set_pos_values(0, 0, 2)
# test1.present_matrix()
# print()
test1.set_pos_values(0, 1, 2)
test1.set_pos_values(0, 2, 2)
test1.set_pos_values(0, 3, 2)
test1.set_pos_values(0, 4, 2)
test1.set_pos_values(1, 0, 3)
test1.set_pos_values(1, 1, 3)
test1.set_pos_values(1, 2, 3)
test1.set_pos_values(1, 3, 3)
test1.set_pos_values(1, 4, 3)
# test1.present_matrix()
# print(len(test1))

test2 = Matrix(2, 5)
# test2.present_matrix()
# print()
test2.set_pos_values(0, 0, 1)
# test2.present_matrix()
# print()
test2.set_pos_values(1, 1, 1)
# test2.present_matrix()
# print(len(test2))
# test1.present_matrix()
# test2.present_matrix()
# print()
#
# print()
test3 = Matrix(5, 2)
test3.set_pos_values(0, 1, 2)
test3.set_pos_values(1, 1, 2)
test3.set_pos_values(2, 1, 2)
test3.set_pos_values(3, 1, 2)
test3.set_pos_values(4, 1, 2)
print("printing test 1 ")
test1.present_matrix()
print()
test3.present_matrix()
print("printing test 2 ")

print("printing test1 * test3 ")
print(test1 * test3)
# print(test1 + test2)
# print(test1 + 1)
# print(test1 - test2)
# print(test1 - 1)
# print(test1 / 2)
# print(test1 * 2)
# print(test1 * 2)

test_deter = Matrix(4, 4)
test_deter.set_pos_values(0, 0, 1)
test_deter.set_pos_values(0, 1, 0)
test_deter.set_pos_values(0, 2, 2)
test_deter.set_pos_values(0, 3, -1)
test_deter.set_pos_values(1, 0, 3)
test_deter.set_pos_values(1, 1, 0)
test_deter.set_pos_values(1, 2, 0)
test_deter.set_pos_values(1, 3, 5)
test_deter.set_pos_values(2, 0, 2)
test_deter.set_pos_values(2, 1, 1)
test_deter.set_pos_values(2, 2, 4)
test_deter.set_pos_values(2, 3, -3)
test_deter.set_pos_values(3, 0, 1)
test_deter.set_pos_values(3, 1, 0)
test_deter.set_pos_values(3, 2, 5)
test_deter.set_pos_values(3, 3, 0)
print("printing test deter ")
print()
test_deter.present_matrix()
print("printing test deter determinant")
print(test_deter.determinant)

test_square = SquareMatrix(3)
test_square.set_pos_values(0, 0, 1)
test_square.set_pos_values(0, 1, 2)
test_square.set_pos_values(0, 2, 3)
test_square.set_pos_values(1, 0, 4)
test_square.set_pos_values(1, 1, 5)
test_square.set_pos_values(1, 2, 6)
test_square.set_pos_values(2, 0, 7)
test_square.set_pos_values(2, 1, 8)
test_square.set_pos_values(2, 2, 9)
test_square.present_matrix()

print(test_square.main_diagonal())
print(test_square.sub_diagonal())
