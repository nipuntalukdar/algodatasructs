'''
Below functions implement longest common sequence in string.
It uses dyncmic programming.
It works with the below simple principle.
lcs is 0 of any one of the string has length == 0
if X is string 1, and Y is string 2, then if we know the lcs of substrings for
till (i-1)th character of X and till (j-1)th char of Y, then we can calculate the 
lcs X (till ith char) and Y (till jth char)

lcs(till ith char of X, till jth char of Y)
== lcs(till i-1 th char of X, till j-1th char of Y) + 1 if X[i] == Y[j],
else
    lcs if max of (lcs(X[:i],Y[:j+1), lcs(X[:i+1],Y[:j]))

'''

''' 
below constants are needed to climb up the result to construct the
lcs string
'''

SKIP_X = 100
SKIP_Y = 200
ADD_XY = 300
def lcs(one, two):
    '''
    Returns length of lcs
    '''
    l1 = len(one)
    l2 = len(two)
    
    if l1 == 0 or l2 == 0:
        return 0
    i = 0
    matrix = []
    while i < l2:
        matrix.append([0] * l1)
        i += 1
    i = 0
    j = 0
    while i < l2:
        j = 0
        while j < l1:
            mx = 0
            if one[j] == two[i]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                if i > 0 and j == 0:
                    matrix[i][j] = matrix[i-1][j]
                elif i == 0 and j > 0:
                    matrix[i][j] = matrix[i][j-1]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
            j += 1
        i += 1
    return matrix[l2 - 1][l1 -1]


def lcs_also_retun_the_longest_sequence(one, two):
    '''
    Returns length of lcs and also the details needed to get the lcs string
    '''
    l1 = len(one)
    l2 = len(two)
    
    if l1 == 0 or l2 == 0:
        return 0
    i = 0
    matrix = []
    while i < l2:
        matrix.append([(0, SKIP_Y)] * l1)
        i += 1
    i = 0
    j = 0
    while i < l2:
        j = 0
        while j < l1:
            mx = 0
            if one[j] == two[i]:
                if i == 0 or j == 0:
                    matrix[i][j] = (1, ADD_XY) 
                else:
                    matrix[i][j] = (matrix[i-1][j-1][0] + 1, ADD_XY)
            else:
                if i > 0 and j == 0:
                    matrix[i][j] = (matrix[i-1][j][0], SKIP_Y)
                elif i == 0 and j > 0:
                    matrix[i][j] = (matrix[i][j-1][0], SKIP_X)
                elif i > 0 and j > 0:
                    if matrix[i][j-1][0] > matrix[i-1][j][0]:
                        matrix[i][j] = (matrix[i][j-1][0], SKIP_X)
                    else:
                        matrix[i][j] = (matrix[i-1][j][0], SKIP_Y)
            j += 1
        i += 1
    return matrix[l2 - 1][l1 -1][0], matrix

if __name__ == '__main__':
    one="abccd1e234hj56uiiii78hdhdh"
    two="AAAA1BBBB2XXX3HHH4HH4H5JJJ6JJJ7JJJJJ8"
    lcsval,seq = lcs_also_retun_the_longest_sequence(one, two)
    print lcsval
    i = len(seq) - 1
    j = len(seq[0]) - 1
    retlcs = []
    while i >= 0 and j >= 0:
        climb = seq[i][j][1]
        if climb == ADD_XY:
            retlcs.insert(0, one[j])
            i -= 1
            j -= 1
        elif climb == SKIP_X:
            j -= 1
        elif climb == SKIP_Y:
            i -=1
    print(''.join(retlcs))

