def komplement(kodujaca):
    """
    Funkcja zwraca nić komplementarną do podanej nici kodującej DNA
    :author Hanna Górecka
    :param kodujaca:nić kodująca DNA, na początku sprawdza czy nie jest pusta
    :return:komplementarna nić matrycowa (odwrócona kolejność)
    :raise ValueError jeśli znajdzie niewłaściwy znak w nici kodującej
    :raise ValueError jeśli nić kodująca jest pusta
    """
    if not kodujaca:
        raise ValueError("Nic kodujaca jest pusta")
    if type(kodujaca)!=str:
        raise TypeError("Argument musi byc typu String")
    komplementarna = ""
    for el in kodujaca.upper():
        match el:
            case 'A':
                komplementarna += 'T'
            case 'C':
                komplementarna += 'G'
            case 'T':
                komplementarna += 'A'
            case 'G':
                komplementarna += 'C'
            case _:
                raise ValueError(" Niewłaściwy symbol w nici kodujacej")
    return komplementarna[::-1]


def transkrybuj(matrycowa):
    """
    Funkcja zwraca nić transkrybowaną RNA do podanej nici matrycowej
    :author: Hanna Górecka
    :param matrycowa: nić matrycowa DNA, na początku sprawdza czy nie jest pusta
    :return: transkrybowana nić RNA
    :raise ValueError jeśli znajdzie niewłaściwy znak w nici matrycowej
    """
    if not matrycowa:
        raise ValueError("Nic matrycowa jest pusta")
    if type(matrycowa)!=str:
        raise TypeError("Argument musi byc typu String")
    transkrybowana = ""
    for el in matrycowa.upper():
        match el:
            case 'A':
                transkrybowana += 'U'
            case 'C':
                transkrybowana += 'G'
            case 'T':
                transkrybowana += 'A'
            case 'G':
                transkrybowana += 'C'
            case _:
                raise ValueError(" Niewłaściwy symbol w nici matrycowej")

    return transkrybowana[::-1]


def transluj(rna):
    """
    Funkcja zwraca sekwencję aminokwasów (białko) na podstawie nici RNA
    :author: Hanna Górecka
    :param rna:nić RNA, na podstawie, której translowane jest białko, na początku sprawdza czy nie jest pusta
    :return:sekwencja aminokwarów tworzących białko
    :raise: ValueError jeśli znajdzie nieistniejący kodon
    """
    if not rna:
        raise ValueError("Nic RNA jest pusta")
    if type(rna)!=str:
        raise TypeError("Argument musi byc typu String")
    slownikAminokwasow = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
    }
    i = 0
    aminokwasy = ""
    while i + 3 <= len(rna):
        temp = rna.upper()[i:i+3]
        if temp in slownikAminokwasow.keys():
            if slownikAminokwasow.get(temp) == "Stop":
                aminokwasy += " "
                break
            else:
                aminokwasy += slownikAminokwasow.get(temp)
                aminokwasy += " "
                i += 3
        else:
            raise ValueError("Niewłaściwy kodon w nici RNA")
    return aminokwasy







