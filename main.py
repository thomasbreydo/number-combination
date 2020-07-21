import time


def get_numbers():
    total = float(input("Total? "))
    a = float(input("Out of what number? "))
    return total, a


def solve_using_n_repeated(total, a, repetitions):
    print(repetitions)
    time.sleep(1)


def solve(total, a):
    repetitions = 1
    while True:
        solution = solve_using_n_repeated(total, a, repetitions)
        if solution is not None:
            return solution
        repetitions += 1


def main():
    total, a = get_numbers()
    print(solve(total, a))


if __name__ == "__main__":
    main()
