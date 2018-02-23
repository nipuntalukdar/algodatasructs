def knapsack_max_value(items, maxweight):
    '''
    items is an array of value and weight (v, w)
    maxweight is maximu weight can be held in knapsack
    '''

    i = 0
    possibles = []
    itemcount = len(items)
    while i <= maxweight:
        possibles.append([0] * (itemcount + 1))
        i += 1

    # if maxweight == 0, only zero item can be taken
    
    startweight = 1 # will map to zeroth item in items
    startitem = 1   # will map to zeroth item in items

    while startweight <= maxweight:
        while startitem <= itemcount:
            w = items[startitem - 1][1]
            v = items[startitem - 1][0]
            if w > startweight:
                possibles[startweight][startitem] = possibles[startweight][startitem - 1]
            else:
                v1 = possibles[startweight][startitem - 1]  # of we leave this item
                # if we take this item, value is v2
                v2 = 0
                v2 = possibles[startweight - w][startitem - 1] + v
                possibles[startweight][startitem] = max(v1, v2)
            startitem += 1
        startitem = 1
        startweight += 1
    
    return possibles[maxweight][itemcount]


print knapsack_max_value([(10,2), (1000,2),(1,5), (2000, 5)], 9)
    
