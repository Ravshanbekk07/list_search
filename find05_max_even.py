def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    max  = 0
    k = 1
    while k<len(data):
        if max<data[k]:
            max = data[k]
            if max%2:
                print(max)

        k+=1
    return max
    

v = find_max_even([1,4,3,8,5,12])
print(v)
