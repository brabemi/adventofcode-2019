from collections import Counter

MIN = 156218
MAX = 652527


def validate_1(number):
    double = False
    for i in range(5):
        if number[i] == number[i+1]:
            double = True
    acc = 0
    for e in number:
        acc *= 10
        acc += e
    return double and acc >= MIN and acc <= MAX


def validate_2(number):
    cnt = Counter(number)
    acc = 0
    for e in number:
        acc *= 10
        acc += e
    return 2 in cnt.values() and acc >= MIN and acc <= MAX


def numbers(prefix, depth, validate):
    acc = 0
    if depth == 0:
        return 1 if validate(prefix) else 0
    a = prefix[-1] if prefix else 1
    for i in range(a, 10):
        prefix.append(i)
        acc += numbers(prefix, depth-1, validate)
        prefix.pop()
    return acc


def part_1():
    return numbers([], 6, validate_1)


def part_2():
    return numbers([], 6, validate_2)


print('Part 1:', part_1())
print('Part 2:', part_2())
