def bubbleSort(list):
    n = len(list)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


def switchToNext(list, i, max):
    if i < 0:
        raise ValueError("Niepoprawny iterator")
    if i > max:
        raise OverflowError("Iterator przekracza zakres")
    if max < 0:
        raise ValueError("Niepoprawny zakres")
    temp1 = i
    temp = list[i]
    while list[temp1] == temp and temp1 < max:
        temp1 += 1
    return temp1


def shared(list1, list2):
    bubbleSort(list1)
    bubbleSort(list2)
    n = len(list1)
    m = len(list2)
    j = 0
    k = 0
    list3 = []
    while j < n and k < m:
        if list1[j] == list2[k]:
            list3.append(list1[j])
            j += 1
            k += 1
        elif list1[j] > list2[k] and k < m - 1:
            k = switchToNext(list2, k, m)
        elif list2[k] > list1[j] and j < n - 1:
            j = switchToNext(list1, j, n)
        else:
            j += 1
            k += 1
    return list3


list1 = [1, 2]
list2 = [2, 1]
print(shared(list2, list1))
