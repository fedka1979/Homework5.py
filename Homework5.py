immutable_var = 1, 2, 3, 4, 'trace'
print(immutable_var)
mutable_list = ([1, 2], 3, 'halk')
print(mutable_list)
mutable_list[0][0] = 5
print(mutable_list)
immutable_var[0] = 300
print(immutable_var) # программа ругается не поддеоживает обращение по элементам