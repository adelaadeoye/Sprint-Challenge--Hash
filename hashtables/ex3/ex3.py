import collections

def intersection(arrays):

    """
    YOUR CODE HERE
    """
    cache={}
    result=[]
    for element in range(len(arrays)):
        cache[element]=arrays[element]
    for i in range(len(cache)):
        result+=(cache[i])
    result=[item for item, count in collections.Counter(result).items() if count > 1]
    return(result)
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10,20)) + [1,2,3])
    arrays.append(list(range(20,30)) + [1,2,3])
    arrays.append(list(range(30,40)) + [1,2,3])

    print(intersection(arrays))
