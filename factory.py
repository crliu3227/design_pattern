# 想必大家一定见过类似于麦当劳自助点餐台一类的点餐系统吧。
# 在一个大的触摸显示屏上，有三类可以选择的上餐品：汉堡等主餐、小食、饮料。
# 当我们选择好自己需要的食物，支付完成后，订单就生成了。
# 下面，我们用今天的主角--工厂模式--来生成这些食物的逻辑主体。


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


# 以上的Burger，Snack，Drink，都可以认为是该快餐店的产品，由于只提供了抽象方法，我们把它们叫抽象产品类，
# 而cheese burger等6个由抽象产品类衍生出的子类，叫作具体产品类。
# 接下来，“工厂”就要出现了。


class FoodFactory():
    # 工厂类提供接口，子类可通过该接口实例化
    def creat_food(self, foodclass):
        print("%s factory produce a instance" % self.type)
        food = foodclass()
        return food


class BurgerFactory(FoodFactory):
    def __init__(self):
        self.type = "BURGER"


class SnackFactory(FoodFactory):
    def __init__(self):
        self.type = "SNACK"


class DrinkFactory(FoodFactory):
    def __init__(self):
        self.type = "Drink"


# FoodFactory为抽象的工厂类，而BurgerFactory，SnackFactory，DrinkFactory为具体的工厂类
# 在业务场景中，工厂模式是如何“生产”产品的呢


if __name__ == "__main__":
    burger_factory = BurgerFactory()
    snack_factory = SnackFactory()
    drink_factory = DrinkFactory()

    chicken_burger = burger_factory.creat_food(ChickenBurger)
    french_fries = snack_factory.creat_food(FrenchFries)
    coke = drink_factory.creat_food(Coke)

    total = chicken_burger.get_price() + french_fries.get_price() + \
        coke.get_price()
    print("Total Price: %d" % total)
