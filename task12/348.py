for i in range(3, 2000):
    line = '1' + '8' * i
    while '18' in line or '388' in line or '888' in line:
        if '18' in line:
            line = line.replace('18', '8', 1)
        if '388' in line:
            line = line.replace('388', '81', 1)
        if '888' in line:
            line = line.replace('888', '3', 1)
    if line.count('1') > 2:
        print(i, line)