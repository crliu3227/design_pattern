# 多数游戏都有保存进度的功能，如果一局游戏下来，忘保存了进度，那么下次只能从上次进度点开始重新打了。
# 一般情况下，保存进度是要存在可持久化存储器上，本例中先以保存在内存中来模拟实现该场景的情形。
# 以模拟一个战斗角色为例。首先，创建游戏角色。
import random


class GameCharacter():
    def __init__(self):
        self._vitality = 0
        self._attack = 0
        self._defense = 0

    def display_state(self):
        print("Current state: Life: %d, Attack: %d, Defense: %d",
              (self._vitality, self._attack, self._defense))

    def init_state(self, vitality, attack, defense):
        self._vitality = vitality
        self._attack = attack
        self._defense = defense

    def save_state(self):
        return Memento(self._vitality, self._attack, self._defense)

    def recover_state(self, memento):
        self._vitality = memento.vitality
        self._attack = memento.attack
        self._defense = memento.defense


class FightCharactor(GameCharacter):
    def fight(self):
        self._vitality -= random.randint(1, 10)

# GameCharacter定义了基本的生命值、攻击值、防御值以及实现角色状态控制的方法，
# FightCharactor实现具体的“战斗”接口。为实现保存进度的细节，还需要一个备忘录，来保存进度。


class Memento():
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense


if __name__ == "__main__":
    james = FightCharactor()
    james.init_state(100, 79, 60)
    james.display_state()

    memento = james.save_state()

    james.fight()
    james.display_state()

    james.recover_state(memento)
    james.display_state()
