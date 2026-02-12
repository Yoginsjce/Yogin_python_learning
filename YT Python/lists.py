my_list=[12,24,128,78,99]
print(my_list)

#functions
print(len(my_list))
print(sum(my_list))
print(sorted(my_list))

#methods
print(my_list.index(128))
print(my_list.count(12))

'my_list.reverse()'
'print(my_list)'

#slicing
print(my_list[1:3])
print(my_list[1::2])

#modifying list

my_list.append(99)
print(my_list)
my_list.pop()
print(my_list)
#my_list.clear()
print(my_list)
my_list.remove(128)
print(my_list)
my_list.insert(2,816)
print(my_list)
my_list[3]=678
print(my_list)