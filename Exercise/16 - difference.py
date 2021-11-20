# Write a Python program to get the difference between the two lists.

def difference(list, lists):
    for i in list:
        if i not in lists:
            print(i)

if __name__ == '__main__':
    difference([1,2,3], [1,4,5])
