def duplicateZeros(arr):
    # for i in range (len(arr)):
    i = -1
    while i < len(arr) - 1:
        i += 1
        if arr[i] == 0:
            arr.pop()
            arr.insert(i, 0)
            i += 1

    print(arr)


duplicateZeros([1,0,2,3,0,4,5,0])