in_test = [1, 1, 1, 4, 99, 5, 6, 0, 99]
in_main = [
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    1,
    13,
    19,
    1,
    9,
    19,
    23,
    1,
    6,
    23,
    27,
    2,
    27,
    9,
    31,
    2,
    6,
    31,
    35,
    1,
    5,
    35,
    39,
    1,
    10,
    39,
    43,
    1,
    43,
    13,
    47,
    1,
    47,
    9,
    51,
    1,
    51,
    9,
    55,
    1,
    55,
    9,
    59,
    2,
    9,
    59,
    63,
    2,
    9,
    63,
    67,
    1,
    5,
    67,
    71,
    2,
    13,
    71,
    75,
    1,
    6,
    75,
    79,
    1,
    10,
    79,
    83,
    2,
    6,
    83,
    87,
    1,
    87,
    5,
    91,
    1,
    91,
    9,
    95,
    1,
    95,
    10,
    99,
    2,
    9,
    99,
    103,
    1,
    5,
    103,
    107,
    1,
    5,
    107,
    111,
    2,
    111,
    10,
    115,
    1,
    6,
    115,
    119,
    2,
    10,
    119,
    123,
    1,
    6,
    123,
    127,
    1,
    127,
    5,
    131,
    2,
    9,
    131,
    135,
    1,
    5,
    135,
    139,
    1,
    139,
    10,
    143,
    1,
    143,
    2,
    147,
    1,
    147,
    5,
    0,
    99,
    2,
    0,
    14,
    0,
]


def part_1(numbers):
    numbers = list(numbers)
    index = 0
    while numbers[index] != 99:
        opp = numbers[index]
        a = numbers[numbers[index+1]]
        b = numbers[numbers[index+2]]
        numbers[numbers[index+3]] = a+b if opp == 1 else a*b
        index += 4

    return numbers[0]


def state_1(numbers):
    numbers = list(numbers)
    numbers[1] = 12
    numbers[2] = 2
    return numbers


def part_2(numbers):
    for a in range(100):
        for b in range(100):
            tmp_numbers = list(numbers)
            tmp_numbers[1] = a
            tmp_numbers[2] = b
            result = part_1(tmp_numbers)
            if result == 19690720:
                return 100 * a + b


print('Part 1:', part_1(state_1(in_main)))
print('Part 2:', part_2(in_main))