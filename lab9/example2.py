def get_reversed(my_list):
    if len(my_list)==0:
        return []
    else:
        return [my_list.pop()] + get_reversed((my_list))
print(get_reversed([1,2,3,4,5]))