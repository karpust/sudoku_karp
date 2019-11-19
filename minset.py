alsq = '010 038 060' \
       '000 001 045' \
       '590 000 000' \
       '000 390 100' \
       '650 000 000' \
       '000 160 020' \
       '000 614 000' \
       '007 000 000' \
       '000 000 809'


s = ''.join(i for i in alsq if i.isdigit())
set_all = {1, 2, 3, 4, 5, 6, 7, 8, 9}
all_str = [int(s[i]) for i in range(len(s))]
print(all_str)

def change_zero(some_lst):  # меняем ноль на множество
    ls = []
    for i in range(0, 81, 9):
        l = []
        for k in range(i, i+9):
            if some_lst[k] == 0:
                some_lst[k] = set()
            l.append(some_lst[k])
        ls.append(l)
    return ls


def make_vert(some_lst):
    ls = []
    for i in range(9):
        l = []
        for k in range(9):
            l.append(some_lst[k][i])
        ls.append(l)
    return ls


def make_sqw(some_lst):
    k = 0
    ls = []
    for n in range(0, 7, 3):
        i = n
        for m in range(3):
            l = []
            for i in range(i, i+3):
                for k in range(k, k+3):
                    l.append(some_lst[i][k])
                k -= 2
            ls.append(l)
            k += 3
            i -= 2
        k = 0
    return ls




gor_str = change_zero(all_str)  # создали горизонтальные строки из 9 списков с пустыми сетами и числами
vert_str = make_vert(gor_str)  # создали вертикальные строки из 9 списков с пустыми сетами и числами
sqw = make_sqw(gor_str)  # создали малые квадраты из 9 списков с пустыми сетами и числами

print(gor_str)


# убирает пересечение множеств возвращает число если оно одно во множестве
def min_set():
    for i in range(9):
        a = set()
        for k in range(9):
            if type(gor_str[i][k]) is set and gor_str[i][k] == 0:
                # a.add(some_lst[i][k])
        a.symmetric_difference_update(set_all)
        for k in range(9):
            if type(some_lst[i][k]) is set:
                if len(some_lst[i][k]) == 0:
                    some_lst[i][k].update(a)
                elif len(some_lst[i][k]) > 1:
                    c = (some_lst[i][k]).copy()
                    some_lst[i][k].intersection_update(a)
                    if len(some_lst[i][k]) < len(c):
                        global count
                        count += 1
                else:
                    global num_num
                    num_num += 1
                    some_lst[i][k] = list(some_lst[i][k])[0]