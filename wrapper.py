# 经常喝奶茶，我们先定义一个奶茶类
class TeaWithMilk():
    def __init__(self, name="", price=0.0):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


# 奶茶又有很多种，不如红茶或者绿茶
class GreenteaWithMilk(TeaWithMilk):
    def __init__(self, name="green tea with milk", price=10.0):
        super(GreenteaWithMilk, self).__init__(name, price)


class RedteaWithMilk(TeaWithMilk):
    def __init__(self, name="red tea with milk", price=10.0):
        super(RedteaWithMilk, self).__init__(name, price)


# 除了基本配置喝奶茶配料才是最爱，比如珍珠，椰果，波霸。。。
# 而这些配料恰好为装饰
class IngredientDecorator():
    def __init__(self, name="", price=0.0):
        self.name = name
        self.price = price

    def get_name(self):
        return self.tea_with_milk.name + self.name

    def get_price(self):
        return self.tea_with_milk.price + self.price


class Coconut(IngredientDecorator):
    def __init__(self, tea_with_milk, name="coconut", price=1.0):
        super(Coconut, self).__init__(name, price)
        self.tea_with_milk = tea_with_milk


class Bubble(IngredientDecorator):
    def __init__(self, tea_with_milk, name="bubble", price=2.0):
        super(Bubble, self).__init__(name, price)
        self.tea_with_milk = tea_with_milk


# 下面开始买奶茶
if __name__ == "__main__":
    drink = GreenteaWithMilk()
    drink_with_ingredient = Coconut(drink)
    print("name: %s" % drink_with_ingredient.get_name())
    print("price: %f" % drink_with_ingredient.get_price())
