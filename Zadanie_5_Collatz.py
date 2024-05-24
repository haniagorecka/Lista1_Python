def collatz(c0):
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



