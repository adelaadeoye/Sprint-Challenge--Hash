def finder(files, queries):

    """
    YOUR CODE HERE
    """
    cache= {}

    for query in queries:
            cache[query]=True
    
    result=[]

    for path in files:
        if path.split("/")[-1] in cache:
            result.append(path)

   
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
