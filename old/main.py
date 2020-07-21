import itertools
import operator
import math
from exceptions import ConcatError


def get_numbers():
    Desired = float(input("Desired? "))
    a = float(input("Out of what number? "))
    return Desired, a


def like_int(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return math.isclose(n, round(n))
    raise TypeError('got a non-numeric n')


def got_desired(total, desired):
    if isinstance(desired, int):
        if like_int(total):
            return round(total) == desired
        else:
            return False
    if isinstance(desired, float):
        return total == desired


def apply_operators(operators, a):
    '''Applies each operation in `operators` in order to `a` with `a`'''
    total = a
    for operator in operators:
        try:
            total = operator(total, a)
        except (ConcatError, ZeroDivisionError):
            return None
        except ValueError:  # just one input needed
            total = operator(total)
    return total


def concat_nums(x, y):
    if like_int(x) and like_int(y):
        return float(str(int(x)) + str(int(y)))
    else:
        raise ConcatError('cannot concatenate non-integer x and y')


def reverse_sub(x, y):
    return y - x


def reverse_truediv(x, y):
    return y / x


def reverse_concat(x, y):
    return concat_nums(y, x)


OPERATORS = [
    # Commutative
    operator.add, operator.mul,
    # Not commutative
    operator.sub, reverse_sub,  operator.truediv, reverse_truediv, concat_nums,
    reverse_concat,
    # One-input
    operator.neg,
]


def solve_using_n_repeated(desired, a, repetitions):
    for operators_list in itertools.product(OPERATORS, repeat=repetitions - 1):
        total = apply_operators(operators_list, a)
        if got_desired(total, desired):
            return operators_list


def solve(desired, a):
    repetitions = 1
    while True:
        solution = solve_using_n_repeated(desired, a, repetitions)
        if solution is not None:
            return solution
        repetitions += 1


def main():
    desired, a = get_numbers()
    print(solve(desired, a))


if __name__ == "__main__":
    main()
