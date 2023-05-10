def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    min  = 4
    k = 1
    while k<len(data):
        
        if k % 2:
            if min>data[k]:
                min = data[k]
        
        k+=1   
   
    return min
  
v = find_min_even([1,4,10,5,6,8,3,2])
print(v)

