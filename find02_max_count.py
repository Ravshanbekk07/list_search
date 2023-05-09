def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    
    max = 0
    k = 1
    count = 0
    while k < len(data):
        if max < data[k]:
            max = data[k]
            
            
            
        
        
        while k<len(data):
            if max == data[k]:
                count += 1
            k+=1
            
    return count


v = find_max_count([1, 8, 3, 8, 5,8])
print(v)
