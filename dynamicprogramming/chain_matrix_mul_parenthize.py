import random
import sys

'''
The algorithm works as follows:
suppose there are n matrix, we first need to find out a k such that 
(matrix_0...matrix_k) and (matrix_k...matrix_n) multiplication cost is minimized.
For that we should know the cost of multiplication of the 2 submetrics as well.
If there is just one matrix, then cost is 0.
If there is just 2 metrics, cost is p * q * r where first is of dimension (p,q)
and second is of dimension (q,r).
So, we save the min cost of multiplications for all metrics array with smaller lenght
which are finally used to calculate the min cost of the entire matrix array
'''

MAX = sys.maxint
def get_min_cost(marr):
    '''
    returns the min cost for multiplication and also the markers where to put
    brackets for multiplication
    '''
    if len(marr) <= 1:
        return None, None
    mins = []
    markers = []
    i = 0
    l = len(marr)
    while i < l:
        mins.append([MAX]* l)
        markers.append([MAX] * l)
        mins[i][i] = 0  # cost of multiplying is 0 for i==j
        i += 1

    # Compute the cost of matrix multiplication when 
    # L = 2 to L = n
    L = 2
    while L <= l:
        i = 0
        while i <= l - L:
            j = i + L -1
            if L == 2:
                mins[i][j] = marr[i][0] * marr[i][1] * marr[j][1]
            else:
                k = i
                cur_min = MAX
                while k < j:
                    tmp = mins[i][k] + mins[k+1][j] + marr[i][0] * marr[k][1] * marr[j][1]
                    if tmp < cur_min:
                        cur_min = tmp
                        markers[i][j] = k
                    k += 1
                mins[i][j] = cur_min
            i += 1 
        L += 1
    return mins[0][l-1], markers


def gen_matrix_array(maxdim, n):
    if n < 1 or maxdim < 1:
        raise Exception("Hello")
    i = 0
    lastx = random.randint(1,maxdim)
    lasty = random.randint(1,maxdim)
    output = []
    while i < n:
        output.append((lastx, lasty))
        lastx = lasty
        lasty = random.randint(1,maxdim)
        i += 1
    return output


if __name__ == '__main__':
    x = gen_matrix_array(15, 10)
    print('The matrix array {}'.format(x))
    mincost, markers = get_min_cost(x)
    print('Min cost {}'.format(mincost))
    i = 0
    mx = len(x)
    j = mx - 1
    if mx > 2:
        marks = [(i, j , markers[i][j])]
        while True:
            if not marks:
                break
            i, j, m = marks.pop(0)
            if j - i < 2:
                continue
            print('Dividing matrix[{}][{}] at position {}'.format(i, j, m))
            if m - i > 1:
                marks.append((i, m, markers[i][m]))
            if j - m > 1:
                marks.append((m + 1, j, markers[m + 1][j]))
