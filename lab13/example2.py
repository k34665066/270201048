def binary_search(list,element):
    if len(list)==1:
        return 0
    else:
        mid_element=len(list)//2
        if element==list[mid_element]:
            return mid_element
        elif element<list[mid_element]:
            return binary_search(list[:mid_element],element)
        else:
            return binary_search(list[mid_element:],element)+mid_element
print(binary_search([1,2,3,4,5,6,7],5))