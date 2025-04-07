def find_word_in_circle(circle, word):
    lWord = len(word)
    lCircle = len(circle)
    for i in range(lCircle):
        for j in range(lWord):
            index = i + j
            index = index % lCircle
            if word[j] != circle[index]:
                break
            if j == lWord - 1:
                return i, 1
        for j in range(0, -lWord, -1):
            index = i + j
            index = index % lCircle
            if word[-j] != circle[index]:
                break
            if j == -lWord + 1:
                return i, -1
    return -1


print(find_word_in_circle('hel', 'lehlehleh'))
