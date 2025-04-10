idx_to_minphabet = "a b k d e g h i l m n z o p r s t u w y".split()
minphabet_to_idx = {idx_to_minphabet[i]: i for i in range(len(idx_to_minphabet))}

n = int(input())
wordlist = [input().replace("ng", "z") for _ in range(n)]


def word2idx(word):
    idxword = []
    for s in word:
        idxword.append(minphabet_to_idx[s])
    return idxword


print("\n".join(map(lambda x: x.replace("z", "ng"), sorted(wordlist, key=word2idx))))
