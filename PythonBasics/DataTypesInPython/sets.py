# my_set = {11, 9, 26, 34, 53, 'apple', 'ball', 'cat'}
# print(my_set)

# a = {}
# print(a)

# add(), discard(), clear(), pop(), copy(), union(), update(), intersection(), isdisjoint(), issuperset(), max(), min(), len()
a = {1, 2, 3, 4}
b = {5, 6, 7, 8, 9, 75, 42, 86, 38}
c = {9, 7, 38, 42}
d = b.issuperset(a)
print('Is all the elements of Set a are elements of Set b ', d)

e = b.issuperset(c)
print('Is all the elements of Set c are elements of Set b ', e)

# my_set = {11, 9, 26, 34, 53}
# print(my_set)
# b = [94, 'Allen', 75, 1, 4]
# c = (56, 89, 34, 75)
# my_set.update(b, c)
# print(my_set)

# a = {2, 1, 3, 5, 4}
# b = {5, 7, 6, 8, 1}
# c = my_set.union(a, b)
# c = a.intersection(b)
# print(my_set.isdisjoint(b))

# xyz = my_set.copy()
# print(xyz)
# my_set.pop()
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.add(90)
# print(my_set)
# my_set.discard(11)
# print(my_set)
# my_set.clear()
# print(my_set)
