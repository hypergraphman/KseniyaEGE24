for x in range(23):
    a = 7 * 23**6 + x * 23**5 + 3 * 23**4 + 8 * 23**3 + 5 * 23**2 + 9 * 23 + 6
    b = 23**4 + 4 * 23**3 + x * 23**2 + 3 * 23 + 6
    c = 6 * 23**3 + 23**2 + x + 7
    if (a + b + c) % 22 == 0:
        print((a + b + c) // 22, x)