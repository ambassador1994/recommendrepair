import re

# q1 = re.compile(r"\$?[a-zA-Z0-9.]*[Vv][Ee][Rr][Ss][Ii][Oo][Nn][a-zA-Z0-9.]* :?= ['\"]?[0-9]+.?[0-9]+")
# q2 = re.compile(r"\$")
#['\"]?[0-9]+\.?[0-9]*['\"]? 要修改 考虑多个小数点的情况！！！！！！！！！！！！！！
q1 = re.compile(r"\$?([^ \n\t;,]*version[^ \n\t;,]*)[ \n\t]*.?(:|:=|==|=)[ \n\t]*['\"]?[0-9]+(\.[0-9]+)*['\"]?", re.I)
q2 = re.compile(r"\$?([^ \n\t;,]+)[ \n\t]*.?(:|:=|==|=)[ \n\t]*['\"]?[0-9]+(\.[0-9]+)*['\"]?")
q4 = re.compile(r"[^ \n\t;,]+\(['\"]?[0-9]+(\.[0-9]+)*['\"]?(, *[^ \n\t;,]*)*\)")
q5 = re.compile(r"[^ \n\t;,]+\([^ \n\t;,]+([ \n\t;,]*,[ \n\t;,]*[^ \n\t;,]+)*\)")
q79 = re.compile(r"(ensure|version)[ \n\t]*=>[ \n\t]*(latest|[0-9]+(\.[0-9]+)*)",re.I)
q8 = re.compile(r"case [ \n\t]*=>[ \n\t]*(true|false|['\"]?[0-9]+(\.[0-9]+)*['\"]?)",re.I)
q11 = re.compile(r"/(([\w_]+|\.\.|\.)/)+") #匹配路径
q15 = re.compile(r"\$?[^ \n\t;,]*version[^ \n\t;,]*[ \n\t]*(:|:=|==|=)[ \n\t]*(([^ \n\t.])*\.)*version", re.I)
q1617 = re.compile(r"\$?[^ \n\t;,]*version[^ \n\t;,]*[ \n\t]*(:|:=|==|=)[ \n\t]*[^ \n.]+?\.[^ \n.]*?\([^\n]+?\)")
q18 = re.compile(r"[a-zA-Z0-9_\-.]*version ?(:|:=|==|=) ?[^\n]*", re.I)
q19 = re.compile(r"\$?[^ \n\t><+\-]*depend[^ \n\t;,]*[ \n\t]*(:|:=|==|=)[ \n\t]*[^\n\t ]", re.I)

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
    print('--------------------------------------------------------')
    print(i+2, v[0])
    if match(v[3], q2) != []:
        if match(v[3], q1) != []:
            matchWords = [i.group(1) for i in q1.finditer(v[3])]
            print(1, match(v[3], q1))
            print(matchWords)
        else:
            matchWords = [i.group(1) for i in q2.finditer(v[3])]
            print(2, match(v[3], q2))
            print(matchWords)
    if match(v[3], q5) != []:
        if match(v[3], q1617) != []:
            print("16 or 17", match(v[3], q1617))
        elif match(v[3], q4) != []:
            print("4", match(v[3], q4))
        else:
            print("5 or 13", match(v[3], q5))
    if match(v[3], q79) != []:
        print("7 or 9", match(v[3], q79))
    if match(v[3], q8) != []:
        print(8, match(v[3], q8))
    if match(v[3], q11) != []:
        print(11, match(v[3], q11))
    if match(v[3], q15) != []:
        print(15, match(v[3], q15))
    if match(v[3], q19) != []:
        print(19, match(v[3], q19))