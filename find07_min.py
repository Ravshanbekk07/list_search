def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """

    min  = 1
    k = 2
    while k<len(data):
        if min>data[k]:
            min = data[k]
        k+=1
    return min
    

v = find_min([15, 23, 3, 9, 1, -4])
print(v)