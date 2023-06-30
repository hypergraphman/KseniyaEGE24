from string import digits, ascii_uppercase


for x in range(23):
    # letter = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[x % 23]
    alphabet = digits + ascii_uppercase
    letter = alphabet[x % 23]
    t = int(f'7{letter}38596', 23) + int(f'14{letter}36', 23) + int(f'61{letter}7', 23)
    if t % 22 == 0:
        print(t // 22, x)