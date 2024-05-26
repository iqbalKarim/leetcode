def similarPairs(words):
    checker = {}
    for word in words:
        uniq = ""
        word = sorted(word)
        for letter in word:
            if letter not in uniq:
                uniq += letter
        if f"{uniq}" not in checker:
            checker[f"{uniq}"] = 1
        else:
            checker[f"{uniq}"] += 1
    total = 0
    for key, value in checker.items():
        total += int(value*(value - 1) / 2)
    return (total)

# words = ["aba", "aabb", "abcd", "bac", "aabc", 'aab']
# words = ["aba", "aabb", 'aab']
words = ["zgtzytjkre","jjzdbxyutj","umghhnlihq","mdxjukhqsm","mqdplhuvqr","xpdhateywu","ugedwkxapc","vjpryhictr"]
print(similarPairs(words))