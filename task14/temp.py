from string import ascii_uppercase, digits


def n_to_p(n, p):
    r = ''
    d = digits + ascii_uppercase
    while n > 0:
        r = d[n % p] + r
        n //= p
    return r


print(n_to_p(4**2014 + 2**2015 - 8, 2).count('1'))