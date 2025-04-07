def get_new_dictionary(input_dict_name, output_dict_name):
    input = open(input_dict_name, "r")
    numOfWords = int(input.readline())
    dictIn = []
    dictOut = []
    for line in input:
        words = line.split(" ")
        cleanWords = []
        for word in words:
            getVals = list([val for val in word
                            if val.isalpha() or val.isnumeric()])
            cleanWord = "".join(getVals)
            cleanWords.append(cleanWord)
        cleanWords.pop(1)
        dictIn.append(cleanWords)
        print(cleanWords)
    print(dictIn)
    return dictOut

def parse_line(string):
    translation = ""
    translations = []
    writingWord = True
    words = string.split(" ")
    print(words)
    cleanWords = []
    for word in words:
        getVals = list([val for val in word
            if val.isalpha() or val.isnumeric()])
        cleanWord = "".join(getVals)
        cleanWords.append(cleanWord)
    cleanWords.pop(1)
    print(cleanWords)
    return None



print(get_new_dictionary("input.txt", "output.txt"))
