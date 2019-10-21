'''wordlist = ['cat','dog','rabbit']
#print(''.join(wordlist))
letterlist = []
#[letterlist.append(letter) for letter in (''.join(wordlist)) if letter not in letterlist]
#[letterlist.append(letter) for word in wordlist for letter in word if letter not in letterlist]
#print(list(set([letter for word in wordlist for letter in word])))
set(letterlist.append(letter) for word in wordlist for letter in word if letter not in letterlist)
print(letterlist)'''

'''               # Newton's Method
def squareroot(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root

print(squareroot(5))


sent = "methinks it is like a weasel"
print(len(sent))'''

'''vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print([digit for lst in vec for elem in lst for digit in elem])'''


'''def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,other):
        newnum = self.num*other.den + \
        self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        num = self.num*other.num
        den = self.den*other.den
        greatcommon = gcd(num, den)
        return Fraction(num//greatcommon, den//greatcommon)

    def __truediv__(self, other):
        num = self.num*other.den
        den = self.den*other.num
        greatcommon = gcd(num, den)
        return Fraction(num//greatcommon, den//greatcommon)

    def __sub__(self, other):
        num = self.num*other.den - \
            other.num*self.den
        den = self.den*other.den
        greatcommon = gcd(num, den)
        return Fraction(num//greatcommon, den//greatcommon)

    def __gt__(self, other):
        num1 = self.num*other.den
        num2 = other.num*self.den
        return num1 > num2

    def __lt__(self, other):
        num1 = self.num*other.den
        num2 = other.num*self.den
        return num1 < num2


x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)


print(x*y)   # __mul__(self, value, /)   Return self*value.
print(x/y)   # __truediv__
print(x-y)   # __sub__
print(x>y)   # __gt__(self, value, /)   Return self>value.
print(x<y)   # __lt__(self, value, /)   Return self<value.'''
#print(dir(Fraction))
#print(help(dir(Fraction)))'''



'''class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0'''

'''class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate'''


'''def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()'''

                                   # разница между переменной класса и переменной экземпляра класса'
'''class A(object):
    def __init__(self):
        self.lst = []
    name = 'V'

class B(object):
    lst = []
    color = 'red'''''


'''x = B()
y = B()
x.lst.append(1)  # list это одна и та же переменная класса т е статическая переменная
y.lst.append(2)
print(x.lst)
print(y.lst)

print(x.color)
print(y.color)

x.color = 'green'  # так мы создали динамический атрибут(кот принадлежит только X экземпляру класса
print(x.color)
print(y.color)'''


'''x = A()
y = A()
x.lst.append(1)
y.lst.append(2)   # это разные переменные разных экземпляров класса


print(x.name)
print(y.name)
print(x.lst)
print(y.lst)'''


'''class A:
    def __init__(self, a=[]):
        a.append('hello')
        print(a)

A()
A()
A()'''

'''class B:
    def __init__(self, b=None):
        if b is None:
            b = []
            b.append('goodbye')
            print(b)

B()
B()
B()'''


'''class ColCamp:
    def __init__(self, ):
        pass


class Faculty(ColCamp):
    def __init__(self, state, city, history, physics, math, literature):  # сюда передаем все родитель+потомство
        super().__init__(state, city)  # сюда передаем то что наследуем с родительского
        self.history = history
        self.history = physics
        self.history = math
        self.literature = literature



class Stuff(Faculty):
    pass


class Students(Faculty):
    pass


'Argentina'
'Buenos Aires' '''



'''
""" Напишите класс Hand, который хранит карты игрока. Класс Hand имеет методы: 
Взять карту в руку. Показать все карты из руки и их порядковые номера от 1 до 5 на экране"""

class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)

    def get_card(self, n):
        print('The cart in my hand is ' + self.cards[n])

    def show_all(self):
        for i in range(len(self.cards)):
            print(i, '-', self.cards[i])


your_hand = Hand('A', '10', 'K', '6', '8')

your_hand.get_card(2)

your_hand.show_all()

'''


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
alsq = '530 070 000' \
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

min_in_set(gor_str)







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

# добавил строчку просто так

a = 111