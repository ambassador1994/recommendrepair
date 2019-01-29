import re
q5 = re.compile(r"[^ \n\t;,]+\([^ \n\t;,]+([ \n\t;,]*,[ \n\t;,]*[^ \n\t;,]+)*\)")
code = '''version = self.shell_output("getprop ro.build.version.release", timeout=timeout, root=root)
'''
def match(code, q):
    return [i.group() for i in q.finditer(code)]
print(match(code,q5))