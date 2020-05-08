def has_negatives(a):

    """
    YOUR CODE HERE
    """
    cache={}
    result=[]
    for element in a:
        if element not in cache:
            cache[element]=element
    
    for element in cache:
        if element > 0 and element* (-1) in cache:
            result.append(element)
    # print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
