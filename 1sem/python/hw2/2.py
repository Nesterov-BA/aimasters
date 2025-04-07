def hanoi(n, p_from, p_to):
    if p_from == 2 and p_to == 1:
        hanoi(n, p_from, 3)
        hanoi(n, 3, p_to)
    elif p_from == 3 and p_to == 2:
        hanoi(n, p_from, 1)
        hanoi(n, 1, p_to)
    elif p_from == 1 and p_to == 3:
        hanoi(n, p_from, 2)
        hanoi(n, 2, p_to)
    else:
        if n > 1:
            hanoi(n - 1, p_from, 6 - p_from - p_to)
        print(n, p_from, p_to)
        if n > 1:
            hanoi(n - 1, 6 - p_from - p_to, p_to)

hanoi(2,1,3)
