def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    m=data[1]
    for i in data:
        if i>m:
            m=i


    k=0
    for i in data:
        if m==i:
            k+=1
        
    return k