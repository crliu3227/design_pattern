# 还是上一次谈到的快餐点餐系统。只不过，今天我们从订单的角度来构造这个系统。


# 汉堡
class Burger():
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class CheeseBurger(Burger):
    def __init__(self):
        self.name = "Cheese Burger"
        self.price = 10


class ChickenBurger(Burger):
    def __init__(self):
        self.name = "Chicken Burger"
        self.price = 15


# 小食
class Snack():
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class FrenchFries(Snack):
    def __init__(self):
        self.name = "French Fries"
        self.price = 6


class Wings(Snack):
    def __init__(self):
        self.name = "Wings"
        self.price = 12


# 饮料
class Drink():
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Coke(Drink):
    def __init__(self):
        self.name = "Coke"
        self.price = 6


class Milk(Drink):
    def __init__(self):
        self.name = "Milk"
        self.price = 5


# 我们是要建造一个订单，因而，需要一个订单类。假设，一个订单，包括一份主食，一份小食，一种饮料。
class Order():
    def __init__(self, order_builder):
        self.burger = order_builder.burger
        self.snack = order_builder.snack
        self.drink = order_builder.drink

    def show(self):
        print("Burger: %s" % self.burger.get_name())
        print("Snack: %s" % self.snack.get_name())
        print("Drink: %s" % self.drink.get_name())


# Order类中order_builder是什么呢，为什么不直接指定order内容而要通过order_builder呢
# 设想再自助点擦机上，往往是通过再各个子界面上选取食物，然后最终生成一个订单，而这个生成
# 订单的就是order_builder，也就是建造者模式中的“建造者”
class OrderBuilder():
    def add_burger(self, burger):
        self.burger = burger

    def add_snack(self, snack):
        self.snack = snack

    def add_drink(self, drink):
        self.drink = drink

    def build(self):
        return Order(self)


# 下面在场景中实现订单生成
if __name__ == "__main__":
    orderbuilder = OrderBuilder()

    orderbuilder.add_burger(ChickenBurger())
    orderbuilder.add_snack(FrenchFries())
    orderbuilder.add_drink(Coke())

    order = orderbuilder.build()

    order.show()
