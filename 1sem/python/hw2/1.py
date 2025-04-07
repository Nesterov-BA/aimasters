def hanoi(n, p_from, p_to):
    if n == 1:
        if p_from  + p_to == 4:
            print(1, p_from, 2)
            print(1, 2, p_to)
        else:
            print(1, p_from, p_to)
    else:
        h(n-1, p_from, 6-p_from-p_to)
        print(n, p_from, p_to)
        h(n-1, 6-p_from-p_to, p_to)
