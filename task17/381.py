f = open('17-381.txt')
a = [int(x) for x in f]
# ищем максимальный элемент
m = -10**10
for el in a:
    if abs(el) % 100 == 39 and 1000 <= abs(el) < 10000 and el > m:
        m = el

# ищем по условию в начале текста
b = []
for i in range(1, len(a)):
    p1, p2 = a[i - 1], a[i]
    if (1000 <= abs(p1) < 10000) + (1000 <= abs(p2) < 10000) == 1 and (p1 + p2) ** 2 <= m ** 2:
        b.append(p1 + p2)
print(len(b), max(b))