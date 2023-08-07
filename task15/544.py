m = -1
for a in range(0, 100):
    if all(x + 2 * y > a or y < x or x < 30 for x in range(0, 100) for y in range(0, 100)):
        m = max(a, m)
print(m)
