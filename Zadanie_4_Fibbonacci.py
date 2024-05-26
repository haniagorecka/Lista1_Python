def fibo(n):
    """
    Funkcja zwraca n-elementowy ciąg fibonacciego z wykorzystaniem iteracji
    :author: Hanna Górecka
    :param n:długość ciągu
    :return:listę elementów ciągu
    :raise: ValueError jeśli argument jest mniejszy niż 0
    """
    if n < 0:
        raise ValueError("Bledny argument, argument nie moze byc ujemny")
    if type(n) != int:
        raise TypeError("Bledny argument, argument musi byc liczba calkowita")
    i = 2
    list = []
    if n == 1:
        list.append(0)
    elif n == 2:
        list.append(0)
        list.append(1)
    else:
        list.append(0)
        list.append(1)
        while i <= n - 1:
            list.append(list[i - 1] + list[i - 2])
            i += 1
    return list


def fiboRec(n):
    """
    Funkcja zwraca n-elementowy ciąg fibonacciego z wykorzystaniem rekurencji
    :author:Hanna Górecka
    :param n:długość ciągu
    :return:listę elementów ciągu
    :raise: ValueError jeśli argument jest mniejszy niż 0
    Wspomogłam się algorytmem rekurencyjnym przedstawionym w źródle: https://stackoverflow.com/questions/68426233/correct-way-to-return-list-of-fibonacci-sequence-using-recursion
    """
    if n < 0:
        raise ValueError("Bledny argument, argument nie moze byc ujemny")
    if type(n) != int:
        raise TypeError("Bledny argument, argument musi byc liczba calkowita")
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        list = fiboRec(n - 1)
        list.append(list[n - 2] + list[n - 3])
        return list
