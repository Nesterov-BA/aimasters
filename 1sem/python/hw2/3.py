def hanoi(n, p_from, p_to):
    if n == 1:
        if p_to == 2:
            print(1,p_from, 4-p_from)
        print(1, p_from, p_to)
    else:
        h(n-1, p_from, 6-p_from-p_to)
        print(n, p_from, p_to)
        h(n-1, 6-p_from-p_to, p_to)
