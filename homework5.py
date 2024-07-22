immutable_var = 1, "hello", True, 1.78
print(immutable_var)
#immutable_var[3] = False # Ошибка: кортеж не поддерживает обращение по элементам.
#print(immutable_var)
mutable_list = [1, "Bye", False, 5.5]
mutable_list[0] = 256
mutable_list[-1] = 1.23
print(mutable_list)

