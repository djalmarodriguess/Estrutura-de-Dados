# Write a Python program to remove duplicates from a list.
b = []
a = [10, 2, 2, 2 , 0.51, 9, 3, 9, 5]

for i in a:
    if i not in b:
        b.append(i)
        
print(b)