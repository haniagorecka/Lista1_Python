
def heron (s1, s2, s3):
    if (s1 <= 0 or s2 <= 0 or s3 <= 0):
        raise  ValueError("Boki muszą być dodatnie")
    if (s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
        raise ValueError("Te boki nie mogą stworzyć trójkąta")
    p = (s1 + s2 + s3) / 2
    return (p * (p - s1) * (p - s2) * (p - s3))**0.5


