import random

def merge_sort(arr, start, end):
    if start == end:
        return
    if end - start == 1:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return


    mid = start + (end - start) / 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    # everything is sorted between start and mid, and mid+1 and end
    # Now insertion sort merge the two arrays
    while True:
        if mid == end:
            break
        if arr[mid] < arr[mid + 1]:
            break
        j = mid - 1
        while j >= start and arr[mid +1] < arr[j]:
            j -= 1
        j += 1
        temp = arr[mid + 1]
        i = mid + 1
        while i > j:
            arr[i] = arr[i - 1]
            i -= 1
        arr[j] = temp
        mid += 1


if __name__ == '__main__':
    j = 1
    while j < 501:
        x = [random.randint(0, 9999999999999) for i in range(0,1)]
        y = [a for a in x]
        z = [a for a in x]
        y.sort()
        merge_sort(x, 0, len(x) - 1)
        if y != x:
            print("Some issue")
            print("Should be  {}".format(y))
            print("You got    {}".format(x))
            print("Origin     {}".format(z))
        else:
            print('Success with size {}'.format(j))
        j += 1
