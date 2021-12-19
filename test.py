import pytest
from program import *
from math import prod
import random


def test_empty_file_to_sequence():
    with pytest.raises(ValueError):
        with open('test_file.txt', 'w') as _:
            pass
        file_to_sequence('test_file.txt')


def test_bad_format_file_to_sequence():
    with pytest.raises(ValueError):
        with open('test_file.txt', 'w') as f:
            f.write('1 2 3 aaa')
        file_to_sequence('test_file.txt')


def test_not_existing_file_to_sequence():
    with pytest.raises(FileNotFoundError):
        file_to_sequence('not_existing_file.txt')


def test_min_of_sequence():
    # Normal arguments
    test_cases = [
        ([1, 3, 5, 7], 1),
        ([5, 5, 5], 5),
        ([0.998, 0.997, 0.995, 0.996], 0.995),
        ([-1, -2, -7, -4, -6, -5], -7),
        ([1, 7.35, 84.7, -8, 0, -2, -3.5, 12], -8),
        ([-0.77, -0.65, -0.88, -0.22], -0.88),
        ([12], 12)
    ]

    for seq, res in test_cases:
        assert min_of_sequence(seq) == res

    # Special arguments
    test_cases = [
        ([1, 3, 5], int),
        ([7.0, 7.00, 7.000], int),
        ([2.2, 7.2, -2.22], float)
    ]

    for seq, res in test_cases:
        assert type(max_of_sequence(seq)) == res

    # Bad arguments
    test_cases = [
        [12, 0.2, '1354', 22],
        [5, 7, [7, 3, 5]],
        [0.88, 12, [3, 4, 5], 'wasd']
    ]

    for case in test_cases:
        with pytest.raises(TypeError):
            max_of_sequence(case)


def test_max_of_sequence():
    # Normal arguments
    test_cases = [
        ([83, 21, 33, 41, 55, 75], 83),
        ([7, 7, 7, 7, 7], 7),
        ([2.978, 2.977, 2.974, 2.979, 2.971, 2.972], 2.979),
        ([-8, -7, -5, -12, -4, -5], -4),
        ([5, 2.48, 32.774, -12, 0, -4.45, 24, 12.00], 32.774),
        ([-3.47, -3.45, -3.77, -3.11, -3.82], -3.11),
        ([22], 22)
    ]

    for seq, res in test_cases:
        assert max_of_sequence(seq) == res

    # Special arguments
    test_cases = [
        ([2, 4, 8], int),
        ([2.0, 2.000, 2.00], int),
        ([3.5, 4.5, -2.5], float)
    ]

    for seq, res in test_cases:
        assert type(max_of_sequence(seq)) == res

    # Bad arguments
    test_cases = [
        [1, 2, 'a'],
        [[1, 3], 1, 2],
        [7, 2, 'dsd', [-1, -2, -3]]
    ]

    for case in test_cases:
        with pytest.raises(TypeError):
            max_of_sequence(case)


def test_sum_of_sequence():
    # Normal arguments
    test_cases = [
        ([24, 37, 25, 15, 40, 11, 12, 7], 171),
        ([11, 11, 11, 11], 44),
        ([4.958, 4.957, 4.954, 4.959], 19.828),
        ([-1, 1, -1, 1, -1, 1], 0),
        ([-63, 68.22, 83, 4.15, -17.987, 27, 26.12], 127.503),
        ([-6.27, -6.27, -6.25, -6.23, -6.21], -31.23),
        ([15], 15),
    ]

    for seq, res in test_cases:
        assert sum_of_sequence(seq) == pytest.approx(res)

    # Special arguments
    assert sum_of_sequence([100000000000000000000, 100]) is None

    test_cases = [
        ([3, 7, 5], int),
        ([2.0, 2.000, 2.00], int),
        ([3.5, 2.5, -0.5, 1.5], int),
        ([1.5, 7.5, -2.5], float),
    ]

    for seq, res in test_cases:
        assert type(sum_of_sequence(seq)) == res

    # Bad arguments
    test_cases = [
        [1, 4, 'j'],
        [[2, 6, 1], -5, 4],
        [5.4, 20, 'ddsas', [7.3, 2, 3]]
    ]

    for case in test_cases:
        with pytest.raises(TypeError):
            sum_of_sequence(case)


def test_prod_of_sequence():
    # Normal arguments
    test_cases = [
        ([26, 20, 17, 18, 18, 8, 3, 23], 1581016320),
        ([9, 9, 9, 9], 6561),
        ([1.942, 1.944, 1.945, 1.946], 14.28920042256),
        ([-2, 2, -2, 2, -2, 2], -64),
        ([20, 20.12, 19, -8.741, -28, -15.14], -28330653.975232),
        ([-2.45, -2.44, -2.49, -2.46, -2.42], -88.614691704),
        ([6], 6)
    ]

    for seq, res in test_cases:
        assert prod_of_sequence(seq) == pytest.approx(res)

    # Special arguments
    assert prod_of_sequence([9999, 9999, 9999, 9999, 9999, 9999]) is None
    assert prod_of_sequence([9999, 9999, 9999, 9999, 9999, 9999, 0, 9999]) == 0

    test_cases = [
        ([4, 6, 2], int),
        ([7.0, 7.0000, 7.00], int),
        ([1.5, 5.5, -6.5, 2.5], float),
        ([3.5, 12.5, -25.5, 4000], int)
    ]

    for seq, res in test_cases:
        assert type(prod_of_sequence(seq)) == res

    # Bad arguments
    test_cases = [
        [2, 'p', 9],
        [3.2, 15, 4, [1, 2, 3.4]],
        ['ter', 45, [1, 2, 'g'], 22]
    ]

    for case in test_cases:
        with pytest.raises(TypeError):
            prod_of_sequence(case)


def test_stress():
    random.seed(42)
    limit = 10_000_000_000_000_000_000
    for i in range(1, 10_000):
        seq = []
        for j in range(i):
            seq.append(round(random.uniform(-100, 100), 2))
        assert min_of_sequence(seq) == min(seq)
        assert max_of_sequence(seq) == max(seq)
        assert sum_of_sequence(seq) == pytest.approx(sum(seq)) and abs(sum_of_sequence(seq)) <= limit or\
               sum_of_sequence(seq) is None and abs(sum(seq)) > limit
        assert prod_of_sequence(seq) == pytest.approx(prod(seq)) and abs(prod_of_sequence(seq)) <= limit or\
               prod_of_sequence(seq) is None and abs(prod(seq)) > limit or\
               prod_of_sequence(seq) == 0 and 0 in seq
