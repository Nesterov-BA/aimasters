def find_max_substring_occurrence(input_string):
    length = len(input_string)
    factors = []
    substring = []
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            factors.append(i)
    for subLen in factors:
        i = 0
        num = length // subLen
        while i < subLen:
            for j in range(num):
                print(i, j)
                if input_string[i] != input_string[j * subLen + i]:
                    i = subLen
                    break
            i += 1
            if i == subLen:
                return num
    return 1


print(find_max_substring_occurrence('ababa'))
