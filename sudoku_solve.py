s1 = [5, 3, 0, 0, 7, 0, 0, 0, 0]
s2 = [6, 0, 0, 1, 9, 5, 0, 0, 0]
s3 = [0, 9, 8, 0, 0, 0, 0, 6, 0]
s4 = [8, 0, 0, 0, 6, 0, 0, 0, 3]
s5 = [4, 0, 0, 8, 0, 3, 0, 0, 1]
s6 = [7, 0, 0, 0, 2, 0, 0, 0, 6]
s7 = [0, 6, 0, 0, 0, 0, 2, 8, 0]
s8 = [0, 0, 0, 4, 1, 9, 0, 0, 5]
s9 = [0, 0, 0, 0, 8, 0, 0, 7, 9]
al = (s1, s2, s3, s4, s5, s6, s7, s8, s9)
alsq ='530 070 000' \
     '600 195 000' \
     '098 000 060' \
     '800 060 003' \
     '400 803 001' \
     '700 020 006' \
     '060 000 280' \
     '000 419 005' \
     '000 080 079'

s = ''.join(i for i in alsq if i.isdigit())
set_all = {1, 2, 3, 4, 5, 6, 7, 8, 9}
gor_str = [int(s[i]) for i in range(len(s))]
num_num = 0
#vert_str = [int(s[i]) for k in range(9) for i in range(k, len(s), 9)]
#sqw = []
#[sqw.append(int(s[m])) for i in range(0, 9, 3) for k in range(i, i+21, 9) for m in range(k, k+3)]
#[sqw.append(int(s[m])) for i in range(27, 36, 3) for k in range(i, i+21, 9) for m in range(k, k+3)]
#[sqw.append(int(s[m])) for i in range(54, 63, 3) for k in range(i, i+21, 9) for m in range(k, k+3)]


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


# создает множество с элементами которых нет в основном списке
def make_set(all_lst):
  for lst in all_lst:
      a = set()
      for elem in lst:
          if type(elem) is not set:
              a.add(elem)
      for elem in lst:
          if type(elem) is set:
              if len(elem) > 1:
                  a.symmetric_difference_update(set_all)
                  elem = a
              elem.update(a)
  return


# убирает пересечение множеств возвращает число если оно одно во множестве
def min_in_set(some_lst):
  for i in range(9):
      for k in range(9):
          if type(some_lst[i][k]) is set:
              if len(some_lst[i][k]) > 1:
                  some_lst[i][k].symmetric_difference_update(set_all)
                  if len(some_lst[i][k]) == 1:
                      global num_num
                      num_num += 1
                      some_lst[i][k] = list(some_lst[i][k])[0]


gor_str = change_zero(gor_str)
vert_str = make_vert(gor_str)
sqw = make_sqw(gor_str)

make_set(gor_str)
make_set(vert_str)
make_set(sqw)

#min_in_set(sqw)







#min_in_set(vert_str)


#print('gor_str[0] =', gor_str[0])

#gor_str[0][2].add('пиписька')




class BigSquare:
  def __init__(self, *al):
      pass

  '''def input_list(self, a:str) -> list:
'''



class GorStr(BigSquare):
  def __init__(self, *al):
      super().__init__(self, *al)
      for st in al:
          self.st = st


class VertStr(BigSquare):
  def __init__(self, *al, v=[]):
      super().__init__(self, *al)
      self.v = v
      for st in al:
          for i in range(9):
              lst = []
              for el in st:
                  lst.append(el[i])
              v.append(lst)


'''for i in range(8):
  for k in range(8):'''






gor1 = GorStr(al)
#print(gor1.st[0])

ver1 = VertStr(al)
#print(ver1.v[0])


print('gor_str =', gor_str)
print('vert_str =', vert_str)
print('sqw =', sqw)
print('num_num =', num_num)


