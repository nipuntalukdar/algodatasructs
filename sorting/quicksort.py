def quick_sort(arr, start, end):
    if start == end:
        return
    if end - start == 1:
        if arr[start] > arr[end]:
            arr[end], arr[start] = arr[start],arr[end]
        return
    i = start + 1
    j = end
    pivot = arr[start]
    while i <= j:
        if arr[i] <= pivot:
            i += 1
            continue
        while arr[j] > pivot and j > i:
            j -= 1
        if j == i:
            # all elements from index i are greater than pivot
            break
        #element a[j] < pivot, a[i] >= pivot , j > i
        arr[j], arr[i] = arr[i], arr[j]
        i += 1
        j -= 1

    # from index i onwards everything is >= pivot
    # below index i, everything is < pivot
    i -= 1
    if i - start >  0:
        arr[i], arr[start] = arr[start], arr[i]
        quick_sort(arr, start, i - 1)
    if i + 1 < end:
        quick_sort(arr, i + 1, end)

if __name__ == '__main__':
    import random
    j = 1
    while j <= 1000:
        x = [random.randint(0,999999999999) for i in range(0,j)]
        y = [a for a in x]
        z = [a for a in x]
        y.sort()
        quick_sort(x, 0, len(x) - 1)
        if y != x:
            print("Sorting failed for {}".format(z))
            break
        j += 1
        print("Success on iteration {}".format(j - 1))
