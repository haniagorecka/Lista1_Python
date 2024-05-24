
def heron (s1, s2, s3):
    """
    Funkcja zwraca powierzchnię trójkąta z boków podanych jako argumenty
    :param s1: pierwszy bok trójkąta, dodatni
    :param s2: drugi bok trójkąta, dodatni
    :param s3: trzeci bok trójkąta, dodatni
    :return: powierzchnię trójkąta
    :raise: ValueError jeśli któryś z boków jest niedodatni
    :raise: ValueError jeśli jedna z par boków nie jest większa niż ostatni bok
    :author: Hanna Górecka
    """
    if (s1 <= 0 or s2 <= 0 or s3 <= 0):
        raise  ValueError("Boki muszą być dodatnie")
    if (s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
        raise ValueError("Te boki nie mogą stworzyć trójkąta")
    p = (s1 + s2 + s3) / 2
    return (p * (p - s1) * (p - s2) * (p - s3))**0.5


