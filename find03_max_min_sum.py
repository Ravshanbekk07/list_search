def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    max  = 0
    k = 1
    while k<len(data):
        if max<data[k]:
            max = data[k]
        k+=1
    min  = 4
    k = 0
    while k<len(data):
        if min>data[k]:
            min = data[k]
        k+=1
    return min+max
    

v = find_max_min_sum([2, 7, 3, 4, 9])
print(v)
