import copy


def words2vec(words1=None, words2=None):
    s1 = {i for i in words1}
    s2 = {i for i in words2}
    all = s1|s2
    d1 = {}.fromkeys(all,0)
    d2 = copy.deepcopy(d1)
    for i in words1:
        d1[i] += 1
    for i in words2:
        d2[i] += 1
    # print(d1)
    # print(list(d1.values()))
    # print(d2)
    # print(list(d2.values()))
    return list(d1.values()),list(d2.values())



def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA ** 0.5) * (normB ** 0.5)) * 100, 2)


def cosine(str1, str2):
    vec1, vec2 = words2vec(str1, str2)
    return cosine_similarity(vec1, vec2)


print(cosine('versionaaaaaa', 'version'))