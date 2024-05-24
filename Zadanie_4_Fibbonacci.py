def fibo (n):
    if n<0:
        raise ValueError("Bledny argument, argument nie moze byc ujemny")
    i = 2
    list = []
    if n==1:
        list.append(0)
    elif n==2:
        list.append(0)
        list.append(1)
    else:
        list.append(0)
        list.append(1)
        while i<=n-1:
            list.append(list[i - 1] + list[i - 2])
            i+=1
    return list


def fiboRec(n):
    if n < 0:
        raise ValueError("Bledny argument, argument nie moze byc ujemny")
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        list = fiboRec(n - 1)
        list.append(list[n - 2] + list[n - 3])
        return list
