def fake_bin(x):
    a = ''
    for i in x:
        i = int(i)
        if i < 5:
            a = a + '0'
        elif i >= 5:
            a = a + '1'
    return a