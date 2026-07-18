def match_words(words):
    count = 0
    lst = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)
    print(f"List of word with first and last character same:{lst}")
    return count
total_matching_words = match_words(["aba","cfx","cdddc","ab", "xyz"])
print(total_matching_words)

