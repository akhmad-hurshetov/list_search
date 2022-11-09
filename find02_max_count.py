def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    m=data[0]
    count=0
    for i in len(data):
        if m<len(data):
            count+=1
    return count

print(find_max_count([3,5,6,7,10]))
    
