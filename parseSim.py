import re
from pprint import pprint
import os
from cosine import cosine
# print(os.listdir("codes"))
divider = re.compile(r"[^a-z0-9_\-]+", re.I)

def recommand(id, keywords):
    codeFileNames = [i for i in os.listdir("codes") if i.startswith(id)]
    print(codeFileNames)

    for codeFileName in codeFileNames:
        with open("codes\\" + codeFileName, "r", encoding="utf8") as f:
            codeLines = [i for i in f.readlines()]

        codeWords = []
        for line in codeLines:
            r = divider.split(line)
            r = [i for i in r if i != "" and "-"]
            codeWords.append(r)

        keyLines = set()
        for keyword in keywords:
            for i,lineWords in enumerate(codeWords):
                for word in lineWords:
                    if 90 < cosine(word, keyword) < 100:
                        keyLines.add(i)
                        print("similar word: line", i, word)

        keyLines = list(keyLines)
        keyLines.sort()
        print("keyLines", keyLines)
        keyLineCodes = [codeLines[i] for i in keyLines]
        print()
        print("推荐结果")
        # print(keyLineCodes)
        for i in keyLineCodes:
            print(i, end='')
        print()
        return keyLineCodes


# def searchRecommandLine(codesFile, keyword):
if __name__ == "__main__":

    recommand("1003729",["ff"])