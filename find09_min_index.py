def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    min  = 1
    k = 2
    while k<len(data):
        if min>data[k]:
            min = data[k]
        k+=1
    return data.index(min)
    

v = find_min_index([1, 2, -3, 4, 5])
print(v)

