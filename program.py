def file_to_sequence(file_name):
    with open(file_name, 'r') as f:
        seq = [float(i) for i in f.readline().split(' ')]
        return seq


def min_of_sequence(seq):
    minimum = seq[0]
    for i in seq:
        if i < minimum:
            minimum = i
    return int(minimum) if minimum == int(minimum) else minimum


def max_of_sequence(seq):
    maximum = seq[0]
    for i in seq:
        if i > maximum:
            maximum = i
    return int(maximum) if maximum == int(maximum) else maximum


def sum_of_sequence(seq):
    s = 0
    limit = 10_000_000_000_000_000_000
    for el in seq:
        if abs(limit - s) < abs(el):
            return None
        s += el
    return int(s) if s == int(s) else s


def prod_of_sequence(seq):
    if 0 in seq:
        return 0
    else:
        limit = 10_000_000_000_000_000_000
        prod = 1
        for el in seq:
            if abs(limit / prod) < abs(el):  # Проверка на переполнение
                return None
            prod *= el
        return int(prod) if prod == int(prod) else prod


if __name__ == '__main__':
    sequence = file_to_sequence('file.txt')

    # Минимальный элемент
    print("Минимальное:", min_of_sequence(sequence))

    # Максимальный элемент
    print("Максимальное:", max_of_sequence(sequence))

    # Сумма
    result = sum_of_sequence(sequence)
    if result is not None:
        print("Сумма:", result)
    else:
        print("Сумма чисел находится вне предела допустисых значений")

    # Произведение
    result = prod_of_sequence(sequence)
    if result is not None:
        print("Произведение:", result)
    else:
        print("Произведение чисел находится вне предела допустисых значений")
