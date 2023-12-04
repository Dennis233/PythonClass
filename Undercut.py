import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Human(Player):
    @staticmethod
    def choose_number():
        while True:
            try:
                number = int(input("请输入一个1~10之间的整数: "))
                if 1 <= number <= 10:
                    return number
                else:
                    print("请输入一个1~10之间的整数！")
            except ValueError:
                print("请输入一个有效的整数！")


class Computer(Player):
    @staticmethod
    def choose_number():
        return random.randint(1, 10)


class Undercut:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        number1 = self.player1.choose_number()
        number2 = self.player2.choose_number()

        print(f"{self.player1.name}选择了数字 {number1}")
        print(f"{self.player2.name}选择了数字 {number2}")

        if number1 == number2 - 1:
            print(f"{self.player1.name}获胜！")
            self.player1.score += 1
        elif number2 == number1 - 1:
            print(f"{self.player2.name}获胜！")
            self.player2.score += 1
        else:
            print("平局！")

    def play_game(self, num_rounds):
        for i in range(num_rounds):
            print(f"\n第 {i + 1} 轮游戏开始：")
            self.play_round()

        print("\n游戏结束！")
        print(f"{self.player1.name}的得分: {self.player1.score}")
        print(f"{self.player2.name}的得分: {self.player2.score}")


# 创建玩家对象
player1 = Human("Dennis")
player2 = Computer("AI")

# 创建游戏对象并开始游戏
game = Undercut(player1, player2)
game.play_game(5)
