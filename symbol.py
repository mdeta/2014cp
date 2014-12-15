#@+leo-ver=5-thin
#@+node:lee.20141212201841.7: * @file symbol.py
#@@language python
#@@tabwidth -4

def symbolSpace(row):
    s = [
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
    ]
    return s[row]


def symbol1(row):
    s = [
        '■■■□■■■',
        '■■□□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■□□□□□□',
    ]
    return s[row]


def symbol2(row):
    """
    row is a positive int
    return None
    """
    s = [
        '■□□□□□■',
        '■□■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■■□□□□□',
        '■□■■■■■',
        '■□■■■■■',
        '■□□□□□□',
    ]
    return s[row]


def symbol3(row):
    s = [
        '■□□□□□■',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■□□□□□■',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■□□□□□■',
    ]
    return s[row]

symbolDict = {"1": symbol1, "2": symbol2, "3": symbol3, "":symbolSpace}
#@-leo
