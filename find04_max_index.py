def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    max  = 0
    k = 1
    while k<len(data):
        if max<data[k]:
            max = data[k]
        k+=1
    return data.index(max)
    

v = find_max_index([1,2,3,4,5,6])
print(v)

