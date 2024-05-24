def bubbleSort(list):
    """
    Funkcja sortuje listę algorytmem sortowania bąbelkowego w sposób rosnący
    :param list: lista nieposortowanych elementów
    :author: Hanna Górecka
    Wspomogłam się algorymem sortowania bąbelkowego z: https://www.javaguides.net/2022/11/bubble-sort-algorithm-in-kotlin.html
    """
    n = len(list)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


def switchToNext(list, i, max):
    """
    Funkcja zwraca indeks, na którym w podanej liście znajduje się następny element o innej wartości niż początkowa
    :param list: lista, której elementy sprawdzamy
    :param i: początkowy indeks
    :param max: maksymalny indeks
    :return: indeks nastepnego elementu o innej wartości
    :raise: ValueError jeśli iterator jest ujemny lub większy od maksymalnego indeksu
    :raise: ValueError jeśli maksymalny indeks jest ujemny
    :author: Hanna Górecka
    """
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
    """
     Funkcja zwraca listę wspólnych elementów z dwóch podanych jako argumenty list
    :param list1: pierwsza lista
    :param list2: druga lista
    :return: listę wspólnych elementów
    :author: Hanna Górecka
    """
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


