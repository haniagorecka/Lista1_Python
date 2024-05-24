def collatz(c0):
    """
    Funkcja zwraca listę elementów ciągu collatza zaczynającego się od c0 przed tym jak wpadnie w cykl, przyjmuję, że cykl zaczyna się
    od pierwszego elementu równego 4 włącznie, więc nie wypisuję już tego elementu
    :author: Hanna Górecka
    :param c0:pierwszy element ciągu
    :return:lista elementów ciągu przed wpadnięciem w cykl
    :raise: ValueError jeśli pierwszy element ciągu jest niedodatni
    """
    if c0<=0:
        raise ValueError("Bledny pierwszy element ciagu")
    c1 = c0
    list = []
    while c1!=4:
        if c1%2 == 0:
            list.append(c1)
            c1 = int(c1/2)
        else:
            list.append(c1)
            c1 = int(3 * c1 + 1)
    return list



