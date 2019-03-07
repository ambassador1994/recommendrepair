import re
from parseSim import recommand
import nltk

# q1 = re.compile(r"\$?[a-zA-Z0-9.]*[Vv][Ee][Rr][Ss][Ii][Oo][Nn][a-zA-Z0-9.]* :?= ['\"]?[0-9]+.?[0-9]+")
# q2 = re.compile(r"\$")
#['\"]?[0-9]+\.?[0-9]*['\"]? 要修改 考虑多个小数点的情况！！！！！！！！！！！！！！
q1 = re.compile(r"\$?([^ \n\t;,]*version[^ \n\t;,]*)[ \n\t]*(:|:=|==|=)[ \n\t]*['\"]?([0-9][0-9.]*)['\"]?", re.I) #ok
q2 = re.compile(r"\$?([^ \n\t;,]+)[ \n\t]*(:|:=|==|=)[ \n\t]*['\"]?([0-9][0-9.]*)['\"]?") #ok
q4 = re.compile(r"([^ \n\t;,]+)\((['\"]?[0-9][0-9.]*['\"]?(, *[^ \n\t;,()]*)*)\)") #ok
q5 = re.compile(r"([^ \n\t;,]+)\(([^ \n\t;,]+([ \n\t]*,[ \n\t]*[^ \n\t;,()]+)*)\)")
q79 = re.compile(r"(ensure|version)[ \n\t]*=>[ \n\t]*(latest|[0-9]+(\.[0-9]+)*)",re.I)
q8 = re.compile(r"case [ \n\t]*=>[ \n\t]*(true|false|['\"]?[0-9]+(\.[0-9]+)*['\"]?)",re.I)
q11 = re.compile(r"/((([\w_]+|\.\.|\.)/)+)") #匹配路径
q15 = re.compile(r"\$?[^ \n\t;,]*version[^ \n\t;,]*[ \n\t]*(:|:=|==|=)([ \n\t]*(([^ \n\t.])*\.)+version)", re.I)
q1617 = re.compile(r"\$?[^ \n\t;,]*version[^ \n\t;,]*[ \n\t]*(:|:=|==|=)[ \n\t]*[^ \n.]+?\.[^ \n.]*?\([^\n]+?\)")
q18 = re.compile(r"[a-zA-Z0-9_\-.]*version ?(:|:=|==|=) ?[^\n]*", re.I)
q19 = re.compile(r"\$?[^ \n\t><+\-]*depend[^ \n\t;,]*?[ \n\t]*(:|:=|==|=)[ \n\t]*([^\n\t ]*)", re.I)

# code1 = '''my VersionTxt = \'123\' '''
# print([i.group(1) for i in q1.finditer(code1)])
# code4 = '''self.assertFailsValidation("1.0.5556", "unknown")'''
# code5 = '''TEST_P(TlsAgentTestClient, CannedHello)                                                                  TEST_P(TlsAgentTestClient, EncryptedExtensionsInClear)'''
# code7 = '''ensure => latest;'''
# code11 = '''APP_VERSION := $(shell cat $(srcdir)/../../config/version.txt)(Makefile.in)                          FIREFOX_VERSION=`cat $_topsrcdir/browser/config/version.txt(configure.in)'''
# code15 = '''var version = req.query.version;'''
# code17 = '''datadata_version = res.headers['X-Data-Version'](api.py)                                                    return (json.loads(resp.content), resp.headers['X-Data-Version'])(api.py)                                     version="0.0.3"(setup.py)
# '''
# code18 = '''usage='%prog [options] test_file_or_dir <test_file_or_dir> ...',
# version=""%prog {version} (using marionette-driver: {driver_version}"
# '''
# print([i.group() for i in q2.finditer(code1)])
# print([i.group() for i in q4.finditer(code4)])
# print([i.group() for i in q5.finditer(code5)])
# print([i.group() for i in q789.finditer(code7)])
# print([i.group() for i in q11.finditer(code11)])
# print([i.group() for i in q15.finditer(code15)])
# print([i.group() for i in q17.finditer(code17)])
# print([i.group() for i in q18.finditer(code18)])

def match(code, q):
    return [i.group() for i in q.finditer(code)]


# def recommanda(matchwords, id):
#     for i in matchwords:
#         recommand()
# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print
#     "No match!!"


import csv

with open("data.csv", "r", encoding="utf-8") as f:
    csvObj = csv.reader(f)
    data = [row for row in csvObj]
    # print(f.read())
# print(data)
# fuck
for i,v in enumerate(data):
    # print(match(v[3], q1))
    matchWords = []
    print('--------------------------------------------------------')
    print(i+2, "issueID:" ,v[0])
    if match(v[3], q2) != []:
        if match(v[3], q1) != []:
            matchWords += [i.group(1) for i in q1.finditer(v[3])] + [i.group(3) for i in q1.finditer(v[3])]
            # print([i.groups() for i in q1.finditer(v[3])])
            print("q1", match(v[3], q1))
            print("keywords in code:", matchWords)
            # recommand(v[0], matchWords)
        else:
            matchWords += [i.group(1) for i in q2.finditer(v[3])] + [i.group(3) for i in q2.finditer(v[3])]
            # print([i.groups() for i in q2.finditer(v[3])])
            print("q2", match(v[3], q2))
            print("keywords in code:", matchWords)
            # recommand(v[0], matchWords)

    if match(v[3], q5) != []:
        if match(v[3], q1617) != []:
            print("q16 or 17", match(v[3], q1617))
        elif match(v[3], q4) != []:
            matchWords += [i.group(1) for i in q4.finditer(v[3])] # 有问题， 中间会漏掉
            lines = [i.group(2) for i in q4.finditer(v[3])]
            # print(lines)
            tempKeyWordLst = []
            for i in lines:
                s = i.split(",")
                for j in s:
                    tempKeyWordLst.append(j.strip())

            matchWords += tempKeyWordLst
            print([i.groups() for i in q4.finditer(v[3])])
            print("q4", match(v[3], q4))
            print("keywords in code:", matchWords)
            # recommand(v[0], matchWords)

        else:
            matchWords += [i.group(1) for i in q5.finditer(v[3])]
            lines = [i.group(2) for i in q5.finditer(v[3])]
            # print(lines)
            tempKeyWordLst = []
            for i in lines:
                s = i.split(",")
                for j in s:
                    tempKeyWordLst.append(j.strip())

            matchWords += tempKeyWordLst
            print([i.groups() for i in q5.finditer(v[3])])
            print("q5 or 13", match(v[3], q5))
            print("keywords in code:", matchWords)
            # recommand(v[0], matchWords)

    if match(v[3], q79) != []:
        matchWords += [i.group(2) for i in q79.finditer(v[3])]
        print("q7 or 9", match(v[3], q79))
        print("keywords in code:", matchWords)
        # recommand(v[0], matchWords)

    if match(v[3], q8) != []:
        matchWords += [i.group(1) for i in q8.finditer(v[3])]
        print("q8", match(v[3], q8))
        print("keywords in code:", matchWords)
        # recommand(v[0], matchWords)

    if match(v[3], q11) != []:
        matchWords += match(v[3], q11)
        print("q11", match(v[3], q11))
        print("keywords in code:", matchWords)
        # recommand(v[0], matchWords)
    if match(v[3], q15) != []:
        matchWords += [i.group(2) for i in q15.finditer(v[3])]
        print("q15", match(v[3], q15))
        print("keywords in code:", matchWords)
        # recommand(v[0], matchWords)

    if match(v[3], q19) != []:
        matchWords += [i.group(2) for i in q19.finditer(v[3])]
        print("q19", match(v[3], q19))
        print("keywords in code:", matchWords)
        # recommand(v[0], matchWords)

    tokens = nltk.word_tokenize(v[1])
    filtered_words = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]
    print("keywords in report", tokens)
    matchWords += filtered_words
    recommand(v[0], matchWords)

