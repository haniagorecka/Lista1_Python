def allBinary(n, list, i, arr):
    if (n < 0):
        raise ValueError("Długość liczby nie może być mniejsza niż 0")
    if (i < 0):
        raise ValueError("Iterator nie może być na ujemnej pozycji")
    if (i == n):
        temp = arr.copy()
        list.append(temp)
        return
    arr[i] = 0
    allBinary(n, list, i + 1, arr)
    arr[i] = 1
    allBinary(n, list, i + 1, arr)


def subsets(list):
    n = len(list)
    subsets = []
    binary = []
    if n == 0:
        return subsets
    i = 0
    arr = [0] * n
    allBinary(n, binary, 0, arr)
    for k in range(0, len(binary)):
        temp = []
        for j in range(0, len(binary[k])):
            if binary[k][j]==1:
                temp.append(list[j])
        subsets.append(temp)
    return subsets



