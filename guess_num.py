import random

n = 100  # 范围上限
num = random.randint(1, n)
i = 1

while True:
    guess = input('输入一个1~{}之间的整数：'.format(n))

    # 检查用户输入是否为整数
    if not guess.isdigit():
        print('请输入一个整数')
        continue

    guess = int(guess)

    # 检查用户输入是否在范围内
    if guess < 1 or guess > n:
        print('数字在1到{}之间'.format(n))
        continue

    if guess == num:
        if i == 1:
            print('一次就猜对了，真厉害！')
        else:
            print('猜对啦！')
        break
    elif guess > num:
        print('比这个小')
    else:
        print('比这个大')

    # 超过5次猜错进行嘲讽
    if i > 5:
        print('你运气真差，都猜了{}次了还没猜对！'.format(i))

    i += 1

print('一共猜了{}次猜对'.format(i))