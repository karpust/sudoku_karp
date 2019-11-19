# s = "abc"
# it = iter(s)    # создали итератор - объект перечислитель кот вызывает next или исключение StopIteration
# print(it)
# print(type(it))
# print(dir(it))
# c = next(it)
# d = next(it)
# e = next(it)
# print(c)
# print(d)
# print(e)
#
# lst = [1, 2, 3]
# print(type(iter(lst)))


# --------------------------------------------------------------------------------------------------------------
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# rev = Reverse('spam')
# iter(rev)
# for char in rev:
#     print(char)


# ------------------------------------------------------------------------------------------------------------------
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#
#
# # for char in reverse('golf'):
# #     print(char)
# rev = reverse('golf')
# print(next(rev))
# print(next(rev))
# print(next(rev))
# print(next(rev))


# -------------------------------------------------------------------------------------
# mylist = [x*x for x in range(3)]    # list comprehension
# for i in mylist:
#     print(i)
# print(type(mylist))
# print(mylist)
#
# mygenerator = (x*x for x in range(3))   # Generators
# for n in mygenerator:
#     print(n)
# print(type(mygenerator))
# print(mygenerator)


# ----------------------------------------------------------------------------------------