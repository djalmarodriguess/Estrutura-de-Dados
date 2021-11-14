# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 

lista_a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lista_a.sort(key=lambda a:a[1])
print(lista_a)


from operator import itemgetter

lista_b = [(9, 6), (8, 10), (5, 8), (3, 3), (2, 4)]
lista_b = sorted(lista_b, key=itemgetter(1))
print(lista_b)