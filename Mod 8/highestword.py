def findfrequencey(string, target_word):
    word_count = 0
    for words in string:
        if words == target_word:
            word_count += 1
        else:
            continue
    return word_count

print(findfrequencey("karpagam", "a"))