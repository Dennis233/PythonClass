def isIn(s1: str, s2: str) -> bool:
    if s1 in s2:
        return True
    else:
        return False


s1 = str(input('请输入一个单词：'))
s2 = str(input('请输入一个字符串：'))
print(isIn(s1, s2))

f = lambda str1, str2: str1 in str2
print(f(s1, s2))