def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hashTable={}
    for i in range(length):
        if limit - weights[i] in hashTable:
            return [i, hashTable[limit - weights[i]]]
        else:
            hashTable[weights[i]] = i
    print(hashTable)


    return None
