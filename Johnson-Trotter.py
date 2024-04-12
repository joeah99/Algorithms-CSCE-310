def printPermutations(word, permutations):
    print('permutations')
    print(word)
    p = 1
    word_list = list(word)
    mobile_list = []
    direction = {}
    for x in range(len(word)):
        direction[x] = 'left'

    while p < permutations:
        for x in range(len(word) - 1):
            if direction[x] == 'left' and direction[x + 1] == 'left':
                if word[x] < word[x + 1]:
                    mobile_list.append(word[x + 1])
            else:
                if word[x] > word[x + 1]:
                    mobile_list.append(word[x])

        if len(mobile_list) != 0:
            k = max(mobile_list)
            for x in range(len(word)):
                if word[x] > k:
                    if direction[x] == 'left':
                        direction[x] = 'right'
                    else:
                        direction[x] = 'left'

            if direction[word.index(k)] == 'left':
                old_char = word[word.index(k) - 1]
                if direction[word.index(old_char)] == 'left':
                    direction[word.index(k)] = 'left'
                else:
                    direction[word.index(k)] = 'right'
                word_list[word.index(k) - 1] = word_list[word.index(k)]
                direction[word.index(k) - 1] = 'left'
            else:
                old_char = word[word.index(k) + 1]
                if direction[word.index(old_char)] == 'left':
                    direction[word.index(k)] = 'left'
                else:
                    direction[word.index(k)] = 'right'
                word_list[word.index(k) + 1] = word_list[word.index(k)]
                direction[word.index(k) + 1] = 'right'

        else:
            break
        word_list[word.index(k)] = old_char
        word = ''.join(word_list)
        print(word)
        mobile_list.clear()
        p += 1

    return


if __name__ == '__main__':
    num = int(input("number of permutations: "))
    word = input("word: ")
    printPermutations(word, num)
