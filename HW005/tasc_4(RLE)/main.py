# Алгоритм сжатия для строки

def encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1

    return encoding


def decode(s):
    decode = ''
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


if __name__ == '__main__':

    s = input('Введите строку:\n')
    e = encode(s)
    print(e)
    d = decode(e)
    print(d)