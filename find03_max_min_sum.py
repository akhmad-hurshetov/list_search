def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    m=data[0]
    max=0
    min=0
    for i in data:
        if i>m:
            max=i
        if i==m:
            min=i
        find_max_min_sum=max+min
    return find_max_min_sum