def check_first_sentence_is_second(first_sentence, second_sentence):
    firstSplit = first_sentence.split()
    secondSplit = second_sentence.split()
    firstSet = set(first_words)
    secondSet = set(second_words)
    if not secondSet.issubset(firstSet)
    	return False
    for word in secondSplit:
        if firstSplit.count(word) < secondSplit.count(word):
            return False
    return True
