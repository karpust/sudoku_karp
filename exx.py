from string import ascii_letters
alsq = '010 038 060' \
       '000 001 045' \
       '590 000 000' \
       '000 390 100' \
       '650 000 000' \
       '000 160 020' \
       '000 614 000' \
       '007 000 000' \
       '000 000 809'

set_all = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Sudoku:
    def __init__(self, source):
        self.source = source

    def str_to_list(self):
        self.source = ''.join(i for i in alsq if i.isdigit())
        return [int(self.source[i]) for i in range(len(self.source))]

    def change_zero(self, gor_line):  # меняем ноль на множество
        ls = []
        for i in range(0, 81, 9):
            l = []
            for k in range(i, i + 9):
                if gor_line[k] == 0:
                    gor_line[k] = set()
                l.append(gor_line[k])
            ls.append(l)
        return ls

    def make_vert(self, some_lst):
        ls = []
        for i in range(9):
            l = []
            for k in range(9):
                l.append(some_lst[k][i])
            ls.append(l)
        return ls

    def make_sqw(self, some_lst):
        k = 0
        ls = []
        for n in range(0, 7, 3):
            i = n
            for m in range(3):
                l = []
                for i in range(i, i + 3):
                    for k in range(k, k + 3):
                        l.append(some_lst[i][k])
                    k -= 2
                ls.append(l)
                k += 3
                i -= 2
            k = 0
        return ls

    def __getitem__(self, key):
        return ascii_letters[key]

    # убирает пересечение множеств возвращает число если оно одно во множестве
    def min_set(self, some_lst=None, second_lst=None):
        for i in range(9):
            a = set()
            for k in range(9):
                if type(some_lst[i][k]) is not set:
                    a.add(some_lst[i][k])
            a.symmetric_difference_update(set_all)
            for k in range(9):
                if type(some_lst[i][k]) is set:
                    if len(some_lst[i][k]) == 0:
                        some_lst[i][k].update(a)
                    elif len(some_lst[i][k]) > 1:
                        c = (some_lst[i][k]).copy()
                        some_lst[i][k].intersection_update(a)
                        if len(some_lst[i][k]) < len(c):
                            self.min_set(second_lst)
                            global count
                            count += 1
                    else:
                        global num_num
                        num_num += 1
                        some_lst[i][k] = list(some_lst[i][k])[0]
                        self.min_set(second_lst)
        return

    # Для единственного в строке: 5283 257 789 т е 9:
    def one_from_all(self, all_lst):
        for lst in all_lst:
            l = []
            for elem in lst:
                if type(elem) is set:
                    l += (list(elem))
            for elem in lst:
                if type(elem) is set:
                    for el in elem:
                        if l.count(el) == 1:
                            elem.intersection_update({el})
                            break

    # Для двух возможных в строке: 347 и 3587 и больше нигде нет 37 оставит в них только 37
    def two_from_all(self, all_lst):
        for lst in all_lst:
            a = set()
            l = []
            for elem in lst:
                if type(elem) is set:
                    l += (list(elem))
            for elem in lst:
                if type(elem) is set:
                    for el in elem:
                        if l.count(el) == 2:
                            a.add(el)
            for elem in lst:
                if type(elem) is set:
                    i = 0
                    b = elem.intersection(a)
                    if len(b) == 2:
                        for elem in lst:
                            if type(elem) is set:
                                if b <= elem:
                                    i += 1
                    if i == 2:
                        for elem in lst:
                            if type(elem) is set:
                                if b <= elem:
                                    elem.intersection_update(b)
                                    global g
                                    g += 1

    # если по два одинаковых в двух клетках: 46 и 64 то уберет из других 46
    def two_from_two(self, all_lst):
        for lst in all_lst:
            i = 0
            for elem in lst:
                i = 0
                if type(elem) is set and len(elem) == 2:
                    a = elem.copy()
                    for elem in lst:
                        if type(elem) is set:
                            if a <= elem and len(elem) == 2:
                                i += 1
                    if i == 2:
                        for el in a:
                            for elem in lst:
                                if type(elem) is set:
                                    if a <= elem and len(elem) == 2:
                                        pass
                                    elif el in elem:
                                        elem.remove(el)
                                        global g
                                        g += 1

    def check_for_rep(self, all_lst):
        l = list(set_all)
        for lst in all_lst:
            for i in range(9):
                score = lst.count(l[i])
                if score > 1:
                    print('неверное решение')


class GorLine(Sudoku):
    def __init__(self, source):
        Sudoku.__init__(self, source)
        self.gorline = self.change_zero(self.str_to_list())

    def show(self):
        print('gorline =', self.gorline)

    def min(self, some_lst=None, second_lst=None):
        self.min_set(some_lst=self.gorline, second_lst=self.vertline)


class VertLine(GorLine):
    def __init__(self, source):
        GorLine.__init__(self, source)
        self.vertline = self.make_vert(self.gorline)

    def show(self):
        print('vertline =', self.vertline)

    def min(self, some_lst=None, second_lst=None):
        self.min_set(some_lst=self.vertline, second_lst=self.sqw)


class SmalSquare(GorLine):
    def __init__(self, source):
        GorLine.__init__(self, source)
        self.sqw = self.make_sqw(self.gorline)

    def min(self, some_lst=None, second_lst=None):
        self.min = self.min_set(some_lst=self.sqw, second_lst=self.gorline)

    def show(self):
        print('sqw =', self.min)





g = GorLine(alsq)
g.show()
v = VertLine(g)
v.show()
sqw = SmalSquare(g)
sqw.show()
sqw.min()