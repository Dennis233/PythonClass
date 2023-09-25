# ls = [x ** 2 for x in range(1, 5)]
# print(ls)
# -------------------------------

# def removeDups(l1, l2):
#     l1[:] = [i for i in l1 if i not in l2]
#
#
# l1 = [1, 2, 3, 4]
# l2 = [1, 2, 4, 5]
# removeDups(l1, l2)
# print(l1)
# ------------------------

def getNum():
    nums = []
    while True:
        iNumStr = input('请输入数字（回车退出）：')
        try:
            while iNumStr != "":
                nums.append(eval(iNumStr))
                iNumStr = input('请输入数字（回车退出）：')
            return nums
        except:
            print('请输入数字:')


def mean(ls):
    s = 0.0
    for i in ls:
        s = s + i
    return s / len(ls)


def dev(ls):
    sdev = 0.0
    for i in ls:
        sdev = sdev + (i-mean)**2
    return sdev


print(getNum())
