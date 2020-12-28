def sum_of_a_nested_list(x)
    if not isinstance(x,list):
        return x
    else:
        sum_result = 0
        for i in x:
            sum_result+=i
            sum_result += sum_of_a_nested_list(i)
        return sum_result
        
        
        