
def allBinary(n, list, i, arr):
    """
    Funkcja rekurencyjnie dodaje listę wszystkich liczb binarnych o długości n do listy list
    :param n: długość liczb binarnych
    :param list: lista list, do której dodane zostaną liczby binarne
    :param i: iterator
    :param arr: zmienna tymczasowa, lista, która jest zmieniana w celu przejścia przez wszytskie liczby binarne
    :raise: ValueError jeśli podana długość liczby binarnej jest ujemna
    :raise: ValueError jeśli iterator jest ujemny
    :author: Hanna Górecka
    Wspomogłam się algorytmem wypisywania liczb binarnych z: https://www.geeksforgeeks.org/generate-all-the-binary-strings-of-n-bits/
    """
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
    """
    Funkcja zwraca listę list, będących wszystkimi podzbiorami podanego zbioru

    :param list: lista, będąca zbiorem, z którego trzeba wyznaczyć podzbiory
    :return: lista podzbiorów
    :author: Hanna Górecka
    Zainspirowałam się algorytmem przedstawionym w pytaniu użytkownika azonips w https://4programmers.net/Forum/Inne/167256-Algorytm_znajdywania_wszystkich_podzbiorow_danego_zbioru?fbclid=IwAR1JgneaWoUcm7d73cYB74IGo2ke7I8N9isF-a5oXuUrszfFn5EK7fMR0fg_aem_AUzeYB96MaJxZ59VmaEMmJ-7xH_xm2xv3RfpvBACM9gvC2pAagk3ndjI9XUTdkQC8aLVyF8Y3D_HTy3HbES7_wck
    """
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
            if binary[k][j] == 1:
                temp.append(list[j])
        subsets.append(temp)
    return subsets

