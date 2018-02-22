def find_rectangle_with_corner_ones(matrix):
    if len(matrix) <= 1:
        return None, False

    prevlen = -1
    for i in matrix:
        if prevlen == -1:
            prevlen = len(i)
        else:
            if len(i) != prevlen:
                return None, False

    a = []

    for i in matrix:
        x = set()
        j = 0
        while j < prevlen:
            if i[j] == 1:
                x.add(j)
            j += 1
        a.append(x)
    
    i = 0
    j = 1
    while i < len(matrix) - 1:
        if len(a[i]) < 2:
            i += 1
            continue
        j = i + 1
        while j < len(matrix):
            if len(a[j]) < 2:
                j += 1
                continue
            out = a[i] & a[j]
            if len(out) >= 2:
                return (i, j, out), True
        i += 1
    return None, False

print find_rectangle_with_corner_ones([[1,0,1], [1,0,0], [1,0,1]])
