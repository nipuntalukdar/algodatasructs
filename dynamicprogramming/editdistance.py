def editdistance(one, two):
    l1 = len(one)
    l2 = len(two)
    if l1 == 0:
        # l2 insert for converting one to two
        return l2
    if l2 == 0:
        # l1 delete to convert l1 to l2
        return l1

    distances = []
    i = 0
    while i < l2 + 1:
        distances.append([0] * (l1 + 1))
        i += 1
    i = 0
    while i < l1 + 1:
        distances[0][i] = i
        i += 1
    i = 0
    while i < l2 + 1:
        distances[i][0] = i
        i += 1

    i = 1
    j = 1
    while i <= l2:
        j = 1
        while j <= l1:
            d1 = distances[i][j-1] + 1   # delete a char from first string
            d2 = distances[i-1][j] + 1   # insert a char two the first string
            d3 = distances[i-1][j-1] 
            if one[j-1] != two[i-1]:
                d3 = d3 + 2
            distances[i][j] = min(d1,d2,d3)
            j += 1
        i += 1
    return distances[l2][l1]

print editdistance("212345A", "012345X")
