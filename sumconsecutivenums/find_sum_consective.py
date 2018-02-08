'''
array = [1, 2, 3],   if sum is 4, no match
but if sum is 5, then arr[1:3] we should return

sumtil = current sum from last possible position to current position
if sumtil < givensum:
    add next number also and continue
else if sutil == givensum:
    got it and you may return
else:
    sum is bigger.... 
    adjust sumtil...
    sumtil -= arr[last pssible position]
    lastpossible positon += 1
if current position is highest position:
    break
'''

# Returns start and end index of the sub array which adds up to
# the given sum

def find_given_sum(arr, givensum):
    size = len(arr)
    if size == 1:
        if givensum == arr[0]:
            return 0, 0, True
    if size == 0:
        return 0, 0, False

    sumtil = 0
    current_pos = 0
    lastpos = 0
    while True and current_pos < size:
        sumtil += arr[current_pos]
        if sumtil < givensum:
            current_pos += 1
            continue
        elif sumtil == givensum:
            return lastpos, current_pos, True
        else:
            while sumtil > givensum and lastpos <= current_pos:
                sumtil -= arr[lastpos]
                lastpos += 1
            if sumtil == givensum:
                return lastpos, current_pos, True
            current_pos += 1
                
    return 0, 0, False

if __name__ == '__main__':
    startindex, endinde, found = find_given_sum([6, 2], 7)
    if found:
        print("Something wrong")
    else:
        print("Success")
    
    startindex, endindex, found = find_given_sum([6, 2], 6)
    if startindex != 0 or endindex != 0 or not found:
        print("Something wrong")
    else:
        print("Success")
    
    startindex, endindex, found = find_given_sum([6, 2], 8)
    if startindex != 0 or endindex != 1 or not found:
        print("Something wrong")
    else:
        print("Success")
    
    startindex, endindex, found = find_given_sum([6, 2, 10, 5, 9, 2], 26)
    if startindex != 1 or endindex != 4 or not found:
        print("Something wrong")
    else:
        print("Success")


