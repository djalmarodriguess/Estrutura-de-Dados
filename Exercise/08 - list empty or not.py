# Write a Python program to check a list is empty or not

a = [10, 2, 2, 2 , 0.51, 9, 3, 9, 5]
b = []

def lista(list):
    if len(list) == 0: 
        print('List is empty')
    else:
        print('List is not empty')
    

if __name__ == '__main__':
    lista(a)
    lista(b)
