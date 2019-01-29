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
        with open("codes\\" + codeFileName, "r") as f:
            codeLines = [i for i in f.readlines()]

        codeWords = []
        for line in codeLines:
            r = divider.split(line)
            r = [i for i in r if i != "" and "-"]
            codeWords.append(r)

        keyLines = set()
        for keyword in keywords:
            for lineWords in codeWords:
                for i,word in enumerate(lineWords):
                    if 50 < cosine(word, keyword) < 99:
                        keyLines.add(i)
                        print("simword", word)
        print("keyLines", keyLines)
        keyLineCodes = [codeLines[i] for i in keyLines]
        print(keyLineCodes)


# def searchRecommandLine(codesFile, keyword):

recommand("1003729",["ff"])