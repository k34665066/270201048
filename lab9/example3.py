def get_evens(my_list):
    if len(my_list)==0:
        return 0
    #recursive part
    counter=0
    if my_list[0]%2==0:
        counter=1
    return counter + get_evens(my_list[1:])
print(get_evens([0,1,2,3,4,5]))
        

