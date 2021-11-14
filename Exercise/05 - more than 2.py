 # Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
 
count = 0
a = ['abc', 'xyz', 'aba', '1221']
for i in a:
    if len(i) and i[0] == i[-1]: 
        count += 1 
print(count)