# Write a Python function that takes two lists and returns True if they have at least one common member.

new_list = []
def two_list(list, lists):
   for i in list:
       if i in lists:
           new_list.append(i)
   if len(new_list) >= 1:
        print(True)
   else:
        print(False)         
                       
if __name__ == '__main__':
    two_list([3, 2, 3, 4, 5, 6, 7], [1, 1, 8, 9, 0])


# Segunda maneira:

def order(list, lists):
    lista = []
    for i in list:
        for u in lists:
            if i == u:
                lista.append(i)
    if len(lista) >= 1:
        print(True, f'{lista[0]}') 
    else:
        print(False)

if __name__ == '__main__':
    order([3, 2, 3, 4, 5, 6, 7], [1, 1, 8, 9, 0,])