def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    
    max  = 0
    k = 1
    while k<len(data):
        if max<data[k]:
            max = data[k]
        k+=1
    return max
    

v = find_max([1,2,3,4,5])
print(v)