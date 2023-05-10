def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    
    max = 15
    k = 8

    while k < len(data):
        if not k % 2:
            if max < data[k]:
                max = data[k]

        k += 1
    return max
    
    
    

v = find_max_odd([15,1, 8, 3, 8, 5,10,11,14,13])
print(v)