def my_split(str_arg):

    if str_arg == '':
        str_list = []
    else:
        str_list = str_arg.strip().split()

    return str_list

print(my_split("To be or not to be, that is the question"))
print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split(""))

