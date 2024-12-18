immutable_var = 22, 33 , "Cucumber" , True
print(immutable_var)
#immutable_var [0]=99
#print(immutable_var)  кортеж относится к неизменяемым типам данных и не поддерживает обращение к элементам,
#но несмотря на неизменяемость самого кортежа, в себе он может хранить какие-то изменяемые объекты
mutable_list = [1 , 2, "Tree", False]
mutable_list [0] = 99
print(mutable_list)