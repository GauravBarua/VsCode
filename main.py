# Well i have completely lost the touch of python but still gonna try

lst = []
lst.extend([1, 2, 3, 4, 5])
print(lst)
print(type(lst))

lst2 = [10, 20.5, 30, 40.5]
lst2.reverse()
print(lst2)
print(type(lst2))

lst3 = [30, 21, 100, 1, 5, 0]
lst3.sort()
print("Sorted list would be: ", lst3)

lst4 = ['Gaurav', 'Barua']
print(' '.join(lst4))

char = "GauravBarua"
char_lst = []
for i in char:
    char_lst.append(i)

print(char_lst)
print(set(char_lst))