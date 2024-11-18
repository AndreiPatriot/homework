def print_params(a = 1, b ='строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
print_params()
values_list = (1, 'голос', [50])
values_dict = {'a' : 3, 'b' : 5, 'c' :10}
print_params(*values_list)
print_params(**values_dict)
values_list_2 =[100, "'Яблоко'"]
print_params(*values_list_2,42)