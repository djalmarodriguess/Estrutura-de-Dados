# Write a Python program to clone or copy a list

copy_list = []
def new_list (list):
    for i in list:
        if i not in copy_list:
            copy_list.append(i)
    print(f'Lista de entrada = {list}')

if __name__ == "__main__":
    new_list([1, 2, 3, 4] )
    print(f'Lista copiada = {copy_list}')

