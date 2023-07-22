for i in range(0, 25):
    line = '7' + (i + 1) * '1' + (i + 2) * '2' + (i + 3) * '3'
    while '71' in line or '72' in line or '73' in line:
        if '71' in line:
            line = line.replace('71', '227', 1)
        if '72' in line:
            line = line.replace('72', '37', 1)
        if '73' in line:
            line = line.replace('73', '17', 1)
    print(i, 9 * i, sum(map(int, line)))