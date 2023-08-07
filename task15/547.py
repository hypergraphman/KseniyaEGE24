m = 1000
for a in range(1, 1000):
    if all((a + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0)) for x in range(1, 1000)):
        m = min(a, m)
print(m)
